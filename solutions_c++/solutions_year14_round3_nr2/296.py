//using standard c++0x
//compile with gc 4.8.1: g++ -O2 -std=c++0x
//or Visual Studio Exress 2013

#include <stdio.h>
#include <map>
#include <stdarg.h>
#include <string>
#include <math.h>
#include <stdlib.h>
#include <set>
#include <stack>
#include <vector>
#include <functional>
#include <algorithm>
#include <cstdlib>

typedef unsigned long uint;
typedef unsigned long long ull;
using namespace std;

template<class T, class Cmp>
set<T,Cmp> &operator<<(set<T,Cmp> &s, const T&x){
	s.insert(x); return s;
}

template<class T>
struct arr{
	T *p;
	int sz;
	arr(int n=0){if((sz=n)>0)p=new T[n];else p=0;}
	void resize(int n){
		if(n==sz)return;
		delete[]p;
		if((sz=n)>0)p=new T[n];else p=0;
	}
	arr<T>& operator=(const arr<T>&a){
		resize(a.sz);
		for(int i=0; i<sz; i++)p[i]=a.p[i];
		return *this;
	}
	arr(const arr<T>&a){
		p=0; sz=0;*this = a;
	}
	void clear(){resize(0);}
	~arr(){delete []p;p=0;}
	void swap(arr<T> &a){std::swap(a.p,p); std::swap(sz,a.sz);}
	operator T*(){return p;}
};
typedef arr<int> intarr;
typedef arr<long long> llarr;
typedef arr<double> doublearr;
typedef arr<string> stringarr;

struct file{
	FILE *f;
	file(){f=0;}
	file(const char* n, const char *mode){
		f = fopen(n, mode);
	}
//	bool operator !()const{return !f;}
	~file(){if(f)fclose(f); f=0;}
	bool read(const char *fmt, ...);
//	void write(const char *fmt, ...);
	bool operator!()const{return !f;}
private:
	file(const file&);
	file&operator=(const file&f);
};
int power(int i, int n){
	int res=1, t=1;
	for(;n;n>>=1){
		t*=i;
		if(n&1)res*=t;
	}
	return res;
}
int read_int(const char *&str, const map<string,int> &m, char end);
const char* space(const char *&str){
	while(*str == ' ')str++;
	return str;
}
int read_s(const char *&str, const map<string,int> &m){
	space(str);
	char s0[100], *ps = s0;
	if(!*str)return -1;
	if(*str=='('){
		++str;
		return read_int(str, m, ')');
	}
	if(*str>='0'&&*str<='9'){
		int r=*str-'0';
		for(str++; *str>='0'&&*str<='9'; str++)
			r=r*10+(*str-'0');
		return r;
	}
	while((*str>='a'&&*str<='z')||(*str>='A'&&*str<='Z')||*str=='_')
		*(ps++)=*(str++);
	*ps=0;
	if(!m.count(s0))return -1;
	return m.find(s0)->second;
}
int read_exp(const char *&str, const map<string,int> &m){
	space(str);
	int f = read_s(str, m), n;
	if(f <0)return -1;
	char ch = *space(str);
	if(ch!='^')return f;
	str++;
	n = read_exp(str, m);
	if(n<0)return -1;
	return power(f,n);
}
int read_mul(const char *&str, const map<string,int> &m){
	space(str);
	int f = read_exp(str, m), n;
	if(f <0)return -1;
	for(;;){
		char ch = *space(str);
		if(ch!='*'&&ch!='/'&&ch!='%')return f;
		str++;
		n = read_exp(str, m);
		if(n<0)return -1;
		switch(ch){
			case '*': f*=n; break;
			case '/': f/=n; break;
			case '%': f%=n; break;
		}
	}
	return f;
}
int read_int(const char *&str, const map<string,int> &m, char end){
	int f = read_mul(str, m), n;
	if(f <0)return -1;
	for(;;){
		char ch = *(str++);
		if(ch==end)break;
		space(str);
		n = read_mul(str, m);
		if(n<0)return -1;
		switch(ch){
			case '+': f+=n; break;
			case '-':f-=n; break;
			default: return -1;
		}
	}
	return f;
}
int read_int(const char *str, const map<string,int> &m){
	return read_int(str, m, 0);
}

