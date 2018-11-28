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


char str[1010];
int main(){
  int t,t1;
  scanf("%d",&t);
  t1=t;
  while(t--){
    int s,ans=0,count=0;
    scanf("%d",&s);
    scanf("%s",str);
    count=str[0]-'0';
    for(int i=1;i<=s;i++){
      if(count<i){
        ans+=i-count;
        count+=i-count;
      }
      count+=str[i]-'0';
    }
    printf("Case #%d: %d\n",t1-t,ans);
  }

  return 0;
}
