#pragma warning (disable: 4530) 
#include<map>
#include<set>
#include<list>
#include<cmath>
#include<queue>
#include<stack>
#include<cstdio>
#include<string>
#include<vector>
#include<complex>
#include<cstdlib>
#include<cstring>
#include<numeric>
#include<sstream>
#include<iostream>
#include<algorithm>
#include<functional>
#include<climits>


#define mp       make_pair
#define pb       push_back
#define all(x)   (x).begin(),(x).end()
#define rep(i,n) for(int i=0;i<(n);i++)
 
using namespace std;
 
typedef    long long          ll;
typedef    unsigned long long ull;
typedef    vector<bool>       vb;
typedef    vector<int>        vi;

typedef    vector<vb>         vvb;
typedef    vector<vi>         vvi;
typedef    pair<int,int>      pii;
 
const int INF=1<<29;
const double EPS=1e-9;
 
const int dx[]={1,0,-1,0},dy[]={0,-1,0,1};//right down left up
int N;
int main(){
  int T; scanf("%d",&T);
  for(int t = 0; t < T; t++){
    cin>>N;
    vector<bool> NaomiF(N,false);
    vector<bool> KenF(N,false);
    deque<double> Naomi,Ken;
    rep(i,N){
      double k; cin>>k;
      Naomi.push_back(k);
    }
    rep(i,N){
      double k; cin>>k;
      Ken.push_back(k);
    }
    sort(all(Naomi));
    sort(all(Ken));
    int War = 0,DWar = 0;
    for(int n = 0; n < Naomi.size(); n++){
      double KenWin = -1;
      for(int k = 0; k < Ken.size(); k++){
	if(!KenF[k] && Ken[k] > Naomi[n]){
	  KenWin = Ken[k];
	  KenF[k] = true;
	  break;
	}
      }
      if(KenWin == -1){
	for(int k = 0; k < Ken.size(); k++){
	  if(!KenF[k]){
	    KenF[k] = true;
	    War++;
	    break;
	  }
	}
      }
    }
    rep(i,KenF.size()) KenF[i] = false,NaomiF[i] = false;

    for(int k = Ken.size() - 1; k >= 0; k--){
      double NaomiWin = -1;
      for(int n = 0; n < Naomi.size(); n++){
	if(!NaomiF[n] && Naomi[n] > Ken[k]){
	  NaomiWin = Naomi[n];
	  NaomiF[n] = true;
	  DWar++;
	  break;
	}	
      }
      if(NaomiWin == -1){
	for(int n = 0; n < Naomi.size(); n++){
	  if(!NaomiF[n]){
	    NaomiF[n] = true;
	    break;
	  }
	}	
      }
    }
    // rep(i,Naomi.size()) cout<<Naomi[i]<<" ";
    // cout<<endl;
    // rep(i,Ken.size()) cout<<Ken[i]<<" ";
    // cout<<endl;
    
    printf("Case #%d: %d %d\n",t + 1,DWar,War);
  }
  return 0;
}
