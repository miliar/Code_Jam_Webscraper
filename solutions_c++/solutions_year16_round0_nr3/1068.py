#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include <string>
#include <cstring>
#include <utility>
#include <algorithm>
#include <cmath>
using namespace std;

int const LONG_BASE=100000000;
int const MAX_DIGITS_ON_DEFAULT = 35;
short const LESS=0;
short const EQUAL=1;
short const MORE=2;

int calculate_base_deg() {
	int ans=0,x=LONG_BASE;
	while (x>0) {
		ans++;
		x/=10;
	}
	return ans-1;
}

/*---------------------------------tlong unsigned int-------------------------------------------------------------*/
class Tlong_Unsigned_Int {
	int len;
	int max_digits;
	int *s;
	
	public:
		Tlong_Unsigned_Int(int);
		Tlong_Unsigned_Int(const Tlong_Unsigned_Int&);
		Tlong_Unsigned_Int(const string &st);
		Tlong_Unsigned_Int(double);
		
		~Tlong_Unsigned_Int();

		void trim();
		
		friend short compare (const Tlong_Unsigned_Int&,const Tlong_Unsigned_Int&,int);
		bool equal_null() const;
		Tlong_Unsigned_Int& operator = (const Tlong_Unsigned_Int&);
		void expand(int);
		
		friend void sub(const Tlong_Unsigned_Int&,const Tlong_Unsigned_Int&,Tlong_Unsigned_Int &,int);
		
		friend Tlong_Unsigned_Int operator + (const Tlong_Unsigned_Int&,const Tlong_Unsigned_Int&);
		friend Tlong_Unsigned_Int operator - (const Tlong_Unsigned_Int&,const Tlong_Unsigned_Int&);
		friend Tlong_Unsigned_Int operator * (const Tlong_Unsigned_Int&,const Tlong_Unsigned_Int&);
		friend Tlong_Unsigned_Int operator / (const Tlong_Unsigned_Int&,const Tlong_Unsigned_Int&);
		friend Tlong_Unsigned_Int operator % (const Tlong_Unsigned_Int&,const Tlong_Unsigned_Int&);
		
		Tlong_Unsigned_Int& operator += (const Tlong_Unsigned_Int&);
		Tlong_Unsigned_Int& operator -= (const Tlong_Unsigned_Int&);
		Tlong_Unsigned_Int& operator *= (const Tlong_Unsigned_Int&);
		Tlong_Unsigned_Int& operator /= (const Tlong_Unsigned_Int&);
		Tlong_Unsigned_Int& operator %= (const Tlong_Unsigned_Int&);

		friend ostream& operator << (ostream &stream,const Tlong_Unsigned_Int&);
		void print_to_str(string &) const;
		friend istream& operator >> (istream &stream,Tlong_Unsigned_Int&);
		
		void make_shift(int);
		void truncate(int);
		int kol_digits() const;
};

Tlong_Unsigned_Int::Tlong_Unsigned_Int(int max_dig=MAX_DIGITS_ON_DEFAULT):max_digits(max_dig),len(1) {
	s=new int[max_digits];
	s[0]=0;
}

Tlong_Unsigned_Int::Tlong_Unsigned_Int(const Tlong_Unsigned_Int& a):max_digits(a.max_digits),len(a.len) {
	s=new int[max_digits];
	for (int i=0; i<max_digits; ++i) s[i]=a.s[i];
}

Tlong_Unsigned_Int::Tlong_Unsigned_Int(const string &st) {
	int BASE_DEG=calculate_base_deg(),n=(int) st.length();
	len=n/BASE_DEG;
	max_digits=len+(n%BASE_DEG>0);
	s=new int[max_digits];
	fill(s,s+max_digits,0);
	if (n%BASE_DEG) for (int i=0; i<n%BASE_DEG; i++) s[len]=s[len]*10+(st[i]-'0');
	for (int i=1; i<=len; i++)
		for (int j=(i-1)*BASE_DEG; j<i*BASE_DEG; j++)
			s[len-i]=s[len-i]*10+(st[j+n%BASE_DEG]-'0');
	len+=(n%BASE_DEG>0);
	trim();
}

