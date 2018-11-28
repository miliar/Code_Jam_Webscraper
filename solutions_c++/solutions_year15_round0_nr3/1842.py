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

char str[10005];
int l;
void multiply(int& ans, char& sans, int j){
  if(sans=='i'){
    if(str[j]=='i'){
      sans='1';
      ans*=-1;
    }else if(str[j]=='j'){
      sans='k';
    }else if(str[j]=='k'){
      sans='j';
      ans*=-1;
    }
  }else if(sans=='j'){
    if(str[j]=='i'){
      sans='k';
      ans*=-1;
    }else if(str[j]=='j'){
      sans='1';
      ans*=-1;
    }else if(str[j]=='k'){
      sans='i';
    }
  }else if(sans=='1'){
    sans=str[j];
  }else if(sans=='k'){
    if(str[j]=='i'){
      sans='j';
    }else if(str[j]=='j'){
      sans='i';
      ans*=-1;
    }else if(str[j]=='k'){
      sans='1';
      ans*=-1;
    }
  }

}

int main(){
  int t,t1;

  scanf("%d",&t);
  t1=t;
  while(t--){
    int x,f=1,p=1,d=1;
    int ans=1;
    char sans='1';
    scanf("%d %d",&l,&x);
    scanf("%s",str);
    int i,j;
    if(x>16){
      x=x%16+16;
    }
    for(i=0;i<x;i++){

      for(int j=0;j<l;j++){
    //    debug(ans);
    //    debug(sans);
        multiply(ans,sans,j);
    //    debug(ans);
    //    debug(sans);
        if(ans==1 && sans=='i' && p==1){
          ans=1;sans='1';p=0;
        }
        if(ans==1 && sans=='j' && d==1 && p==0){
          ans=1;sans='1';d=0;
        }
    //    debug(ans);
    //    debug(sans);
      }
    }
    if(ans==1 && sans=='k' && d==0){
      printf("Case #%d: YES\n",t1-t);
    }else{
      printf("Case #%d: NO\n",t1-t);
    }
  }
  return 0;
}
