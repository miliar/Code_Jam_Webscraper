#include<iostream>
#include<cstdio>
#include<vector>
#include<set>
#include<string>
#include<utility>
#include<map>
#include<cmath>
#include<queue>
#include<stack>
#include<cstring>
#include<algorithm>
#include<sstream>
#define ll long long
#define VI vector<int>
#define REPN(i,x,y) for(int i=x;i<y;i++)
#define REP(i,y) REPN(i,0,y)
#define REPR(i,y,x) for(int i=y;i>=x;i--)
#define CLR(A,x) memset(A,x,sizeof(A))
#define INF (1<<30)
#define eps (1e-9)
#define ALL(v) (v).begin(),(v).end()
#define RALL(v) (v).rbegin(),(v).rend()
#define pb push_back
#define mp make_pair
#define sqr(x) (x)*(x)
#define dbg(x) cout << #x << " = " << x << endl
#define dbg2(x,y)cout<<#x<<"="<<x<<" "<<#y<<"="<<y<<endl
#define S(x)scanf("%d\n",&x)
#define S2(x,y)scanf("%d %d\n",&x,&y)
#define SC(x)scanf("%d",&x)
#define P(x)printf("%d\n",x);
#define f first
#define s second
#define MAXN 100005
using namespace std;
int A[4][4];
int main(){
  int nc;S(nc);
  int fc,sc;
  int cases=0;
  while(nc--){
    S(fc);
    REP(i,4){
      REP(j,4){
	SC(A[i][j]);
      }
    }
    map<int,int> mapa;
    map<int,int>::iterator it;
    REP(i,4){
      mapa[A[fc-1][i]]++;
    }
    S(sc);
    REP(i,4){
      REP(j,4){
	SC(A[i][j]);
      }
    }
    REP(i,4){
      mapa[A[sc-1][i]]++;
    }
    int cont=0;
    int id;
    for(it=mapa.begin();it!=mapa.end();it++) {
      //      dbg2((*it).f,(*it).s);
      if((*it).s == 2){
	cont++;
	id=(*it).f;
      }
    }
    if(cont==1) {
      printf("Case #%d: %d\n",++cases,id);
    } else if(cont==0) {
      printf("Case #%d: Volunteer cheated!\n",++cases);
    } else {
      printf("Case #%d: Bad magician!\n",++cases);      
    }
  }

  return 0;	
}
