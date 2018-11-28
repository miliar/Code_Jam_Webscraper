// Ideone_Language_Id:1
/* Don't remove the first line! */
#include <bits/stdc++.h>
/*more #includes. Don't write "using namespace std" here*/

#ifdef __WIN32__
#define getchar_unlocked getchar
#endif
//Input-output macros
#define s(n) scan(&n)
#define sf(n) scanf("%f",&n)
#define sc(n) scanf("%c",&n)
#define ss(n) scanf("%s",n)
// Useful constants
#define INF (int)1e9
#define MOD 1000000007
#define EPS 1e-9
// Useful hardware instructions
#define bitcount __builtin_popcount
#define lz __builtin_clz
#define tz __builtin_ctz
#define gcd __gcd
// Useful container manipulation / traversal macros
#define forall(i,a,b) for(int i=a;i<b;i++)
#define forrev(i,a,b) for(int i=a;i>b;i--)
#define foreach(v,c) for(typeof((c).begin()) v=(c).begin();v!=(c).end();++v)
#define all(a) a.begin(),a.end()
#define in(a,b) ((b).find(a)!=(b).end())
#define pb push_back
#define fill(a,v) memset(a,v,sizeof a)
#define sz(a) ((int)(a.size()))
#define mp make_pair
#define checkbit(n,b) ((n>>b)&1)
#define DREP(a) sort(all(a));a.erase(unique(all(a)),a.end())
#define INDEX(arr,ind) (lower_bound(all(arr),ind)-arr.begin())
#define re return
#define runtime() ((double)clock() / CLOCKS_PER_SEC)
using namespace std;
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef pair<int,int > ii;
typedef vector<ii > vii;
typedef vector<string> vs;
typedef vector<vi > vvi;
typedef istringstream iss;
typedef ostringstream oss;

/*Faster input functions*/
void scan(int* i){int t=0;char c;bool negative=false;c=getchar_unlocked();while(c<'0'||c>'9'){if(c=='-')negative=true;c=getchar_unlocked();}while(c>='0'&&c<='9'){t=(t<<3)+(t<<1)+c-'0';c=getchar_unlocked();}if(negative)t=~(t-1);*i=t;}
void scan(long long int* i){long long int t=0;char c;bool negative=false;c=getchar_unlocked();while(c<'0'||c>'9'){if(c=='-')negative=true;c=getchar_unlocked();}while(c>='0'&&c<='9'){t=(t<<3)+(t<<1)+c-'0';c=getchar_unlocked();}if(negative)t=~(t-1);*i=t;}
/*debug functions*/
#ifdef DEBUG
  #define debug(args...) {dbg,args;std::cout<<std::endl;}
#else
  #define debug(args...) // Just strip off all debug tokens
#endif
struct debugger{template<typename T> debugger& operator ,(const T& v){std::cout<<v<<" ";return *this;}}dbg;
template <typename T1,typename T2> inline std::ostream& operator<<(std::ostream& os,const std::pair<T1,T2>& p){return os<<"("<<p.first<<", "<<p.second<<")";}
template<typename T>inline std::ostream&operator<<(std::ostream& os,const std::vector<T>& v){std::string delim="[";for(unsigned int i=0;i < v.size();i++){os<<delim<<v[i];delim=", ";}return os<<"]";}
template<typename T>inline std::ostream&operator<<(std::ostream& os,const std::set<T>& v){std::string delim="[";for (typename std::set<T>::const_iterator ii=v.begin();ii!=v.end();++ii){os<<delim<<*ii;delim=", ";}return os<<"]";}
template<typename T1,typename T2>inline std::ostream&operator<<(std::ostream& os,const std::map<T1,T2>& v){std::string delim="[";for (typename std::map<T1,T2>::const_iterator ii=v.begin();ii!=v.end();++ii){os<<delim<<*ii;delim=", ";}return os<<"]";}

int toInt(string a){int i; iss(a)>>i; return i;}
string toString(int a){oss ss;ss<<a;return ss.str();}

/*structs and typedefs*/

int T;/*number of test cases*/
/*integers to be scanned every loop*/
/*more global variables*/

/*functions*/
const int MAX = 30;

  long long dp[MAX+1][2][2][2];
  vi da,db,dc;
  vi digits(int A){
    vi d(MAX,0);
    forall(i,0,MAX){
      d[i] = ((A&(1<<i))!=0);
    }
    return d;
  }
  long long f(int t, int eqx,int eqy, int eqz){
    long long &ret = dp[t][eqx][eqy][eqz];
    if(ret==-1){
      ret = 0;
      if(t==0){
        ret = 1;
      }
      else{
        forall(x,0,2)forall(y,0,2){
          int z = x&y;
          if(t!=1){
            if((!eqx||x<=da[t-1])&&(!eqy||y<=db[t-1])&&(!eqz||z<=dc[t-1])){
              ret+=f(t-1,eqx && x==da[t-1],eqy && y==db[t-1],eqz && z==dc[t-1]);
            }
          }
          else{
            if((!eqx||x<da[t-1])&&(!eqy||y<db[t-1])&&(!eqz||z<dc[t-1])){
              ret+=f(t-1,eqx && x==da[t-1],eqy && y==db[t-1],eqz && z==dc[t-1]);
            }
          }
        }
      }
    }
    return ret;
  }
  long long getNumber(int A, int B, int C){

    memset(dp,-1,sizeof(dp));
    da = digits(A);
    db = digits(B);
    dc = digits(C);
    return f(30,1,1,1);


  }


int main(int argc, char const *argv[])
{
  /* code */
  s(T);
  int a,b,c;
  forall(t,0,T){
    s(a);s(b);s(c);
    cout<<"Case #"<<t+1<<": "<<getNumber(a,b,c)<<"\n";
  }

  return 0;
}
