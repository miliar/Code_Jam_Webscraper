#include <vector>
#include <string>
#include <iostream>
#include <string.h>
#include <stdio.h>
#include <algorithm>

#define abs(a) ((a)>=0?(a):-(a))

using namespace std;

class LargeInteger
{
public:

	LargeInteger(const char * s);

	LargeInteger(unsigned long long a = 0):negative(false)
	{
		if( a == 0 ) 
		{
			v.resize(1);
			n = 0;
			return ;
		}

		while(a)
		{
			v.push_back(a%base);
			a /= base;
		}
		n = v.size();
	}

	LargeInteger(long long a)
	{
		bool t = (a<0);
		*this = (unsigned long long) abs(a);
		negative = t;
	}

	LargeInteger(int a)
	{
		*this = (long long) a;
	}

	LargeInteger(short a)
	{
		*this = (long long) a;
	}

	LargeInteger(char a)
	{
		*this = (long long) a;
	}

	LargeInteger(unsigned int a)
	{
		*this = (unsigned long long)a;
	}

	LargeInteger(unsigned short a)
	{
		*this = (unsigned long long)a;
	}

	LargeInteger(unsigned char a)
	{
		*this = (unsigned long long)a;
	}

	LargeInteger operator + (const LargeInteger &other) const
	{
		LargeInteger ret;
		add(this , &other , &ret);
		return ret;
	}

	LargeInteger &operator +=(const LargeInteger &other)
	{
		add(this , &other , this);
		return *this;
	}

	LargeInteger operator - (const LargeInteger &other) const
	{
		LargeInteger ret;
		sub(this , &other , &ret);
		return ret;
	}

	LargeInteger &operator -=(const LargeInteger &other)
	{
		sub(this ,  &other , this);
		return *this;
	}

	LargeInteger operator * (const LargeInteger &other) const
	{
		LargeInteger ret;
		mul(this , &other , &ret);
		return ret;
	}

	LargeInteger &operator *=(const LargeInteger &other)
	{
		mul(this ,  &other , this);
		return *this;
	}

	LargeInteger operator / (const LargeInteger &other) const
	{
		LargeInteger ret;
		div(this , &other , &ret , NULL);
		return ret;
	}

	LargeInteger &operator /= (const LargeInteger &other)
	{
		div(this , &other , this , NULL);
		return *this;
	}

	LargeInteger operator % (const LargeInteger &other) const
	{
		LargeInteger ret;
		div(this , &other , NULL , &ret);
		return ret;
	}

	LargeInteger &operator %= (const LargeInteger &other)
	{
		div(this , &other , NULL , this);
		return *this;
	}

	LargeInteger operator ^(unsigned long long p)
	{
		LargeInteger ret = 1;
		for(LargeInteger t = *this ; p ; p >>= 1)
		{
			if(p & 1) ret *= t;
			t *= t;
		}
		return ret;
	}

	bool operator < (const LargeInteger &other) const
	{
		return compare(*this , other) < 0;
	}

	bool operator > (const LargeInteger &other) const
	{
		return compare(*this , other) > 0;
	}

	bool operator == (const LargeInteger &other) const
	{
		return compare(*this , other) == 0;
	}

	bool operator <= (const LargeInteger &other) const
	{
		return compare(*this , other) <= 0;
	}

	bool operator >= (const LargeInteger &other) const
	{
		return compare(*this , other) >= 0;
	}

	bool operator != (const LargeInteger &other) const
	{
		return compare(*this , other) != 0;
	}

	LargeInteger operator -() const
	{
		LargeInteger ret = *this;
		ret.negative = !ret.negative;
		return ret;
	}

	LargeInteger operator +() const
	{
		return *this;
	}

	LargeInteger absolute() const
	{
		LargeInteger ret = *this;
		ret.negative = false;
		return ret;
	}

	string ToString();

	static void add(const LargeInteger *pa ,const LargeInteger *pb, LargeInteger *pc);
	static void sub(const LargeInteger *pa ,const LargeInteger *pb, LargeInteger *pc);
	static void mul(const LargeInteger *pa ,const LargeInteger *pb, LargeInteger *pc);
	static void div(const LargeInteger *pa ,const LargeInteger *pb ,LargeInteger *pc , LargeInteger *pd);

private:
	static int compare(const int *pa , int an , const int *pb , int bn);
	static int compare(const LargeInteger &a , const LargeInteger &b);

	static void add(const int *pa , int an , const int *pb , int bn ,int *pc , int &cn);
	static bool sub(const int *pa , int an , const int *pb , int bn ,int *pc , int &cn);
	static void mul(const int *pa , int an , const int *pb , int bn ,int *pc , int &cn);
	static void div(      int *pa , int &an, const int *pb , int bn, int *pc , int &cn); //a既是输入被除数也是余数

	static void mul(const int *pa , int an ,long long b, int *c , int &cn);
	static int div(const int *pa,const int an,const int *pb,const int bn);

