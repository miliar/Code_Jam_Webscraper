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
  vector<int> can, is;
  
  scanf("%d",&t);
  
  for(l=0;l<t;l++){
    can.clear();
    is.clear();
    scanf("%d",&n);
    for(i=0;i<4;i++){
      for(j=0;j<4;j++){
	scanf("%d",&p);
	if(i==n-1){
	  can.push_back(p);
	}
      }
    }
    
    scanf("%d",&n);
    for(i=0;i<4;i++){
      for(j=0;j<4;j++){
	scanf("%d",&p);
	if(i==n-1){
	  can.push_back(p);
	}
      }
    }
    
    for(i=0;i<4;i++){
      for(j=4;j<8;j++){
	if(can[i]==can[j]){
	  is.push_back(can[i]);
	}
      }
    }
    
    /*for(i=0;i<can.size();i++){
      printf("%d ",can[i]);
    }putchar('\n');*/
    
    if(is.size()==0){
      printf("Case #%d: Volunteer cheated!\n",l+1);
    }
    if(is.size()==1){
      printf("Case #%d: %d\n",l+1,is[0]);
    }
    if(is.size()>1){
      printf("Case #%d: Bad magician!\n",l+1);
    }
  }
  
  return 0;
}
