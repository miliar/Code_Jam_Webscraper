#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <cstring>
#include <assert.h>
#include <sys/time.h>
#include <fstream>

#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define rep(i,n)  FOR(i,0,n)
#define REP(i,n)  FOR(i,0,n)
#define each(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define exist(s,e) ((s).find(e)!=(s).end())

#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" << __LINE__ << ")" << " " << __FILE__ << endl;
#define deb(x) cerr << #x << " = " << (x) << " , ";
#define debl cerr << " (L" << __LINE__ << ")"<< endl;


#define clr(a) memset((a),0,sizeof(a))
#define nclr(a) memset((a),-1,sizeof(a))
#define pb push_back
#define INRANGE(x,s,e) ((s)<=(x) && (x)<(e))
#define MP(x,y) make_pair((x),(y))

double pi=3.14159265358979323846;

using namespace std;
static const double EPS = 1e-5;
//typedef long long ll;
typedef int ll;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<string> vs;

template<typename T> std::ostream& operator<<(std::ostream& os, const vector<T>& z){
	os << "[ ";
	REP(i,z.size())os << z[i] << ", " ;
	return ( os << "]" << endl);
}

template<typename T> std::ostream& operator<<(std::ostream& os, const set<T>& z){
	os << "set( ";
	EACH(p,z)os << (*p) << ", " ;
	return ( os << ")" << endl);
}

template<typename T,typename U> std::ostream& operator<<(std::ostream& os, const map<T,U>& z){
	os << "{ ";
	EACH(p,z)os << (p->first) << ": " << (p->second) << ", " ;
	return ( os << "}" << endl);
}

template<typename T,typename U> std::ostream& operator<<(std::ostream& os, const pair<T,U>& z){
	return ( os << "(" << z.first << ", " << z.second << ",)" );
}

double get_time(){
	struct timeval tv;
	gettimeofday(&tv, NULL);
	return tv.tv_sec + tv.tv_usec*1e-6;
}

typedef unsigned int uint32_t;
struct RND{
	uint32_t x;
	uint32_t y;
	uint32_t z;
	uint32_t w;
	RND(){
		x=123456789;
		y=362436069;
		z=521288629;
		w=88675123;
	}
	void init(int seed){
		x=123456789;
		y=362436069;
		z=521288629;
		w=seed+100;
		REP(i,10)get();
	}
	uint32_t get(){
		uint32_t t;
		t=x^(x<<11);
		x=y;y=z;z=w;
		w=(w^(w>>19))^(t^(t>>8));
		return w;
	}
};
RND rnd;

ll N,M,K;

vvi kouho;

void gen(vi a){
    if(a.size()==N){
        kouho.pb(a);
        return;
    }
    else{
        int st=(a.size()==0 ? 2 : a[a.size()-1]);
        FOR(k,st,M+1){
            vi a2=a;
            a2.pb(k);
            gen(a2);
        }
    }
}

vl weight;

vector<map<ll,int> > cnts;

void pre(){
    gen(vi());
    
    cnts.resize(kouho.size());
    weight.resize(kouho.size());
    
    rep(jj,kouho.size()){
        map<ll,int> cnt;
        vi seq = kouho[jj];
        rep(qq,(1<<seq.size())){
            ll v=1;
            rep(j,seq.size()){
                if((qq>>j)%2==1)v*=seq[j];
            }
            cnt[v]+=1;
        }
        cnts[jj] = cnt;
        
        ll w=1;
        ll p=0;
        rep(kk,seq.size()){
            if(kk>=1 && seq[kk]==seq[kk-1])p++;
            else p=1;
            
            w*=p;
        }
        weight[jj]=w;
    }
}

vi test_seq;

void _main(istream &inp){
	int T;
	inp >> T >>ws;
    double start=get_time();
	REP(tt,T){
		cout << "Case #" << tt+1 << ":" << endl;
        ll R;
        inp >> R >> N >> M >> K;
        deb(R);deb(N);deb(M);deb(K);debl;
        
        pre();
        debug(kouho.size());
        
        int test_ok_num=0;
        
        rep(j,R){
            if(j%100==0){
                debug(j);
                debug(test_ok_num);
                debug(get_time()-start);
            }
            vl vs;
            if(1){
                rep(t,K){
                    ll v;
                    inp >> v;
                    vs.pb(v);
                }
            }
            else{
                vi seq;
                rep(tt,N){
                    int h=2+rnd.get()%(M+1-2);
                    seq.pb(h);
                }
                rep(t,K){
                    ll v=1;
                    rep(i,seq.size()) if(rnd.get()%2==0) v*=seq[i];
                    vs.pb(v);
                }
                test_seq=seq;
            }
            
            double best=0.0, best_ind=0;

            rep(jj,kouho.size()){
                double sc=1.0;
                rep(ii,vs.size()){
                    ll v=vs[ii];
                    double uu=0.0;
                    if(exist(cnts[jj],v)){
                        uu += cnts[jj][v];
                    }
                    sc *= uu;
                }
                
                sc /= weight[jj];
                
                if(sc>best){
                    best = sc;
                    best_ind=jj;
                }
            }
            
            //debug(best);
            
            vi seq=kouho[best_ind];
            
            //debug(weight[best_ind]);
            //debug(vs);
            
            sort(test_seq.begin(), test_seq.end());
            
            if(seq==test_seq) test_ok_num++;
            
            //debug(seq);debug(test_seq);
            
            rep(tt,seq.size()){
                cout << seq[tt] << (tt==seq.size()-1 ? "\n" : "");
            }
        }
        debug(R);debug(test_ok_num);
	}
    debug(get_time()-start);
    
}

int main(){
	if(0){
		ifstream ifs("test.txt");
		_main(ifs);
	}
	else{
		_main(cin);
	}
	return 0;
}