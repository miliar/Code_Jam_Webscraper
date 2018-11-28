#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#define mp(a,b) make_pair((a),(b))
#define ff first
#define ss second

using namespace std;

int main(){
  int i,j,k,l,m,n,o,p,r,s,t;
  char c;
  
  scanf("%d",&n);
  
  for(i=0;i<n;i++){
    scanf("%d",&k);
    m=0;
    r=0;
    
    //printf("%d\n",k);
    
    c=getchar();
    while(!(c>='0' && c<='9')){
      c=getchar();
    }
    
    for(j=0;j<=k;j++){
      //printf("%c %d ",c,(int)((int)c-(int)'0'));
      if(m<j){
        r+=(j-m);
        m=j;
      }
      m+=(int)(c-'0');
      //printf("%d\n",r);
      c=getchar();
    }
    
    //printf("\n");
    
    printf("Case #%d: %d\n",i+1,r);
  }
  
  return 0;
}
