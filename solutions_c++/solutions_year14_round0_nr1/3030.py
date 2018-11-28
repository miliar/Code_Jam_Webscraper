#include<iostream>
using namespace std;
int main()
{

	int t,an1,an2,a[5][5],bitmap=0,c = 0,ans = 0;
	scanf("%d",&t);
	for(int p=1;p<=t;p++){

		bitmap = 0;
		c = 0;ans = 0;
		scanf("%d",&an1);
		
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&a[i][j]);
			}
		}
		
		for(int i=0;i<4;i++){
			bitmap |= (1 << a[an1-1][i]);
		}
		
		scanf("%d",&an2);
		
		for(int i=0;i<4;i++){
			for(int j=0;j<4;j++){
				scanf("%d",&a[i][j]);
			}
		}
		
		for(int i=0;i<4;i++){
			if(bitmap & (1 << a[an2-1][i])){
				ans = a[an2-1][i];
				++c;
			}
		}
		
		if(c == 1){
			printf("Case #%d: %d\n",p,ans);
		}
		else if(c > 1){
				printf("Case #%d: %s\n",p,"Bad magician!");
		}
		else{
			    printf("Case #%d: %s\n",p,"Volunteer cheated!");
		}
		
	}
}
