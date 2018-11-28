#include<stdio.h>
#include<math.h>

int main(){
	int c;
	int i;
	scanf("%d",&c);
	
	for(i = 1;i <= c;i++){
		int a,b;
		scanf("%d %d",&a,&b);
        int y = 0;
		int q = 0;
		for(int j = a;j <= b;j++){
			int count = 1;  //碭计
			int countsqrt = 1;//キよ碭计
			
			if((int)sqrt((float) j) - sqrt((float) j) == 0){  //璶耞计j
				for(int k = 10;k <= b;k = k*10){				
					if(j / k != 0){  //耞jΤ碭计
						count ++;
					}//end if
					else{
						break;
					}//end else
				}

				/*耞キよΤ碭计*/
				for(int k = 10;k <= (int)sqrt((float) j);k = k*10){				
					if(j / k != 0){  //耞jΤ碭计
						countsqrt ++;
					}//end if
					else{
						break;
					}//end else
				}//end for

				/*耞キよ琌癸嘿*/
				if(countsqrt == 1){
					q++;
				}//end if
				else{
					for(int l = 1;l <= countsqrt/2;l++){
						if(((int)sqrt((float) j) % (int)pow(10.00,(double)l) / (int)pow(10.00,(double)l - 1)) == ((int)((int)sqrt((float) j) / (int)pow(10.00,(double)countsqrt - l)) % 10 )){
							q++;
						}//end if
					}//end for
				}//end else


				if(q != 0){
					/*耞琌癸嘿*/
					if(count == 1){
						y++;
					}//end if
					else{
						for(int l = 1;l <= count/2;l++){
							if((j % (int)pow(10.00,(double)l) / (int)pow(10.00,(double)l - 1)) == ((int)(j / (int)pow(10.00,(double)count - l)) % 10 )){
								y++;
							}//end if
						}//end for
					}//end else
				}//end if
				q = 0;
			

			}//end if
			else{
				continue;
			}
		}//end for
		printf("Case #%d: %d",i,y);
		printf("\n");
	}//end for
}//end main