bool file::read(const char *fmt, ...){
	map<string, int> m;
	va_list l;
	va_start(l, fmt);
	int d, i,sz; double lf;
	long long ld;
	intarr *ad; doublearr *af;
	const char *f0;
	char s[1000];
	bool ok=true;
	for(;ok && *fmt;fmt++){
		switch(*fmt){
			case ' ':continue;
			case 'f':
				if(fscanf(f, "%lf", &lf)!=1){ok=false; break;}
				*va_arg(l,double*)=lf;
				break;
			case 'd':
				if(fscanf(f, "%d", &d)!=1){ok=false; break;}
				if(fmt[1]=='>'){
					if(fmt[2]!='>')*va_arg(l,int*)=d;
					else fmt++;
					for(i=0;fmt[i+2]&&fmt[i+2]!=' '; i++)
						s[i]=fmt[i+2];
					s[i] = 0;
					if(!i)ok=false;
					else m[s] = d;
					fmt += i+2;
				}else *va_arg(l,int*)=d;
				break;
			case 'l':
				if(fscanf(f, "%lld", &ld)!=1){ok=false; break;}
				*va_arg(l,long long*)=ld;
				break;
			case 's':
				if(fscanf(f, "%s", va_arg(l,char*))!=1)ok=false;
				break;
			case 'a':
				f0 = fmt+2;
				if(fmt[2]!='['){
					if(fscanf(f, "%d", &sz)!=1||sz<0){ok=false; break;}
				}else{
					f0 = fmt+3;
					sz = read_int(f0, m, ']');
					if(sz<0){ok=false; break;}
				}
				if(fmt[1]=='d'){
					ad = va_arg(l,intarr*);
					intarr a(sz);
					for(i=0; i<sz; i++){
						if(fscanf(f, "%d", a.p+i)!=1){ok=false;break;}
					}
					if(ok)ad->swap(a);
				}
				else if (fmt[1] == 'l'){
					arr<long long> *al = va_arg(l, arr<long long>*), a(sz);
					for (i = 0; i<sz; i++){
						if (fscanf(f, "%lld", a.p + i) != 1){ ok = false; break; }
					}
					if (ok)al->swap(a);
				}
				else if (fmt[1] == 'f'){
					af = va_arg(l,doublearr*);
					doublearr a(sz);
					for(i=0; i<sz; i++){
						if(fscanf(f, "%lf", a.p+i)!=1){ok=false;break;}
					}
					if(ok)af->swap(a);
				}else if(fmt[1]=='s'){
					stringarr *as = va_arg(l,stringarr*);
					stringarr a(sz);
					for(i=0; i<sz; i++){
						if(fscanf(f, "%s", s)!=1){ok=false; break;}
						a.p[i] = s;
					}
					if(ok)as->swap(a);
				}else {ok = false; break;}
				fmt = f0-1;
				break;
			default: ok = false;
		}
	}
	va_end(l);
	return ok;
}

int cmp_double(const void *d1, const void *d2){
	if(*(double*)d1<*(double*)d2)return -1;
	if(*(double*)d1>*(double*)d2)return 1;
	return 0;
}
template<class T>
T gcd(T i, T j){
	while(j){
		T k = i%j;
		i=j; j=k;
	}
	return i;
}
/*
bool operator<(const set<pair<int, int> > &x, const set<pair<int, int> > &y){
	if (x.size() < y.size())return true;
	if (x.size() > y.size())return false;
	for (auto itx = x.begin(), ity = y.begin(); itx != x.end(); ++itx, ++ity){
		if (*itx < *ity)return true;
		if (*itx > *ity)return false;
	}
	return false;
}
*/
const ull M=1000000007;
int fact_mod(int n, int st=2){
	int x = 1;
	for (int i = st; i <= n; i++){
		x *= i;
		if (!(i &3))x %= M;
	}
	return x%M;
}
/*
map<int, int> &operator+=(map<int, int> &mp, const map<int, int> &m1){
	for (auto p : m1){
		if (mp.find(p.first) != mp.end())mp[p.first] += p.second;
		else mp[p.first] = p.second;
	}
	return mp;
}
map<int, int> &operator-=(map<int, int> &mp, const map<int, int> &m1){
	for (auto p : m1){
		if (mp.find(p.first) != mp.end())mp[p.first] -= p.second;
		else mp[p.first] = -p.second;
	}
	return mp;
}
*/
map<int, int> factors(int n){
	int n0 = (int)sqrt((double)n);
	map<int, int> res;
	for (int j = 2; j <= n0; j++){
		if (n%j)continue;
		int m = 0;
		while (!(n%j)){
			n /= j;
			m++;
		}
		res[j] = m;
	}
	if (n > 1)res[n] = 1;
	return res;
}
/*struct edge{
	int c1,c2,f1, f2;
	int h0;
	bool valid = false;
	void init(int C1, int C2, int F1, int F2, int H0){
		c1 = C1; c2 = C2; f1 = F1; f2 = F2;
		h0 = H0;
		valid = (c1 - f2 >= 50 && c2 - f1 >= 50);
	}
	double time(double t){
		if (!valid)return 1e+100;
		double h = h0 - 10 * t, w0 = max((h - (c2 - 50.))*0.1, 0.);
		t += w0; h -= 10 * w0;
		if (f1 + 20 > h) return t+10.;
		return t + 1;
	}
};
struct vert{
	double tm = 0.;
	int f,c;
	bool w1 = false, w2 = false;
	edge l,r,t,b;
	bool operator<(const vert &v2)const{ return tm < v2.tm; }
};
*/
struct int0{
	int x;
	int0(int i = 0){ x = i; }
	operator int()const{ return x; } 
	operator int&(){ return x; }
};

