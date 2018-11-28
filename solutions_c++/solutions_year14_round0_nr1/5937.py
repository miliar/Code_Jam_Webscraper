#include <cstdio>
#include <cstring>

using namespace std;
int T;

int main(){
  scanf("%d",&T);
  for(int k=0;k<T;++k){
    int S,E;
	int a[16];
	int b[16];
    scanf("%d",&S);
    for(int i=0;i<16;++i)
      scanf("%d",&a[i]);
    
    scanf("%d",&E);
    for(int i=0;i<16;++i)
      scanf("%d",&b[i]);

    int ans=0;

    for(int i=0;i<4;++i)
      for(int j=0;j<4;++j)
	{
	  if( a[(S-1)*4+i] == b[(E-1)*4+j]){
	    if( ans==0) 
	      ans=a[(S-1)*4+i];
	    else{
	      printf("Case #%d: Bad magician!\n",k+1);
	      goto ESCAPE;
	    }
	  }
	  
	}
  

    if( ans==0 )
      printf("Case #%d: Volunteer cheated!\n",k+1);
    else 
      printf("Case #%d: %d\n",k+1,ans);
  
  ESCAPE:;
  }
  return 0;
}
