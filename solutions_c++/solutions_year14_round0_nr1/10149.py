#include<iostream>
using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	for(int q=1;q<=t;q++){
		bool a[20],b[20]; for(int i=0;i<20;i++){a[i]=false; b[i]=false;}
		int ans,in;
		scanf("%d",&ans);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				scanf("%d",&in);
				if(i==ans)a[in]=true;
			}
		}
		
		scanf("%d",&ans);
		for(int i=1;i<=4;i++){
			for(int j=1;j<=4;j++){
				scanf("%d",&in);
				if(i==ans)b[in]=true;
			}
		}
		
		int cnt=0;
		int ret=0;
		for(int i=1;i<=16;i++){
			if(a[i]&&b[i]){ cnt++; ret=i; }
		}

		printf("Case #%d: ",q);
		if(cnt==0){
			printf("Volunteer cheated!\n");
		}
		else if(cnt==1){
			printf("%d\n",ret);
		}
		else {
			printf("Bad magician!\n");
		}
	}
}