int solve(int n, string *s){
	long long res=1;
	int i, j;
	int c0set[256]; //mask 1 : exists beginning; 2: exists end; 7:exists middle
	int cset[256];
	int b[256], e[256], nv = n;
	vector<bool> v(n), sym(n);
	for (i = 0; i < n; i++)v[i] = true, sym[i]=false;
	map<int, string> m;
	memset(c0set, 0, sizeof(c0set));
	memset(cset, 0, sizeof(cset));
	for (i = 0; i < n; i++){
		int l = s[i].length();
		unsigned char st=s[i][0], end=s[i][l-1];
		for (j = 1; j < l; j++){
			if (s[i][j] != (char)st)break;
		}
		if (j < l){
			if (c0set[st] & 1)return 0;
			c0set[st] |= 1; b[st] = i;
			if (c0set[end] & 2)return 0;
			if ((c0set[st] & 2 || cset[st])){
				v[i] = false, nv--;
			}
			if (c0set[end] & 1 || cset[end]){
				v[i] = false;
				nv--;
			}
			c0set[end] |= 2; e[st] = i;
			for (l--; l>0 && s[i][l] == end;)l--;
			for (; j < l;){
				unsigned char c = s[i][j];
				if (c0set[c] || cset[c])return 0;
				c0set[c] = 7;
				for (j++; j < l; j++){
					if (s[i][j] != c)break;
				}
			}
		}
		else{
			sym[i] = true;
			if (cset[st]){ v[i] = false; nv--; }
			else{
				if ((c0set[st] & 1))v[i] = false, nv--;
				else if ((c0set[st] & 2))v[i] = false, nv--;
			}
			if (c0set[st] & 4)return 0;
//			if (cset[st])v[i] = false, nv--;
			cset[st]++; res = (res*cset[st]) % M;
		}
	}
	res = (res*fact_mod(nv)) % M;
	map<char, int> B;// , E;
	for (i = 0; i < n; i++){
		if (!sym[i])B[s[i][0]] = B[s[i][s[i].length()]] = i;
	}
	for (map<char, int>::const_iterator it = B.begin(), it0=it; it != B.end(); ++it){
		char c0 = it->first, c;
		int x = 0;
		for (it0=it;;x++){
			c = s[it0->second][s[it0->second].length() - 1];
			if (x>n || c == c0)return false;//there is a cycle
			if ((it0 = B.find(c)) == B.end())break;
		}
	}
	return (int)res;
}
bool valid(const char *s, set<char> &s0){
//	set<char> s0;
	for (; *s;){
		if (s0.find(*s) != s0.end())return false;
//		if (sc.find(*s) != sc.end())return 
		s0 << *s;
		char c = *s;
		while (*s == c)s++;
	}
	return true;
}
int solve1(int n, string *s){
	long long res = 1;
	int i, j;
	int c0set[256]; //mask 1 : exists beginning; 2: exists end; 7:exists middle
	int cset[256];
	int b[256], e[256], nv = n;
	vector<bool> v(n), sym(n);
	for (i = 0; i < n; i++)v[i] = true, sym[i] = false;
	map<int, string> m;
	set<char> s0, s1;
	memset(c0set, 0, sizeof(c0set));
	memset(cset, 0, sizeof(cset));
	for (i = 0; i < n; i++){
		char st = s[i][0]; int l = s[i].length();
		for (j = 0; j < l;j++)
		if (s[i][j] != st)break;
		if (j < l)continue;
		sym[i] = true;
		s0.insert(st);
		cset[(unsigned char)st]++;
		res = (res*cset[(unsigned char)st]) % M;
		for (j = i + 1; j < n; j++)swap(s[j - 1], s[j]);
		n--; i--;
	}
	s1 = s0;
	for (i = 0; i < n; i++){
		char st = s[i][s[i].length() - 1];
		s1.erase(s[i][0]);
		for (;;){
			st = s[i][s[i].length() - 1];
			s1.erase(st);
			for (j = 0; j < n; j++){
				if (s[j][0] == st)break;
			}
			if (j == n)break;
			if (j == i)return 0;
			s[i].append(s[j]);
			for (int k = j + 1; k < n; k++)
				swap(s[k - 1], s[k]);
			n--;
			if (j < i)i--;
		}
	}
	int ns = s1.size();
	for (i = 0; i < n; i++){
		if (!valid(s[i].c_str(),s1))return 0;
	}
	return int((res*fact_mod(ns + n)) % M);
}

int main(){
	file fin("input.txt","r"), fout("output.txt","w");
	if(!fin){printf("no input\n"); return 0;}
	int i, j, T=0, n, dwr=0, wr=0;
	if(!fin.read("d",&T))return 0;
	for(i=1; i<=T; i++){
		int a,b,k;
	//	intarr c,f;
		stringarr s;
		if (!fin.read("d>n as[n]", &n, &s)){
			printf("cannot read case #%d\n", i);
			break;
		}
		fprintf(fout.f, "case #%d: %d\n", i, solve1(n, s));
	}
//	system("pause");
	return 0;
}
