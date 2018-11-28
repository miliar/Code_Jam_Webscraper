#include <cstdio>
#include <vector>
#include <algorithm>
#define mp(a,b) make_pair((a),(b))
#define ff first
#define ss second

using namespace std;

int main(){
  int i,j,k,l,m,n,p,t;
  vector<int> A,used;
  
  scanf("%d",&t);
  
  for(l=1;l<=t;l++){
    scanf("%d",&n);
    scanf("%d",&m);
    
    A.resize(n);
    
    for(i=0;i<n;i++){
      scanf("%d",&p);
      A[i]=p;
    }
    
    sort(A.begin(),A.end());
    reverse(A.begin(),A.end());
    used.resize(n,0);
    
    for(i=0;i<n;i++){
      used[i]=0;
    }
    
    k=0;
    
    j=0;
    
    for(i=0;i<n;i++){
      if(used[i]==1){
	continue;
      }
      used[i]=1;
      k++;
      for(j=0;j<n;j++){
	if(used[j]==0 && ((A[i]+A[j])<=m) ){
	  used[j]=1;
	  break;
	}
      }
    }
    
    printf("Case #%d: %d\n",l,k);
    
  }
  
  return 0;
}