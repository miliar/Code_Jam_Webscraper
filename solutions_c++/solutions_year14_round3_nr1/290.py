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

template<class T>
struct graph{
	mutable int _used;
	void _inc()const{if(this)_used++;}
	void _dec()const{if(this && !--_used)delete this;}

	int e_count;
	typedef map<int, T*> ve_set;
	ve_set empty;
	typedef map<int,map<int, T> > e_map;
	typedef map<int,ve_set> pe_map;
	e_map out;
	pe_map in;
	class edge_iterator{
		e_map *m;
		typename e_map::iterator mit;
		typename map<int,T>::iterator mmit;
		friend struct graph<T>;
	public:
		edge_iterator(){m=0;}
		edge_iterator& to_start(){
			for(mit=m->begin(); mit!=m->end(); ++mit){
				if(!mit->second.empty()){
					mmit = mit->second.begin();
					break;
				}
			}
			return *this;
		}
		edge_iterator& to_next_vert(){
			while(mit!=m->end())
				if(!(++mit)->second.empty()){
					mmit = mit->second.begin();
					break;
				}
			return *this;
		}
		edge_iterator& to_prev_vert(){
			while(true){
				if(mit==m->begin()){
					mit=m->end(); break;
					mmit=map<int,T>::iterator();
				}
				if(!(--mit)->second.empty()){
					mmit = mit->second.begin();
					break;
				}
			}
			return *this;
		}
		edge_iterator& operator++(){
			++mmit;
			while(mit!=m->end() && mmit == mit->second.end()){
				++mit; mmit = mit->second.begin();
			}
			return *this;
		}
		edge_iterator& operator--(){
			while(mit!=m->begin() && mmit == mit->second.begin()){
				mmit = mit->second.end();
			}
			--mmit;
			return *this;
		}
		bool is_valid()const{return mit!=m->end();}
		int v1()const{return mit->first;}
		int v2()const{return mmit->first;}
		T& data(){return mmit->second;}
		T& operator*(){return mmit->second;}
		T* operator->(){return &mmit->second;}
	};
	graph(){
		e_count = 0;
		_used = 0;
	}
	edge_iterator edge_begin(){
		edge_iterator i; i.m = &this->out;
		return i.to_start();
	}
	graph(graph<T> &g):out(g.out){
		e_count = g.e_count;
		complete();
	}
	graph<T> &operator=(const graph<T>&g){
		out=g.out;
		e_count = g.e_count;
		complete();
	}
	T& operator()(int i, int j){
		sort_pair(i,j);
		uint x = out.size();
		bool add=false;
		map<int,T> & r1 = out[i];
		if(x < out.size())add = true;
		x = r1.size();
		T &r2 = r1[j];
		if(x<r1.size())add = true;
		if(add){in[j][i]=in[i][j]=&r2; e_count++;}
		return r2;
	}
	bool add_vertex(int i){
		uint x = in.size();
		in[i];
		return x<in.size();
	}
	bool remove_edge(int i, int j){
		sort_pair(i,j);
		typename e_map::iterator it = out.find(i);
		if(it==out.end())return false;
		bool e = (it->erase(j)>0);
		if(e){in[j].erase(i); e_count--;}
		return e;
	}
	int remove_vertex(int i){
		int x;
		typename e_map::iterator it = out.find(i);
		if(it==out.end())return 0;
		x = it->size();
		out.erase(it);
		typename pe_map::iterator ityy = in.find(i);
		if(ityy!=in.end()){
			ve_set &sy = ityy->second;
			for(typename pe_map::iterator ity = sy.begin(); ity!=sy.end() && ity->first<i; ++ity){
				out[ity->first].erase(i);
			}
			in.erase(ityy);
		}
		e_count-=x;
		return x;
	}
	void complete(){
		in.clear();
		for(typename e_map::iterator it = out.begin(); it!=out.end(); ++it){
			map<int,T> &mp = it->second;
			int i = it->first;
			ve_set &st = in[i];
			for(typename map<int,T>::iterator jt = mp.begin(); jt!=mp.end(); ++jt){
				in[jt->first][i] = st[jt->first]=&jt->second;
			}
		}
	}
	bool has_vertex(int i){
		return out.find(i)!=out.end();
	}
	const ve_set& edge_set(int i){
		typename pe_map::iterator it = in.find(i);
		if(it==in.end())return empty;
		return it->second;
	}
	const map<int,T>* edge_set_ptr(int i){
		typename pe_map::iterator it = out.find(i);
		if(it==out.end())return 0;
		return &it->second;
	}
	int vertex_set(set<int>& res)const{
		key_set(out, res);
		return res.size();
	}
	void rename_vert(const map<int,int>&n){
		for(typename e_map::iterator it = out.begin(); it!=out.end(); ++it){
			rename_keys(it->second, n);
		}
		rename_keys(out, n);
		complete();
	}
	void gr_union(graph<T>& g){
		for(graph<T>::edge_iterator it = g.edge_begin(); it.is_valid(); ++it)
			(*this)(it.v1(),it.v2()) = *it;
	}
	int vertex_count()const {return in.size();}
	int edge_count()const{return e_count;}
};