Tlong_Unsigned_Int::Tlong_Unsigned_Int(double x) {
	char st[100];
	string new_st;
	sprintf(st,"%.16e",x);
	int pos_point=-1,i;
	for (i=0; st[i]; ++i)
		if (st[i]=='.') pos_point=i;
		else if (st[i]=='e') break;
		else new_st+=st[i];
	Tlong_Unsigned_Int c(new_st);
	len=c.len;
	max_digits=c.max_digits;
	s=new int[max_digits];
	int xx;
	sscanf(st+i+1,"%d",&xx);
	int deg=xx-(i-pos_point-1);
	for (i=0; i<len; ++i) s[i]=c.s[i];
	if (deg<0) truncate(-deg);
	else make_shift(deg);
}

Tlong_Unsigned_Int::~Tlong_Unsigned_Int() {
	delete[] s;
}

void Tlong_Unsigned_Int::trim() {
	while (len>1 && !s[len-1]) --len;
}

short compare (const Tlong_Unsigned_Int& a,const Tlong_Unsigned_Int& b,int sp=0) {
	if (a.equal_null() && b.equal_null()) return EQUAL;
	if (a.equal_null()) return LESS;
	if (b.equal_null()) return MORE;
	if (a.len>b.len+sp) return MORE;
	else if (a.len<b.len+sp) return LESS;
	for (int i=b.len-1; i>=0; --i)
		if (a.s[i+sp]>b.s[i]) return MORE;
		else if (a.s[i+sp]<b.s[i]) return LESS;
	for (int i=0; i<sp; ++i)
		if (a.s[i]) return MORE;
	return EQUAL;
}

bool Tlong_Unsigned_Int::equal_null() const {
	return (len==1) && (!s[0]);
}

void Tlong_Unsigned_Int::expand(int max_dig) {
	if (max_digits<max_dig) {
		int *t=s;
		max_digits=max_dig;
		s=new int[max_digits];
		for (int i=0; i<len; i++) s[i]=t[i];
		delete [] t;
	}
}

Tlong_Unsigned_Int& Tlong_Unsigned_Int::operator = (const Tlong_Unsigned_Int& a) {
	expand(a.max_digits);
	len=a.len;
	for (int i=0; i<len; ++i) s[i]=a.s[i];
	return *this;
}

Tlong_Unsigned_Int operator + (const Tlong_Unsigned_Int& a,const Tlong_Unsigned_Int& b) {
	Tlong_Unsigned_Int t(a);
	return t+=b;
}
		
Tlong_Unsigned_Int operator - (const Tlong_Unsigned_Int& a,const Tlong_Unsigned_Int& b) {
	Tlong_Unsigned_Int t(a);
	return t-=b;
}

Tlong_Unsigned_Int operator * (const Tlong_Unsigned_Int& a,const Tlong_Unsigned_Int& b) {
	Tlong_Unsigned_Int t(a);
	return t*=b;
}

Tlong_Unsigned_Int operator / (const Tlong_Unsigned_Int& a,const Tlong_Unsigned_Int& b) {
	Tlong_Unsigned_Int t(a);
	return t/=b;
}

Tlong_Unsigned_Int operator % (const Tlong_Unsigned_Int& a,const Tlong_Unsigned_Int& b) {
	Tlong_Unsigned_Int t(a);
	return t%=b;
}

Tlong_Unsigned_Int& Tlong_Unsigned_Int::operator += (const Tlong_Unsigned_Int& b) {
	int per=0,ss,bb,k=max(len,b.len)+1;
	expand(k);
	for (int i=0; i<k; ++i) {
		if (i>=len) ss=0;
		else ss=s[i];
		if (i>=b.len) bb=0;
		else bb=b.s[i];
		int new_s=(ss+bb+per)%LONG_BASE;
		per=(ss+bb+per)/LONG_BASE;
		s[i]=new_s;
	}
	len=k;
	trim();
	return *this;
}

