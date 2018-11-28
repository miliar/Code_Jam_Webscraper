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

int ar[12];
int main(){
  int t;
  scanf("%d",&t);
  for(int i=1;i<=t;i++){
    int r,c,w,ans=0,pans=0;
    scanf("%d %d %d",&r,&c,&w);

    for(int j=w;j<c;j+=w){
      pans=j/w;
      pans+=w;
      ans=max(ans,pans);
    }
    if(c%w==0){
      pans=0;
      pans+=c/w+w-1;
    }
    ans=max(ans,pans);
    printf("Case #%d: %d\n",i,ans);
  }
  return 0;
}
