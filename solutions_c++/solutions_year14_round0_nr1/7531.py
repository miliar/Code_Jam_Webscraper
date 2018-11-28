#include<iostream>
#include<stack>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstdio>
#include<string>
#include<cstring>
#include<cmath>
#include<complex>
#include<sstream>
#include<map>
#include<set>
#define DEBUG(x) cout<<"line"<<__LINE__<<":"<<#x" == "<<x<<endl
#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define ALL(x) (x).begin(),(x).end()
#define INF 1000000
#define isValid(x,y,p,q) (x>=0 && x<p &&y>=0 && y<q)

using namespace std;

inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}
typedef long long ll;
typedef pair<int,int> P;

int dx[]={-1,0,1,0};
int dy[]={0,-1,0,1};
  
///////////////////////////////////////////////////////////////
int t1[4][4];
int t2[4][4];
int a=0,b=0;

int main(){
  int n;
  cin >>n;
  REP(num,n){
    cin >>a;
    REP(i,4){
      REP(j,4){
        cin>>t1[i][j];
      }
    }
    cin>>b;
    REP(i,4){
      REP(j,4){
        cin>>t2[i][j];
      }
    }

    int counter = 0;
    int ans = 0;
    REP(i,4){
      
      REP(j,4){
        if (t1[a-1][i] == t2[b-1][j]){
          ans = t1[a-1][i];
          counter++;
        }
      }
      
    }
    if(counter == 0){
      cout<<"Case #"<<num+1<<": "<<"Volunteer cheated!"<<endl;
    }
    else if(counter == 1){
      cout<<"Case #"<<num+1<<": "<<ans<<endl;
    }
    else if(counter >1){
      cout<<"Case #"<<num+1<<": "<<"Bad magician!"<<endl;
    }
  }
  return 0;
  
}