Tlong_Unsigned_Int& Tlong_Unsigned_Int::operator -= (const Tlong_Unsigned_Int& b) {
	sub(*this,b,*this,0);
	return *this;
}

Tlong_Unsigned_Int& Tlong_Unsigned_Int::operator *= (const Tlong_Unsigned_Int& b) {
	Tlong_Unsigned_Int c(len+b.len);
	for (int i=0; i<c.max_digits; ++i) c.s[i]=0;
	for (int i=0; i<len; ++i)
		for (int j=0; j<b.len; ++j) {
			long long dv=c.s[i+j]+s[i]*((long long) b.s[j]);
			c.s[i+j+1]+=(int) (dv/LONG_BASE);
			c.s[i+j]=(int) (dv%LONG_BASE);
		}
	c.len=len+b.len;
	c.trim();
	swap(*this,c);
	return *this;
}

Tlong_Unsigned_Int& Tlong_Unsigned_Int::operator /= (const Tlong_Unsigned_Int& b) {
	string st;
	switch (compare(*this,b)) {
		case LESS:st="0";
				  (*this)=st;
				  break;
		case EQUAL:st="1";
				   (*this)=st;
			       break;
		case MORE:{
			       int sp=len-b.len;
				   Tlong_Unsigned_Int ost(*this),c(1);
				   if (compare(ost,b,sp)==LESS) sp--;
				   Tlong_Unsigned_Int res(sp+1);
				   res.len=sp+1;
				   while (sp>=0) {
				      int up=LONG_BASE,down=0,mid;
					  while (up>down) {
					     mid=(up+down)/2;
						 c.s[0]=mid;
						 if (compare(ost,b*c,sp)==LESS) up=mid;
						 else down=mid+1;
					  }
					  down--;
					  c.s[0]=down;
					  sub(ost,b*c,ost,sp);
					  res.s[sp--]=down;
				   }
				   swap(*this,res);
				   break;
				  }
	}
	return *this;
}

Tlong_Unsigned_Int& Tlong_Unsigned_Int::operator %= (const Tlong_Unsigned_Int& b) {
	(*this)-=((*this)/b)*b;
	return *this;
}

void sub(const Tlong_Unsigned_Int& a,const Tlong_Unsigned_Int& b,Tlong_Unsigned_Int &c,int sp) {
	c.expand(a.len);
	c.len=a.len;
	for (int i=0; i<sp; i++) c.s[i]=a.s[i];
	int z=0;
	for (int i=sp; i<a.len; i++) {
		if (i-sp>=b.len) c.s[i]=a.s[i]-z;
		else c.s[i]=a.s[i]-b.s[i-sp]-z;
		z=0;
		if (c.s[i]<0) {
			z=1;
			c.s[i]+=LONG_BASE;
		}
	}
	c.trim();
}		

ostream& operator << (ostream &stream,const Tlong_Unsigned_Int& x) {
	int BASE_DEG=calculate_base_deg();
	stream<<x.s[x.len-1];
	for (int i=x.len-2; i>=0; --i) {
		stream.width(BASE_DEG);
		stream.fill('0');
		stream<<x.s[i];
	}
	return stream;
}

istream& operator >> (istream &stream,Tlong_Unsigned_Int& x) {
	string st;
	stream>>st;
	x=st;
	return stream;
}

void Tlong_Unsigned_Int::make_shift(int sp) {
	int BASE_DEG=calculate_base_deg();
	int i;
	expand(len+sp/BASE_DEG+(sp%BASE_DEG>0));
	for (i=len+sp/BASE_DEG-1; i>=sp/BASE_DEG; --i) s[i]=s[i-sp/BASE_DEG];
	for (i=0; i<sp/BASE_DEG; ++i) s[i]=0;
	len+=sp/BASE_DEG;
	sp%=BASE_DEG;
	i=1;
	while (sp-->0) i*=10;
	Tlong_Unsigned_Int c(1);
	c.s[0]=i;
	(*this)*=c;
}