	static int ValueToStr(int val, char *s,int n)
	{
		int ret = 0;
		s[n] = 0;
		for(int i = n - 1; i >= 0 ; i--)
		{
			s[i] = (val % 10) + '0';
			val /= 10;
			if(val == 0 && ret == 0) ret = i;
		}
		return ret;
	}

	static int StrToValue(const char *s,int n)
	{
		int ret = 0;
		for(int i = 0; i < n; i++)
		{
			ret *= 10;
			ret += s[i] - '0';
		}
		return ret;
	}

	vector<int> v;
	int n;
	bool negative;
	static const int base;
};

const int LargeInteger::base = 1000000000;

LargeInteger::LargeInteger(const char * s)
{
	if( *s == '-' || *s == '+') negative = ( *s++ == '-');
	else negative = false;

	while( *s && *s == '0' ) s++;

	if( !*s ) { *this = 0; return; }

	int len = strlen(s) , i;
	for( i = len - 9; i >= 0 ; i -= 9) v.push_back(StrToValue(s+i,9));

	if( (i += 9) > 0) v.push_back(StrToValue(s,i));

	n = v.size();
}

string LargeInteger::ToString()
{
	if( n == 0 ) return "0";

	char s[10];
	int *p = &v[0];
	string ret;

	if(negative) ret += '-';

	ret += (s + ValueToStr( p[n-1] , s , 9));

	for(int i = n - 2; i >= 0; i--)
	{
		ValueToStr(p[i] , s , 9);
		ret += s;
	}

	return ret;
}

int LargeInteger::compare(const int *pa , int an , const int *pb , int bn )
{
	if( an == bn )
	{
		for(int i=an-1 ; i >= 0 ; i--)
		{
			if(pa[i] != pb[i]) return pa[i] - pb[i];
		}
		return 0;
	}
	return an - bn;
}

int LargeInteger::compare(const LargeInteger &a , const LargeInteger &b)
{
	if( a.negative != b.negative)
	{
		return b.negative - a.negative;
	}
	return b.negative ? -compare( &a.v[0], a.n, &b.v[0], b.n) : compare( &a.v[0], a.n, &b.v[0], b.n);
}

void LargeInteger::add(const LargeInteger *pa ,const LargeInteger *pb, LargeInteger *pc)
{
	pc->v.resize( max(pa->n,pb->n) + 1);

	if( pa->negative == pb->negative )
	{
		pc->negative = pa->negative;
		add(&pa->v[0] ,pa->n , &pb->v[0] , pb->n , &pc->v[0] , pc->n);
	}
	else
	{
		pc->negative = sub(&pa->v[0] ,pa->n , &pb->v[0] , pb->n , &pc->v[0] , pc->n) ? \
			!pa->negative : pa->negative;

		if(pc->n == 0) pc->negative = false;
	}
}

void LargeInteger::sub(const LargeInteger *pa ,const LargeInteger *pb, LargeInteger *pc)
{
	pc->v.resize( max(pa->n,pb->n) + 1);

	if( pa->negative == pb->negative )
	{   
		pc->negative = sub(&pa->v[0] ,pa->n , &pb->v[0] , pb->n , &pc->v[0] , pc->n) ? \
			!pa->negative : pa->negative;

		if(pc->n == 0) pc->negative = 0;
	}
	else
	{
		pc->negative = pa->negative;
		add(&pa->v[0] ,pa->n , &pb->v[0] , pb->n , &pc->v[0] , pc->n);
	}
}

void LargeInteger::mul(const LargeInteger *pa ,const LargeInteger *pb, LargeInteger *pc)
{
	pc->negative = (pa->negative != pb->negative);

	if( pa->n == 0 || pb->n == 0)
	{
		*pc = 0;
		return ;
	}

	pc->v.resize(pa->n+pb->n);
	mul(&pa->v[0] , pa->n , &pb->v[0] , pb->n , &pc->v[0] , pc->n);
}

void LargeInteger::div(const LargeInteger *pa ,const LargeInteger *pb ,LargeInteger *pc , LargeInteger *pd)
{
	LargeInteger td = *pa;
	LargeInteger tc;
	if( pb->n == 0 )
		throw "Divided by 0";
	tc.negative = (pa->negative != pb->negative);
	tc.v.resize(pa->n,0);
	div(&td.v[0], td.n , &pb->v[0], pb->n , &tc.v[0], tc.n);
	if( tc.n == 0 ) tc.negative = false;
	if( td.n == 0 ) td.negative = false;
	if(pc) *pc = tc;
	if(pd) *pd = td;
}


void LargeInteger::add(const int *pa , int an , const int *pb , int bn ,int *pc , int &cn)
{
	int t = 0 , i;

	if( an < bn )
	{
		swap(pa,pb);
		swap(an,bn);
	}

	for( i = 0; i < bn ; i++)
	{
		t = pa[i] + pb[i] + (t>=base);
		pc[i] = (t>=base) ? t - base : t;
	}

	for( ; i < an ; i++)
	{
		t = pa[i] + (t>=base);
		pc[i] = (t>=base) ? t - base : t; 
	}

	if(t>=base) pc[i++] = 1;
	cn = i;
}