template<class T>
struct graph_ref{
	graph<T> *g;
	graph_ref(graph<T> *g0=0){(g=g0)->_inc();}
	graph_ref(const graph_ref<T>& gr){(g=gr.g)->_inc();}
	graph_ref<T>& operator=(const graph_ref<T>& gr){gr.g->_inc();g->_dec(); g=gr.r; return *this;}
	graph_ref<T>& operator=(graph<T>* gr){gr->_inc();g->_dec(); g=gr; return *this;}
	graph<T>* operator->(){return g;}
	graph<T>& operator*(){return *g;}
	graph_ref<T> copy(){return g ? new graph<T>(g) : 0;}
	bool operator!()const{return !g;}
	~graph_ref(){g->_dec();}
	graph_ref<T>& operator|=(const graph_ref<T>&gr){
		if(!gr)return *this;
		if(!g)return *this = gr.copy();
		g->gr_union(*gr.g);
		return *this;
	}
};
template<class T>
int connected_components(graph_ref<T> &g, vector<graph_ref<T> > &res){
	res.clear();
	if(!g||g->vertex_count())return 0;
	set<int> s, s0;
	stack<int> st;
	g->vertex_set(s);
	while(!s.empty()){
		s0.insert(*s.begin());
		st.push(*s.begin());
		while(!st.empty()){
			int i = st.top();
			st.pop();
		}
		s.erase(s.begin());

	}
}

template<class T>
graph_ref<T> subgraph(const graph_ref<T>& g, const set<int>& sv){
	if(!g)return 0;
	graph<T> *gg = new graph<T>;
	for(set<int>::const_iterator it = sv.begin(); it!=sv.end(); ++it){
		const map<int, T> *s = g->edge_set_ptr(*it);
		if(!s)continue;
		intersect(*s, sv,gg->out[*it]);
	}
	gg->complete();
	return gg;
}
template<class T>
graph_ref<T> complete_graph(int i, const T& def, int start=0){
	if(!i)return 0;
	graph<T> *g = new graph<T>;
	g->add_vertex(start);
	i+=start;
	for(int j=start+1; j<i; j++)
		for(int k=start; k<j; k++)
			(*g)(i,j)=def;
	return g;
}*/

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

int solve(ull p, ull q){
	int i, j, k;
	ull d = gcd(p, q);
	p /= d; q /= d;
	for (k = 0, d = q; d > 1; d >>= 1, k++){
		if (d & 1)return -1;
	}
	for (; p > 1; p >>= 1)
		k--;
	return k;
}

int main(){
	file fin("input.txt","r"), fout("output.txt","w");
	if(!fin){printf("no input\n"); return 0;}
	int i, j, T=0, n, dwr=0, wr=0;
	if(!fin.read("d",&T))return 0;
	for(i=1; i<=T; i++){
		ull p,q;
		stringarr f;
		if (!fin.read("l / l", &p, &q)){
			printf("cannot read case #%d\n", i);
			break;
		}
		int r = solve(p, q);
		if (r>=0)fprintf(fout.f, "case #%d: %d\n", i, r);
		else fprintf(fout.f, "case #%d: impossible\n", i);
	}
//	system("pause");
	return 0;
}