void Tlong_Unsigned_Int::truncate(int sp) {
	int BASE_DEG=calculate_base_deg();
	int i;
	for (i=0; i<len-sp/BASE_DEG; ++i) s[i]=s[i+sp/BASE_DEG];
	len-=sp/BASE_DEG;
	i=1;
	sp%=BASE_DEG;
	while (sp-->0) i*=10;
	Tlong_Unsigned_Int c(1);
	c.s[0]=i;
	(*this)/=c;
}

int Tlong_Unsigned_Int::kol_digits() const {
	int ans=(len-1)*calculate_base_deg();
	int k=s[len-1];
	while (k>0) {
		ans++;
		k/=10;
	}
	return ans;
}

void Tlong_Unsigned_Int::print_to_str(string &st) const {
	st.clear();
	int BASE_DEG=calculate_base_deg();
	for (int i=len-1; i>=0; --i) {
		int pos=(int) st.length();
		int x=s[i],kol=0;
		while (x>0) {
			kol++;
			st.insert(st.begin()+pos,(x%10)+'0');
			x/=10;
		}
		if (i!=len-1) {
			kol=BASE_DEG-kol;
			while (kol-->0) st.insert(st.begin()+pos,'0');
		}
	}
	if (st.empty()) st="0";
}
/*---------------------------------tlong unsigned int-------------------------------------------------------------*/

int const MAX_N = 200100;
int const MAX_CH = 100100;
int const INT_INF = 1000000000;
int const MAX_GEN = 1000000;

int p[MAX_GEN],all_p[MAX_GEN],all_p_len = 0;
char st[MAX_CH];

struct one_node {
	string st;
	vector<long long> dvv;

	one_node() {}
	one_node(string st, vector<long long> dvv):st(st),dvv(dvv) {}
};
vector<one_node> ans;

string loc_st;
vector<long long> loc_dvv;

Tlong_Unsigned_Int clc;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	for (int i=0; i<MAX_GEN; i++) p[i] = 1;
	p[0] = p[1] = 0;
	for (int i=2; i<MAX_GEN; i++)
		if (p[i])
			for (int j=i+i; j<MAX_GEN; j+=i)
				p[j] = 0;

	for (int i=2; i<MAX_GEN; i++)
		if (p[i]) all_p[all_p_len++] = i;

	int t;
	gets(st);
	sscanf(st,"%d",&t);
	int ind = 0;
	ans.clear();
	while (t-->0) {
		ind++;
		printf("Case #%d:",ind);
		
		int n, to_gen;
		gets(st);
		sscanf(st,"%d%d",&n,&to_gen);

		long long iter = 0;

		for (int code=0; code<(1<<(n-2)) && ((int) ans.size()) < to_gen; code++) {
			iter++;
			cerr<<"\r"<<iter<<"    Fnd = "<<(int) ans.size()<<"                   ";

			int is_Ok = 1;
			loc_dvv.clear();
			loc_st = "";
			loc_st += (char) '1';
			for (int j=n-3; j>=0; j--)
				if ((code>>j)&1) loc_st += (char) '1';
				else loc_st += (char) '0';
			loc_st += (char) '1';

			for (int osn = 2; osn <= 10 && is_Ok; osn++) {
				clc = 1.0;
				for (int j=1; j<(int) loc_st.length(); j++)
					clc = clc * Tlong_Unsigned_Int((double) osn) + Tlong_Unsigned_Int((double) (loc_st[j]-'0'));

				long long cur_dv = -1;
				for (int j=0; j<all_p_len && compare(clc, (double) all_p[j]) == MORE; j++)
					if (compare(clc % ((double) all_p[j]), 0.0) == EQUAL) {
						cur_dv = all_p[j];
						break;
					}

				if (cur_dv < 0) {
					is_Ok = 0;
					break;
				}

				loc_dvv.push_back(cur_dv);
			}

			if (is_Ok)
				ans.push_back(one_node(loc_st, loc_dvv));
		}

		for (int i=0; i<(int) ans.size(); i++) {
			cout<<"\n";
			cout<<ans[i].st;
			for (int j=0; j<(int) ans[i].dvv.size(); j++)
				cout<<" "<<ans[i].dvv[j];
		}
	}
	return 0;
}