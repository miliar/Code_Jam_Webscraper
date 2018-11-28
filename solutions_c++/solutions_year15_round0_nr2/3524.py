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
  vector<int> pocet;
  
  scanf("%d",&t);
  
  for(l=1;l<=t;l++){
    scanf("%d",&n);
    
    //printf("Number of diners: %d\n",n);
    
    m=0;
    
    pocet.resize(1001);
    for(i=0;i<1001;i++){
      pocet[i]=0;
    }
    
    for(i=0;i<n;i++){
      scanf("%d",&k);
      pocet[k]++;
      if(k>m){
        m=k;
      }
      //printf("%d\n",k);
    }
    
    //printf("Max number of pancakes: %d\n",k);
    
    s=1042;
    
    for(i=1;i<=m;i++){
      r=i;
      for(j=1;j<=m;j++){
        if(pocet[j]>0){
          r+=pocet[j]*(j/i-1);
          if(j%i > 0){
            r+=pocet[j];
          }
        }
      }
      //printf("Max pancakes: %d total time %d\n",i,r);
      if(r<s){
        s=r;
      }
    }
    
    printf("Case #%d: %d\n",l,s);
  }
  
  return 0;
}
