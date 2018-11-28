#define _CRT_SECURE_NO_WARNINGS
#include<algorithm>
#include<iostream>
#include<numeric>
#include<complex>
#include<sstream>
#include<cstdio>
#include<string>
#include<vector>
#include<cmath>
#include<queue>
#include<list>
#include<set>
#include<map>
using namespace std;

//===============================SHORTENINGS====================================
typedef long long int64;
typedef pair<int,int> PII;
//#define X first
//#define Y second
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;
//#define VAR(a,b) __typeof(b) a=(b)
#define VAR(a,b) auto a=(b)
template<typename T> T inline sqr(T q){return q*q;}
#define sz(X) ((int)(X).size())
#define pb push_back
#define ALL(c) (c).begin(),(c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) (c).resize(unique(ALL(c))-(c).begin())
//===============================CONSTANTS======================================
const int INF=1000000001;
const int64 INF64=sqr((int64)INF);
const double EPS=1E-14;
//=================================LOOPS========================================
#define FOR(I,S,N) for(int I=(S);I<(N);I++)
#define REP(I,N) FOR(I,0,N)
#define FORD(I,S,N) for(int I=(S);I>=(N);I--)
#define FORV(i,v) FOR(i,0,sz(v))
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
//===============================STRINGS========================================
typedef stringstream SS;
template<typename T> string tos(T q,int w=0)
{ SS A;A.precision(w);A<<fixed<<q; return A.str();}
template<typename T> T sto(string s){SS A(s);T t;A>>t;return t;}
template<typename T> vector<T> s2v(string s,string d=" "){
    FORV(i,s)FORV(j,d)if(s[i]==d[j])s[i]=' ';
    int n=sz(s);while(n&&s[n-1]==' ')n--;
    s.resize(n);SS A(s);vector<T> ans;
    for(T t;A>>t;)ans.pb(t);
    return ans;
}
//================================DEBUG=========================================
template<typename T1,typename T2>ostream &operator<<(ostream &out,const 
pair<T1,T2> &t ){out << "( " <<  t.X << " , " << t.Y << " )";return out;}
template<typename T>ostream &operator<<(ostream &out,const vector<T> &t){
out<<"{ ";FORV(i,t){if(i)out<<", ";out<<t[i];}out<<" }";return out;}
#define PR(X) cout<<#X<<" = "<<(X)<<" "
#define PRL cout<<endl
//================================TIME==========================================
double Clock() {
	unsigned long long time;
#ifdef _MSC_VER
	time = __rdtsc();
#else
    __asm__ volatile ("rdtsc" : "=A" (time));
#endif
    return time / 2.5e9; 
}
//================================MAIN==========================================

typedef double cfloat;

struct Solver{
	int N;
	cfloat VX, X;
	vector<cfloat> R, C;

	cfloat res;

	Solver() {
	}

	void read(){
		cin >> N >> VX >> X;
		R.resize(N);
		C.resize(N);
		REP(i, N)
			cin >> R[i] >> C[i];
	}

	cfloat calcT(cfloat v0, cfloat t0, cfloat v1, cfloat t1){
		return (t0 * v0 + t1 * v1) / (v0 + v1);
	}

	bool ok(cfloat T){
		vector<cfloat> V(N);
		FORV(i, V)
			V[i] = R[i] * T;

		cfloat lowV = 0, lowT = 0;
		cfloat highV = 0, highT = 0;
		
		cfloat dstV = VX;

		REP(i, N){
			if( C[i] == X ){
				dstV = max(dstV - V[i], (cfloat)0);
				continue;
			}

			if( C[i] < X ){
				lowT = calcT(lowV, lowT, V[i], C[i]);
				lowV += V[i];
			}else{
				highT = calcT(highV, highT, V[i], C[i]);
				highV += V[i];
			}
		}

		if( lowV + highV < dstV )
			return false;

		if( dstV < EPS )
			return true;

		cfloat lowVused = min(dstV, lowV);
		cfloat lowVleft = dstV - lowVused;
		cfloat minT = calcT(lowVused, lowT, lowVleft, highT);

		cfloat highVused = min(dstV, highV);
		cfloat highVleft = dstV - highVused;
		cfloat maxT = calcT(highVused, highT, highVleft, lowT);

		return (minT <= X) && (X <= maxT);
	}

	void work(){
		if( *min_element(ALL(C)) > X + EPS || *max_element(ALL(C)) < X - EPS ){
			res = -1;
			return;
		}

		cfloat L = 0;
		cfloat R = 1E20;

		REP(k, 1000){
			k++;
			cfloat x = (L+R) / 2;
			if( ok(x) )
				R = x;
			else
				L = x;
		}

		res = R;

		//cerr << ok(res) << endl;
	}

	void write(){
		cout << fixed;
		cout.precision(9);

		if( res == -1 )
			cout << "IMPOSSIBLE" << endl;
		else
			cout << res << endl;
	}
};

int main(){
//freopen("input.txt" ,"r",stdin );
//freopen("B-small-attempt0.in" ,"r",stdin );
//freopen("B-small-attempt1.in" ,"r",stdin );
freopen("B-small-attempt2.in" ,"r",stdin );
//freopen("B-large.in" ,"r",stdin );
freopen("output.txt","w",stdout);
#ifdef _DEBUG
	cerr << "Running in DEBUG!!!" << endl;
#endif
    int T;
    cin>>T;

	vector<Solver> solvers(T);
    
	REP(tc, T)
		solvers[tc].read();

//#pragma omp parallel for schedule(dynamic,1)
	REP(tc, T)
		solvers[tc].work();

    REP(tc, T){
        cout<<"Case #"<<tc+1<<": ";
		solvers[tc].write();
    }

    return 0;
}
