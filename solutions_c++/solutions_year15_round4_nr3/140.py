#define DEB

#include<bits/stdc++.h>
#include<unistd.h>
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

const int INF=5e8;

int n;
int m;
map<string,int> conv;
int getid(string s){
  if(conv.count(s)) return conv[s];
  int id=conv.size();
  conv[s]=id;
  return id;
}

int mask[4005];
vector<int> sente[205];
int main(){
  int t;cin>>t;

  REP(setn,t){
    printf("Case #%d: ",setn+1);
    cin>>n;
    conv.clear();
    cin.ignore();cin.ignore();
    REP(i,n){
      sente[i].clear();
      string line;getline(cin,line);
      stringstream ss;ss<<line;
      string word;
      while(ss>>word){
        sente[i].pb(getid(word));
      }
    }
    m=conv.size();

    int res=INF;
    REP(bit,1<<n){//0:English 1: French
      if((bit&1) || !(bit>>1&1)) continue;
      CLR(mask);
      REP(j,n) {
        for(auto e:sente[j]) mask[e]|=(bit>>j&1)+1;
      }



      int cnt=0;
      REP(j,m) cnt+=(mask[j]==3);
      chmin(res,cnt);
    }
    printf("%d\n",res);
  }

  return 0;

}



