//
//  main.cpp
//  QualQE
//
//  Created by Bigmac on 2014/4/11.
//  Copyright (c) 2014年 Google CodeJam. All rights reserved.
//
#include <iostream>
#include <string>
#include <cstdio>
#include <cstring>
#include <vector>
#include <map>
#include <set>
#include <cassert>
#include <string>
#include <algorithm>
#include <queue>
using namespace std;
FILE *fi = NULL;
FILE *fo = NULL;
#define out(x) {cerr << #x"=" << x << endl;}
#define out_stop(x) {cerr << #x"=" << x << endl; cin.ignore(1); exit(1);}
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FOREACH(i,c) for(decltype(c.begin()) i=(c).begin();i!=(c).end();++i)
#define REP(i,n) FOR(i,0,n)

typedef long long ll;

#define MAX(a,b) (((a)>(b))?(a):(b))
#define MIN(a,b) (((a)<(b))?(a):(b))
/*
 //BEGINTEMPLATE_BY_ACRUSH_TOPCODER
 #define SIZE(X) ((int)(X.size()))//NOTES:SIZE(
 #define LENGTH(X) ((int)(X.length()))//NOTES:LENGTH(
 #define MP(X,Y) make_pair(X,Y)//NOTES:MP(
 typedef long long int64;//NOTES:int64
 typedef unsigned long long uint64;//NOTES:uint64
 #define two(X) (1<<(X))//NOTES:two(
 #define twoL(X) (((int64)(1))<<(X))//NOTES:twoL(
 #define contain(S,X) (((S)&two(X))!=0)//NOTES:contain(
 #define containL(S,X) (((S)&twoL(X))!=0)//NOTES:containL(
 const double pi=acos(-1.0);//NOTES:pi
 const double eps=1e-11;//NOTES:eps
 template<class T> inline void checkmin(T &a,T b){if(b<a) a=b;}//NOTES:checkmin(
 template<class T> inline void checkmax(T &a,T b){if(b>a) a=b;}//NOTES:checkmax(
 template<class T> inline T sqr(T x){return x*x;}//NOTES:sqr
 typedef pair<int,int> ipair;//NOTES:ipair
 template<class T> inline T lowbit(T n){return (n^(n-1))&n;}//NOTES:lowbit(
 template<class T> inline int countbit(T n){return (n==0)?0:(1+countbit(n&(n-1)));}//NOTES:countbit(
 //Numberic Functions
 template<class T> inline T gcd(T a,T b)//NOTES:gcd(
 {if(a<0)return gcd(-a,b);if(b<0)return gcd(a,-b);return (b==0)?a:gcd(b,a%b);}
 template<class T> inline T lcm(T a,T b)//NOTES:lcm(
 {if(a<0)return lcm(-a,b);if(b<0)return lcm(a,-b);return a*(b/gcd(a,b));}
 template<class T> inline T euclide(T a,T b,T &x,T &y)//NOTES:euclide(
 {if(a<0){T d=euclide(-a,b,x,y);x=-x;return d;}
 if(b<0){T d=euclide(a,-b,x,y);y=-y;return d;}
 if(b==0){x=1;y=0;return a;}else{T d=euclide(b,a%b,x,y);T t=x;x=y;y=t-(a/b)*y;return d;}}
 template<class T> inline vector<pair<T,int> > factorize(T n)//NOTES:factorize(
 {vector<pair<T,int> > R;for (T i=2;n>1;){if (n%i==0){int C=0;for (;n%i==0;C++,n/=i);R.push_back(make_pair(i,C));}
 i++;if (i>n/i) i=n;}if (n>1) R.push_back(make_pair(n,1));return R;}
 template<class T> inline bool isPrimeNumber(T n)//NOTES:isPrimeNumber(
 {if(n<=1)return false;for (T i=2;i*i<=n;i++) if (n%i==0) return false;return true;}
 template<class T> inline T eularFunction(T n)//NOTES:eularFunction(
 {vector<pair<T,int> > R=factorize(n);T r=n;for (int i=0;i<R.size();i++)r=r/R[i].first*(R[i].first-1);return r;}
 //Matrix Operations
 const int MaxMatrixSize=40;//NOTES:MaxMatrixSize
 template<class T> inline void showMatrix(int n,T A[MaxMatrixSize][MaxMatrixSize])//NOTES:showMatrix(
 {for (int i=0;i<n;i++){for (int j=0;j<n;j++)cout<<A[i][j];cout<<endl;}}
 template<class T> inline T checkMod(T n,T m) {return (n%m+m)%m;}//NOTES:checkMod(
 template<class T> inline void identityMatrix(int n,T A[MaxMatrixSize][MaxMatrixSize])//NOTES:identityMatrix(
 {for (int i=0;i<n;i++) for (int j=0;j<n;j++) A[i][j]=(i==j)?1:0;}
 template<class T> inline void addMatrix(int n,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//NOTES:addMatrix(
 {for (int i=0;i<n;i++) for (int j=0;j<n;j++) C[i][j]=A[i][j]+B[i][j];}
 template<class T> inline void subMatrix(int n,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//NOTES:subMatrix(
 {for (int i=0;i<n;i++) for (int j=0;j<n;j++) C[i][j]=A[i][j]-B[i][j];}
 template<class T> inline void mulMatrix(int n,T C[MaxMatrixSize][MaxMatrixSize],T _A[MaxMatrixSize][MaxMatrixSize],T _B[MaxMatrixSize][MaxMatrixSize])//NOTES:mulMatrix(
 { T A[MaxMatrixSize][MaxMatrixSize],B[MaxMatrixSize][MaxMatrixSize];
 for (int i=0;i<n;i++) for (int j=0;j<n;j++) A[i][j]=_A[i][j],B[i][j]=_B[i][j],C[i][j]=0;
 for (int i=0;i<n;i++) for (int j=0;j<n;j++) for (int k=0;k<n;k++) C[i][j]+=A[i][k]*B[k][j];}
 template<class T> inline void addModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//NOTES:addModMatrix(
 {for (int i=0;i<n;i++) for (int j=0;j<n;j++) C[i][j]=checkMod(A[i][j]+B[i][j],m);}
 template<class T> inline void subModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T A[MaxMatrixSize][MaxMatrixSize],T B[MaxMatrixSize][MaxMatrixSize])//NOTES:subModMatrix(
 {for (int i=0;i<n;i++) for (int j=0;j<n;j++) C[i][j]=checkMod(A[i][j]-B[i][j],m);}
 template<class T> inline T multiplyMod(T a,T b,T m) {return (T)((((int64)(a)*(int64)(b)%(int64)(m))+(int64)(m))%(int64)(m));}//NOTES:multiplyMod(
 template<class T> inline void mulModMatrix(int n,T m,T C[MaxMatrixSize][MaxMatrixSize],T _A[MaxMatrixSize][MaxMatrixSize],T _B[MaxMatrixSize][MaxMatrixSize])//NOTES:mulModMatrix(
 { T A[MaxMatrixSize][MaxMatrixSize],B[MaxMatrixSize][MaxMatrixSize];
 for (int i=0;i<n;i++) for (int j=0;j<n;j++) A[i][j]=_A[i][j],B[i][j]=_B[i][j],C[i][j]=0;
 for (int i=0;i<n;i++) for (int j=0;j<n;j++) for (int k=0;k<n;k++) C[i][j]=(C[i][j]+multiplyMod(A[i][k],B[k][j],m))%m;}
 template<class T> inline T powerMod(T p,int e,T m)//NOTES:powerMod(
 {if(e==0)return 1%m;else if(e%2==0){T t=powerMod(p,e/2,m);return multiplyMod(t,t,m);}else return multiplyMod(powerMod(p,e-1,m),p,m);}
 //Point&Line
 double dist(double x1,double y1,double x2,double y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}//NOTES:dist(
 double distR(double x1,double y1,double x2,double y2){return sqr(x1-x2)+sqr(y1-y2);}//NOTES:distR(
 template<class T> T cross(T x0,T y0,T x1,T y1,T x2,T y2){return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);}//NOTES:cross(
 int crossOper(double x0,double y0,double x1,double y1,double x2,double y2)//NOTES:crossOper(
 {double t=(x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);if (fabs(t)<=eps) return 0;return (t<0)?-1:1;}
 bool isIntersect(double x1,double y1,double x2,double y2,double x3,double y3,double x4,double y4)//NOTES:isIntersect(
 {return crossOper(x1,y1,x2,y2,x3,y3)*crossOper(x1,y1,x2,y2,x4,y4)<0 && crossOper(x3,y3,x4,y4,x1,y1)*crossOper(x3,y3,x4,y4,x2,y2)<0;}
 bool isMiddle(double s,double m,double t){return fabs(s-m)<=eps || fabs(t-m)<=eps || (s<m)!=(t<m);}//NOTES:isMiddle(
 //Translator
 bool isUpperCase(char c){return c>='A' && c<='Z';}//NOTES:isUpperCase(
 bool isLowerCase(char c){return c>='a' && c<='z';}//NOTES:isLowerCase(
 bool isLetter(char c){return c>='A' && c<='Z' || c>='a' && c<='z';}//NOTES:isLetter(
 bool isDigit(char c){return c>='0' && c<='9';}//NOTES:isDigit(
 char toLowerCase(char c){return (isUpperCase(c))?(c+32):c;}//NOTES:toLowerCase(
 char toUpperCase(char c){return (isLowerCase(c))?(c-32):c;}//NOTES:toUpperCase(
 template<class T> string toString(T n){ostringstream ost;ost<<n;ost.flush();return ost.str();}//NOTES:toString(
 int toInt(string s){int r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt(
 int64 toInt64(string s){int64 r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toInt64(
 double toDouble(string s){double r=0;istringstream sin(s);sin>>r;return r;}//NOTES:toDouble(
 template<class T> void stoa(string s,int &n,T A[]){n=0;istringstream sin(s);for(T v;sin>>v;A[n++]=v);}//NOTES:stoa(
 template<class T> void atos(int n,T A[],string &s){ostringstream sout;for(int i=0;i<n;i++){if(i>0)sout<<' ';sout<<A[i];}s=sout.str();}//NOTES:atos(
 template<class T> void atov(int n,T A[],vector<T> &vi){vi.clear();for (int i=0;i<n;i++) vi.push_back(A[i]);}//NOTES:atov(
 template<class T> void vtoa(vector<T> vi,int &n,T A[]){n=vi.size();for (int i=0;i<n;i++)A[i]=vi[i];}//NOTES:vtoa(
 template<class T> void stov(string s,vector<T> &vi){vi.clear();istringstream sin(s);for(T v;sin>>v;vi.push_bakc(v));}//NOTES:stov(
 template<class T> void vtos(vector<T> vi,string &s){ostringstream sout;for (int i=0;i<vi.size();i++){if(i>0)sout<<' ';sout<<vi[i];}s=sout.str();}//NOTES:vtos(
 //Fraction
 template<class T> struct Fraction{T a,b;Fraction(T a=0,T b=1);string toString();};//NOTES:Fraction
 template<class T> Fraction<T>::Fraction(T a,T b){T d=gcd(a,b);a/=d;b/=d;if (b<0) a=-a,b=-b;this->a=a;this->b=b;}
 template<class T> string Fraction<T>::toString(){ostringstream sout;sout<<a<<"/"<<b;return sout.str();}
 template<class T> Fraction<T> operator+(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b+q.a*p.b,p.b*q.b);}
 template<class T> Fraction<T> operator-(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b-q.a*p.b,p.b*q.b);}
 template<class T> Fraction<T> operator*(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.a,p.b*q.b);}
 template<class T> Fraction<T> operator/(Fraction<T> p,Fraction<T> q){return Fraction<T>(p.a*q.b,p.b*q.a);}
 //ENDTEMPLATE_BY_ACRUSH_TOPCODER
 */

