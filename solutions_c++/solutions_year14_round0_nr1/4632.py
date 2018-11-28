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
int main(){
  int T; scanf("%d",&T);
  for(int t = 0; t < T; t++){
    int ord1[4][4],ord2[4][4];
    int row1 = 0,row2 = 0;
    scanf("%d",&row1);
    rep(y,4) rep(x,4) cin>>ord1[y][x];
    scanf("%d",&row2);
    rep(y,4) rep(x,4) cin>>ord2[y][x];
    int res = 0;
    int num = 0;
    rep(x1,4){
      bool exist = false;
      rep(x2,4){
	if(ord1[row1 - 1][x1] == ord2[row2 - 1][x2]){
	  exist = true;
	  num = ord1[row1 - 1][x1];
	  break;
	}
      }
      if(exist) res++;
    }
    printf("Case #%d: ",t + 1);
    if(res == 1) printf("%d\n",num);
    if(res > 1) printf("Bad magician!\n");
    if(res <= 0) printf("Volunteer cheated!\n");
  }
}
