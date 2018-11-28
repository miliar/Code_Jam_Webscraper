#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> ii;
#define X first
#define Y second
#define REP(i,a) for(int i=0;i<a;++i)
#define REPP(i,a,b) for(int i=a;i<b;++i)
#define FILL(a,x) memset(a,x,sizeof(a))
#define	foreach( gg,itit )	for( typeof(gg.begin()) itit=gg.begin();itit!=gg.end();itit++ )
#define	mp make_pair
#define	pb push_back
#define sz(a) int((a).size())
#define	debug(ccc)	cout << #ccc << " = " << ccc << endl;
#define present(c,x) ((c).find(x) != (c).end())
const int mod = 1e9+7;

int ar[1010][1010],ar1[1001];

int main(){
  int t,t1;
  scanf("%d",&t);
  t1=t;
  for(int i=0;i<1001;i++){
    for(int j=1;j<1001;j++){
      if(j<=i) {
        ar[i][j]=0;
        continue;
      }
      ar[i][j]=1000000;
      for(int k=1;k<j/2+1;k++){
        ar[i][j]=min(ar[i][j],ar[i][j-k]+ar[i][k]+1);
      }
    }
  }
  while(t--){
    int d,ans=100000,pans,maxI;
    scanf("%d",&d);
    for(int i=0;i<d;i++){
      scanf("%d",&ar1[i]);
      maxI=max(maxI,ar1[i]);
    }
    for(int x=1;x<=maxI;x++){
      pans=x;
      for(int i=0;i<d;i++){
        pans+=ar[x][ar1[i]];
      }
      ans=min(pans,ans);
    }
    printf("Case #%d: %d\n",t1-t,ans);
  }
  return 0;
}
