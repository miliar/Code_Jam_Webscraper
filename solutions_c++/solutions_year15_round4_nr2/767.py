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

int main(){
  int t;
  scanf("%d",&t);
  for(int i=0;i<t;i++){
    int n;
    double v,x;
    scanf("%d %lf %lf",&n,&v,&x);
    if(n==1){
      double r1,c1;
      scanf("%lf %lf",&r1,&c1);
      if(c1>x-1e-12 && c1<x+1e-12){
        printf("Case #%d: %.12lf\n",i+1,v/r1);continue;
      }else{
        printf("Case #%d: IMPOSSIBLE\n",i+1);continue;
      }
    }else if(n==2){
      double r1,r2,c1,c2;
      scanf("%lf %lf",&r1,&c1);
      scanf("%lf %lf",&r2,&c2);
      if((c1<x && c2<x)|| (c1>x && c2>x)){
        printf("Case #%d: IMPOSSIBLE\n",i+1);continue;
      }else{
        if( c1>c2-1e-12 && c1<c2+1e-12 && c1>x-1e-12 && c1<x+1e-12){
          double ans=v/(r1+r2);
          //if(ans>v/c2)  ans=v/c2;

          printf("Case #%d: %.12lf\n",i+1,ans);continue;
        }
        double a1=v*(x-c1)/(r2*(c2-c1)),a2=v*(x-c2)/(r1*(c1-c2));
      //  printf("%lf %lf\n",)
        if(a1<a2) a1=a2;
        printf("Case #%d: %.12lf\n",i+1,a1);continue;
      }
    }
  }
  return 0;
}
