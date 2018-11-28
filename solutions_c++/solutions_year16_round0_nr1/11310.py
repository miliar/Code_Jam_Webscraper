#include<stdio.h>
int main(){
	 freopen("input.txt","r",stdin);
     freopen("output.txt","w",stdout);
  int y1,y2;
  scanf("%d",&y2);
  for(y1=1;y1<=y2;y1++){
  		int N,j,i=1,k,l2,l1,i1,a[10]={},b,n;
	scanf("%d",&n);
	 N=n;
	for(j=1;j<100;j++){
		for(i=1;i<1000000;i=i*10){
			 l2=N;
			if(N<i){
			for(k=i/10;k>0;k=k/10){
				l1=l2/k;
				l2=l2%k;
				a[l1]=1;
			
			}
			for(i1=0;i1<10;i1++){
				if(a[i1]!=1){
				 b=0;
				  N=N+n;
				 break;	
				}
				 else
				 b=1;
			}
			break;
			}
		
			
		}
	 if(b==1){
      printf("Case #%d: %d\n",y1,N);
      break;
	 }
    
	  
	}
 if(b!=1){
 	printf("Case #%d: INSOMNIA\n",y1);
 }
  }
	return 0;
}