bool LargeInteger::sub(const int *pa , int an , const int *pb , int bn ,int *pc ,int &cn)
{
	int t = 0 ,i;
	bool swaped = false;

	if(compare(pa,an,pb,bn) < 0)
	{
		swaped = true;
		swap(pa,pb);
		swap(an,bn);
	}

	for(i = 0 ; i < bn ; i++)
	{
		t = pa[i] - pb[i] - (t<0);
		pc[i] = (t<0) ? t + base : t;
	}

	for( ; i < an; i++)
	{
		t = pa[i] - (t<0);
		pc[i] = (t<0) ? t + base : t;
	}

	while( --i >= 0 && pc[i] == 0 );
	cn = i + 1; 

	return swaped;
}

void LargeInteger::mul(const int *pa , int an ,long long b, int *c ,int &cn)
{
	cn = 0;
	if( b == 0 ) return;
	long long t = 0;
	for( ; cn < an ; cn++)
	{
		t = b * pa[cn] + t / base;
		c[cn] = (t % base);
	}
	if(t/=base) c[cn++] = t;
}


void LargeInteger::mul(const int *pa , int an , const int *pb , int bn ,int *pc ,int &cn)
{
	int *pSum = new int[an+bn];
	int *pProduct = new int[an+bn];
	int nProduct;
	cn = 0;
	memset(pSum,0,sizeof(int)*(an+bn));
	for(int i = 0; i < bn; i++)
	{
		mul(pa,an,pb[i],pProduct+i,nProduct);
		add(pProduct,nProduct+i,pSum,cn,pSum,cn);
		pProduct[i] = 0;
	}

	memcpy(pc,pSum,cn*sizeof(int));
	delete []pSum;
	delete []pProduct;
}

int LargeInteger::div(const int *pa,const int an,const int *pb,const int bn)
{
	int *pc = new int[bn+1];
	int cn;

	long long s = 0 , e = base , m;
	while( s + 1 < e )
	{
		m = (s + e) >> 1;
		mul(pb,bn,m,pc,cn);

		if(compare(pc,cn,pa,an) > 0) e = m;
		else s = m;
	}

	delete []pc;
	return s;
}

void LargeInteger::div(int *pa , int &an, const int *pb , int bn, int *pc , int &cn)
{
	int t;
	int *pt = new int[an+1];
	int *pfa = pa + an - bn;
	int tn, fan = bn;

	memset(pc,0,sizeof(int)*an);
	while( pfa >= pa )
	{
		t = div(pfa , fan , pb , bn);
		pc[pfa-pa] = t;
		mul(pb,bn,t,pt,tn);
		sub(pfa,fan,pt,tn,pfa,fan);

		if( bn != fan )
		{
			pfa -= (bn - fan); 
			fan = bn;
		}
		else
		{
			pfa--;
			fan++;
		}
	}

	cn = an - bn + 1;
	if( cn < 0 ) cn = 0;
	if( cn - 1 >= 0 && pc[cn-1] == 0) cn--;

	while( --an >=0 && pa[an] == 0);
	an++;

	delete []pt;
}


////////////////////////////////////////////////////////////////////////////////////////////////

LargeInteger table[50000];
int tc;

bool check(const char str[])
{
	int len = strlen(str) - 1;
	for(int i = 0; str[i]; i++)
		if( str[i] != str[len-i] ) return false;
	return true;
}

void f(char str[],int n,int s,int e)
{
	if( n == 0 )
	{
		table[tc] = str;
		table[tc] *= table[tc];
		tc++;
		return ;
	}

	while( s < e )
	{
		str[s] = '1';
		str[e] = '1';
		f(str,n-1,s+1,e-1);
		str[s] = '0';
		str[e] = '0';
		s++;
		e--;
	}
}

void ff(char str[],int ni,char se,char m,bool bm)
{
	str[0] = se;
	for(int i = 0; i < ni; i++ )
		for(int j = i + 2; j <= 51; j++) 
		{
			str[j-1] = se;
			str[j] = 0;
			if( j % 2 == 1 )
			{
				str[j/2] = m;
				f(str,i,1,j-2);
				str[j/2] = '0';
			}
			if(!bm) f(str,i,1,j-2);
			str[j-1] = str[j] = '0';
		}
}


void MakeTable()
{
	char str[60];
	tc = 0;
	memset(str,'0',sizeof(str));
	ff(str,4,'1','1',false);
	ff(str,2,'1','2',true);
	ff(str,1,'2','1',false);
	for(int i = 0; i < 4; i++) table[tc++] = i * i;
}

int main()
{
	int T,c=1;
	char s1[105],s2[105];
	
	MakeTable();
	sort(table,table+tc);

	scanf("%d",&T);
	while(T--)
	{
		scanf("%s%s",s1,s2);
		LargeInteger a(s1),b(s2);
		printf("Case #%d: %d\n",c++,upper_bound(table,table+tc,b) - lower_bound(table,table+tc,a));
	}
	return 0;
}
