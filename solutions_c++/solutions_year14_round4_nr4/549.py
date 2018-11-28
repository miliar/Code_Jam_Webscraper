//using standard c++0x
//compile with gc 4.8.1: g++ -O2 -std=c++0x
//or Visual Studio Exress 2013
#define _CRT_SECURE_NO_WARNINGS
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
#include <iostream>

typedef unsigned long uint;
typedef unsigned long long ull;
using namespace std;

template<class T, class Cmp>
set<T,Cmp> &operator<<(set<T,Cmp> &s, const T&x){
	s.insert(x); return s;
}

void sort_pair(int &x, int &y){if(x>y){int t=x;x=y;y=t;}}

/*template<class T, class K>
void intersect(const map<T, K> &x, const set<T> &y, set<T> &res){
	res.clear();
	auto ix = x.begin(), ixx = ix;
	auto iy = y.begin(), iyy = y.end();
	for(;ix!=x.end();){
		iy = iyy = y.upper_bound(ix->first);
		if(*(--iy)==ix->first)res.insert(ix->first);
		if(iy==y.end())break;
		ixx = ix = x.upper_bound(*iy);
		if(*(--ixx)==*iy)res.insert(*iy);
	}
}
template<class T, class K, class K1>
void intersect(const map<T, K> &x, const map<T,K1> &y, map<T, K> &res){
	res.clear();
	typename map<T,K>::const_iterator ix = x.begin(),ixx;
	typename map<T,K1>::const_iterator iy, iyy;
	for(;ix!=x.end();){
		iy = iyy = y.upper_bound(ix->first);
		if((--iyy)->first==ix->first)res[ix->first] = ix->second;
		if(iy==y.end())break;
		ixx = ix = x.upper_bound(iy->first);
		if((--ixx)->first==iy->first)res[ixx->first]=ixx->second;
	}
}

template<class T, class K>
void key_set(const map<T,K> &m, set<T> &s){
	s.clear();
	for(auto p : m)
		s.insert(p.first);
}

template<class T, class K>
K& map_val(map<T,K> &m, const T& k, K&def){
	typename map<T,K>::iterator it = m.find(k);
	return it==m.end() ? def : it->second;
}
template<class T, class K>
const K& map_val(const map<T,K> &m, const T& k, const K&def){
	auto it = m.find(k);
	return it==m.end() ? def : it->second;
}
template<class T>
bool rename_keys(map<int,T> &m, const map<int,int> &n){
	map<int,int> s;
	intersect(n,m,s);
	map<int,T> t;
	for(const pair<int,int> &p : s){
		int k = p.first;
		auto itm = m.find(k);
		t[p.second]=itm->second;
		m.erase(itm);
//		if(s[map_val(n, it->first, it->first)]);
	}
	for(auto p : s){
		m[p.first].swap(p.second);
	}
	return true;
}

*/
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
	template <class T>
	file& print_arr(const T *x, int n, const char *fmt, const char *end = "\n"){
		for (int i = 0; i < n; i++){
			fprintf(f, fmt, x[i]);
		}
		fprintf(f, "%s", end);
		return *this;
	}
	template<class T>
	file& print_arr(const T *x, int n, int m, const char *fmt){
		for (int i = 0; i < n; i++){
			for (int j = 0; j < m; j++)
				fprintf(f, fmt, x[i*m+j]);
			fprintf(f, "\n");
		}
		return *this;
	}
	file& print(int *x, int n,const char *end = "\n"){
		return print_arr(x, n, "%d ", end);
	}
	file& print(long long *x, int n, const char *end = "\n"){
		return print_arr(x, n, "%lld ", end);
	}
	file& print(double *x, int n, const char *end = "\n"){
		return print_arr(x, n, "%lf ", end);
	}
	file& print(int *x, int n, int m){
		return print_arr(x, n, m, "%d ");
	}
	file& print(long long *x, int n, int m){
		return print_arr(x, n, m, "%lld ");
	}
	file& print(double *x, int n, int m){
		return print_arr(x, n, m, "%lf ");
	}
	file& print(string *x, int n, bool newline = true){
		for (int i = 0; i < n; i++)
			fprintf(f, "%s%c", x[i].c_str(), newline ? '\n' : ' ');
		if (!newline)fprintf(f, "\n");
		return *this;
	}
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
			default: if(fgetc(f)!=*fmt) ok = false;
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

template<class K, class V, class Cmp>
ostream& operator<<(ostream &s, const map<K, V, Cmp> & m){
	s << "{";
	for (typename map<K, V, Cmp>::const_iterator it = m.begin(); it != m.end(); ++it){
		if (it != m.begin())s << ", ";
		s << "(" << it->first << ", " << it->second << ")";
	}
	s << "}";
	return s;
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
/*const int M=9901;
int fact_mod(int n, int st=2){
	int x = 1;
	for (int i = st; i <= n; i++){
		x *= i;
		if (!(i &3))x %= M;
	}
	return x%M;
}*/
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
/*
struct edge{
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

int com_pr(string *s1, string *s2){
	int i;
	for (i = 0; i < (int)s1->length(); i++){
		if ((*s1)[i] != (*s2)[i])break;
	}
	return i;
}
int com_prefs(int n, string **s){
	int res = 0, mx;
	for (int i = 0; i < n; i++){
		mx = 0;
		for (int j = 0; j < i; j++)
			mx = max(mx, com_pr(s[i], s[j])+1);
		res += s[i]->length() + 1 - mx;
	}
	return res;
}

pair<int,int> solve(int n, int m, string *s){
	int i, res = 0, k, j;
	int b = 0, e = n-1;
	int c = 1;
	for (i = 0; i < m; i++)
		c *= n;
	string* cl[4][8];
	int mx = 0;
	for (i = 0; i < c; i++){
		int p[4] = { 0, 0, 0, 0 };
		for (j = 0, k = i; j < m; j++){
			b = k%n;
			cl[b][p[b]++] = s + j;
			k /= n;
		}
		for (k = 0, j = 0; j < n; j++){
			k += com_prefs(p[j], cl[j]);
		}
		if (k>mx){ mx = k; res = 1; }
		else if(k == mx)res++;
	}
	return make_pair(mx, res);
}

int main(){
	file fin("input.txt","r"), fout("output.txt","w");
	if(!fin){printf("no input\n"); return 0;}
	int i, T=0;
	if(!fin.read("d",&T))return 0;
	for(i=1; i<=T; i++){
		uint n, m;
		stringarr s;
		if (!fin.read("d>m d as[m]", &m, &n, &s)){
			printf("cannot read case #%d\n", i);
			break;
		}
		fprintf(fout.f, "case #%d: %d %d\n", i, solve(n, m, s));
	}
	return 0;
}
