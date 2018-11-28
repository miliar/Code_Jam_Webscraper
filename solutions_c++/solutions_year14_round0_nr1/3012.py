

#include <stdio.h>

//magic trick
void main(){
	
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	
	int t=0,r1,r2,r1a[4],r2a[4],c=0,cc=0,card; //test cases
	scanf("%d",&t);
	
//	printf("%d \n",t);
	for(int k=1;k<=t;k++){
	
		scanf("%d",&r1);
	//	printf("%d\n",r1);
			for(int k1=1;k1<=4;k1++){
	//	printf("line %d ",k1);	
				for(int k2=1;k2<=4;k2++){
				if(k1==r1){
				scanf("%d",&r1a[k2-1]);
		//		printf(" %d ",r1a[k2-1]);
					}
					else{
				scanf("%d",&c);
				//printf("%d",c);
					}
				}
		//	printf("\n");	
		
			}


			scanf("%d",&r2);
	//	printf("%d\n",r2);
			for(int k1=1;k1<=4;k1++){
		//	printf("***line %d ",k1);	
				for(int k2=1;k2<=4;k2++){
				if(k1==r2){
				scanf("%d",&r2a[k2-1]);
			//	printf(" %d ",r2a[k2-1]);
					}
					else{
				scanf("%d",&c);
				//printf("%d",c);
					}
				}
		//	printf("\n");	
		
			}

			cc=0;
			for(int ch1=1;ch1<=4;ch1++){
			for(int ch2=1;ch2<=4;ch2++){
				if(r1a[ch1-1]==r2a[ch2-1]){cc++;card=r1a[ch1-1];}

			}
			}
			if(cc==0)printf("Case #%d: Volunteer cheated!\n",k);
			if(cc==1)printf("Case #%d: %d\n",k,card);
			if(cc>1)printf("Case #%d: Bad magician!\n",k);
			//printf("\ncc++ =%d\n\n",cc);
			
	}
		
	
	
	}



