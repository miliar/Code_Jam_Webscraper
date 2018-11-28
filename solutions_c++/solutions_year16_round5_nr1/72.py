#define DEB
#include<bits/stdc++.h>
#define REP(i,m) for(int i=0;i<(m);++i)
#define REPN(i,m,in) for(int i=(in);i<(m);++i)
#define ALL(t) (t).begin(),(t).end()
#define CLR(a) memset((a),0,sizeof(a))
#define pb push_back
#define mp make_pair
#define fr first
#define sc second

using namespace std;


#ifdef DEB
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
#else
#define dump(x) ;
#define prl ;
template<class T> void debug(T a,T b){ ;}
#endif

template<class T> void chmin(T& a,const T& b) { if(a>b) a=b; }
template<class T> void chmax(T& a,const T& b) { if(a<b) a=b; }

typedef long long int lint;
typedef pair<int,int> pi;

namespace std{
  template<class S,class T>
  ostream &operator <<(ostream& out,const pair<S,T>& a){
    out<<'('<<a.fr<<','<<a.sc<<')';
    return out;
  }
}

//const int INF=5e8;
int n;
char s[20005];

char tmp[20005];
bool doit(){
  int m=0;
  REP(i,n){
    if(i+1<n && s[i]==s[i+1]){
      ++i;
    }else{
      tmp[m++]=s[i];
    }
  }
  if(n==m) return false;
  REP(i,m) s[i]=tmp[i];
  s[m]='\0';
  n=m;
  return true;
}
int main(){
  int T;
  cin>>T;
  for(int setn=1;setn<=T;++setn){
    scanf("%s",s);
    n=strlen(s);
    dump(n);
    int res=10*n/2;

    while(doit()) ;

    res-=n/2*5;
    printf("Case #%d: ",setn);
    cout<<res<<endl;
    dump(setn);
  }
  return 0;
}