void openIOFile(int argc, char **argv)
{
	const char *filename_in = "A.in";
	if(argc > 1)
	{
		filename_in = argv[1];
	}
	string filename_out(filename_in);
	filename_out.append("_out");
	fi = fopen(filename_in, "rt");
	if(fi == NULL)
	{
		out_stop("cannot open input.");
	}
	fo = fopen(filename_out.c_str(), "wt");
	if(fo == NULL)
	{
		out_stop("cannot open output.");
	}
}
void closeIOFile()
{
	fclose(fi);
	fclose(fo);
}
int readInt()
{
	int in_v;
	if(fscanf(fi, "%d", &in_v) != 1){out_stop("Failed Reading Input");}
	return in_v;
}
long long readHugeInt()
{
	long long in_v;
	if(fscanf(fi, "%lld", &in_v) != 1){out_stop("Failed Reading Input");}
	return in_v;
}
double readDouble()
{
	double in_v;
	if(fscanf(fi, "%lf", &in_v) != 1){out_stop("Failed Reading Input");}
	return in_v;
}
char readChar()
{
    char in_v = 0x00;
    while(in_v == ' ' || in_v == 0x0d || in_v == 0x0a || in_v == 0x00)
    {
        if(fscanf(fi, "%c", &in_v) != 1){out_stop("Failed Reading Input");}
        if(in_v != ' ' && in_v != 0x0d && in_v != 0x0a && in_v != 0x00)
        {
            return in_v;
        }
    }
    return in_v;
}
set<string> readStrings()
{
    char in_v[20000];
    in_v[0] = 0x00;
    while(in_v[0] == ' ' || in_v[0] == 0x0d || in_v[0] == 0x0a || in_v[0] == 0x00)
    {
        if(fgets(in_v, 20000, fi) <=0){out_stop("Failed Reading Input");}
        set<string> ret;
        if(in_v[0] != ' ' && in_v[0] != 0x0d && in_v[0] != 0x0a && in_v[0] != 0x00)
        {
            char * val = strtok(in_v, " \x0d\x0a\x00");
            do
            {
                if(ret.find(val) == ret.end())
                {
                    ret.insert(val);
                }
                val = strtok(NULL, " \x0d\x0a\x00");
            }while(val!=NULL);
            return ret;
        }
    }
    return set<string>();
}
//2014 Qual QE
int main(int argc, char **argv)
{
	openIOFile(argc,argv);
	int in_t = readInt();
	for(int it_t = 1; it_t <= in_t; it_t++)
	{
		//init input
		//finish init input
        map<string, set<int> > w_map;
        vector< set<string> > in_text;
        
		long long in_n = readHugeInt();
        set<string> in;
        in_text.resize(in_n);
        for(int it_i = 0; it_i < in_n; it_i++)
        {
            in = readStrings();
            in_text[it_i] = in;
            for(auto it_a = in.begin(); it_a != in.end(); it_a++)
            {
                string w = (*it_a);
                set<int> &s = w_map[w];
                if(s.find(it_i) == s.end())
                {
                    s.insert(it_i);
                }
            }
        }
        struct edge {int to, cap;size_t rev;};
        vector<edge> G[2000];
        int level[2000];
        int iter[2000];
        printf("\n");
        auto add_edge = [&](int from, int to, int cap){
            printf("(%d,%d) = %d\n", from, to, cap);
            G[from].push_back((edge){to, cap, G[to].size()});
            G[to].push_back((edge){from, 0, G[from].size() - 1});
        };
        auto bfs = [&](int s){
            memset(level, -1, sizeof(level));
            queue<int> que;
            level[s] = 0;
            que.push(s);
            while(!que.empty())
            {
                int v = que.front(); que.pop();
                for(int i = 0; i < G[v].size(); i++)
                {
                    edge &e = G[v][i];
                    if(e.cap > 0 && level[e.to] < 0) {
                        level[e.to] = level[v] + 1;
                        que.push(e.to);
                    }
                }
            }
        };
        std::function<int(int,int,int)> dfs;
        dfs = [&](int v, int t, int f)-> int{
            if(v==t) return f;
            for(int &i = iter[v]; i < G[v].size(); i++) {
                edge &e = G[v][i];
                if(e.cap > 0 && level[v] < level[e.to])
                {
                    int d = dfs(e.to, t, min(f, e.cap));
                    if(d > 0) {
                        e.cap -= d;
                        G[e.to][e.rev].cap += d;
                        return d;
                    }
                }
            }
            return 0;
        };
        auto max_flow = [&](int s, int t) -> int {
            int flow = 0;
            for(;;) {
                bfs(s);
                if(level[t] < 0) return flow;
                memset(iter, 0, sizeof(iter));
                int f;
                while((f = dfs(s,t,INT_MAX)) > 0) {
                    flow += f;
                }
            }
            return flow;
        };
        auto compute_cost = [&](int s, int t) -> void {
            int ret = 0;
            for(auto it_a = in_text[s].begin();it_a != in_text[s].end();it_a++)
            {
                auto ii = w_map[*it_a].find(s);
                auto jj = w_map[*it_a].find(t);
                if(jj == w_map[*it_a].end())
                {
                    continue;
                }
                auto iii = ii;
                iii++;
                if(iii == w_map[*it_a].end())
                {
                    iii = w_map[*it_a].begin();
                }
                if(jj == iii)
                {
                    ret++;
                    if(s == 0 && t == 2)
                    {
                        printf("ret++\n");
                    }
                    continue;
                }
            }
            if(ret > 0)
            {
                add_edge(s+2, t+2, ret);
            }
        };
        //===========================================solve function begin================================//
        add_edge(0,2, INT_MAX);
        add_edge(3,1, INT_MAX);
        vector< set<int> > ad;
        ad.resize(in_text.size());
        for(int tt = 0; tt < in_text.size(); tt++)
        {
            for(auto it_a = in_text[tt].begin();it_a != in_text[tt].end();it_a++)
            {
                for(auto it_b = w_map[*it_a].begin(); it_b != w_map[*it_a].end(); it_b++)
                {
                    if(ad[tt].find(*it_b) == ad[tt].end())
                    {
                        ad[tt].insert(*it_b);
                        compute_cost(tt, *it_b);
                    }
                }
            }
        }
        printf("\n");
        
        //===========================================solve function  end ================================//
        fprintf(fo, "Case #%d: %lld", it_t, max_flow(0,1) );
		fprintf(fo, "\n");
	}
	closeIOFile();
}