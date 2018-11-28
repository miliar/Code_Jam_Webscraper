#include<iostream>
#include<complex>
#include<vector>
#include<string>

#include<cstdio>
#include<cctype>
#include<cstring>
#include<cstdlib>
#include<cmath>

#include<sstream>
#include<unistd.h>
#include<valarray>
#include<numeric>
#include<algorithm>
#include<list>
#include<deque>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<bitset>
#include<utility>

#include<fstream>
#include<time.h>
#include<pthread.h>
using namespace std;

#define NDEBUG
#include<assert.h>
#define SZ(X) ((int)X.size())
#define CLR(X) memset(X,0,sizeof(X))
#define MAX(A,B) (((A)>(B))?(A):(B))
#define MIN(A,B) (((A)<(B))?(A):(B))
#define MOD(A,B) (((A)%(B)+(B))%(B))
#define MP make_pair
#define FI first
#define SE second
#define FOR(I,A,B) for(int I=(A);I<=(B);I++)
#define FORD(I,A,B) for(int I=(A);I>=(B);I--)
#define REP(I,N) for(int I=0;I<(N);I++)
#define VAR(V,init) __typeof(init) V=(init)
#define FOREACH(I,C) for(VAR(I,(C).begin());I!=(C).end();I++)
#define RFOREACH(I,C) for(VAR(I,(C).rbegin());I!=(C).rend();I++)
#define ALL(X) (X).begin(),(X).end()
#define SRT(X) sort((X).begin(),(X).end())
#define PB push_back

const int threads_num=8;
const int min_test_num=1;
const int max_test_num=1000000;


inline void err_sys(const char *msg){fflush(stdout);perror(msg);fflush(NULL);}
inline void Pthread_mutex_lock(pthread_mutex_t *mptr){int n;if((n=pthread_mutex_lock(mptr))==0)return;errno=n;err_sys("pthread_mutex_lock error");exit(1);}
inline void Pthread_mutex_unlock(pthread_mutex_t *mptr){int n;if((n=pthread_mutex_unlock(mptr))==0)return;errno=n;err_sys("pthread_mutex_unlock error");exit(1);}
inline void Pthread_setconcurrency(int lev){int n;if((n=pthread_setconcurrency(lev))==0)return;errno=n;err_sys("pthread_setconcurrency error");exit(1);}
inline void Pthread_create(pthread_t *tid, void *(*func)(void*), void *arg){int n;if((n=pthread_create(tid,NULL,func,arg))==0)return;errno=n;err_sys("pthread_create error");exit(1);}
inline void Pthread_join(pthread_t tid){int n;if((n=pthread_join(tid,NULL))==0)return;errno=n;err_sys("pthread_join error");exit(1);}

class CasesManager{
  private:
    int T,tt_to_process;
    pthread_mutex_t mutex;
  public:
    CasesManager(int _T=0){
      T=_T;
      tt_to_process=1;
      mutex=PTHREAD_MUTEX_INITIALIZER;
    }
    
    bool getNextCase(int &tt){
      Pthread_mutex_lock(&mutex);
      tt=tt_to_process;
      bool ret=true;
      if(tt_to_process>T){
        Pthread_mutex_unlock(&mutex);
        ret=false;
      }else{
        tt_to_process++;
      }
      return ret;
    }
    
    void haveNextCase(){Pthread_mutex_unlock(&mutex);}
} casesManager;

class ResultsManager{
  private:
    int T;
    vector<string> resv;
    pthread_mutex_t mutex;
  public:
    ResultsManager(int _T=0){
      T=_T;
      resv.resize(T,"");
      mutex=PTHREAD_MUTEX_INITIALIZER;
    }

    void setResult(int tt, string res){
      Pthread_mutex_lock(&mutex);
      resv[tt-1]=res;
      Pthread_mutex_unlock(&mutex);
    }

    string getResults(){
      Pthread_mutex_lock(&mutex);
      string ret="";
      REP(i,T) ret+=resv[i];
      Pthread_mutex_unlock(&mutex);
      return ret;
    }
} resultsManager;

pthread_t threads[threads_num];

typedef vector<int> VI;
typedef set<int> SETI;
inline VI parsei(string s,char ch=' '){string a="";VI wyn;REP(i,(int)s.size()) if(s[i]!=ch) a+=s[i];else if(!a.empty()){wyn.PB(atoi(a.c_str()));a="";} if(!a.empty()) wyn.PB(atoi(a.c_str()));return wyn;}
const int INF=0x7f7f7f7f;
template<class T> inline string stringify(T x,int p=9){ostringstream o;o.precision(p);o<<x;o.flush();return o.str();}
template<class T> inline void wypisz(const T& x){FOREACH(I,x)cout<<*I<<" ";cout<<endl;}

void adds(SETI &x, int y){
  SETI nx;
  FOREACH(I, x){
    nx.insert(*I +y);
  }
  x.insert(nx.begin(),nx.end());
  x.insert(y);
}

inline bool ex(SETI &s, int x){
  return s.find(x)!=s.end();
}

#define DEB 0

int check(SETI &h, SETI &d, int V){
  if(DEB) cout<<"d ";
  if(DEB) wypisz(h);
  if(DEB) cout<<"d2 ";
  if(DEB) wypisz(d);
  int mn=0;
  FOR(i, 1, V){
    if(h.find(i)==h.end()){
      mn=i; break;
    }
  }
  int ret=INF;
  if(mn==0){
    ret=0;
  }else{
    SETI nh=h;
    SETI nd=d;
    if(!ex(d,mn)){
      adds(nh,mn);
      nd.insert(mn);
      ret=check(nh, nd, V)+1;
    }
    FOREACH(I,h){
      int a=mn-(*I);
      if(a<=0) break;
      if(!ex(d,a)){
        nh=h;
        nd=d;
        adds(nh,a);
        nd.insert(a);
        int pom=check(nh,nd,V)+1;
        ret=MIN(ret,pom);
      }
    }
  }
  if(DEB) cout<<"r "<<mn<<" "<<ret<<endl;
  return ret;
}


int main(){
  int T;
  cin>>T;
  string line;
  getline(cin, line);
  T=MIN(T,max_test_num);

  int C, D, V;
  VI den;
  SETI ds;
  SETI h;
  
  FOR(tt, 1, T){
        cin>>C>>D>>V;
        den.clear();
        ds.clear();
        h.clear();
    getline(cin, line);
    getline(cin, line);
    den=parsei(line);
    REP(i,SZ(den)) ds.insert(den[i]);
    FOREACH(I,ds) adds(h,*I);
    
        string ret_str="";
    // fill in
    int ret=check(h, ds, V);
    ret_str="Case #"+stringify(tt)+": "+stringify(ret)+"\n";
    cout<< ret_str;
  }
  return 0;
}
