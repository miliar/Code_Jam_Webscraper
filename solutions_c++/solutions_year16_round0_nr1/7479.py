#include<stdio.h>
#include<math.h>

int N;
long long int newN;
int T;

int check[10];

int main(){
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int i,j,k;
	int cnt;
	int flag;
	scanf("%d",&T);
	for(k=1;k<=T;k++){
		flag=1;
		for(i=0;i<10;i++)check[i]=0;
		cnt=0;
		
		scanf("%d",&N);
		if(N == 0){
			printf("Case #%d: INSOMNIA\n",k);
			continue;
		}
		while(cnt!=10){
			newN = N*(flag++);
			for(j=10;j>=0;j--)if(newN/int(pow(10,j)) != 0)break;
			for(i=0;i<=j;i++){
				if(!check[(newN/int(pow(10,i)))%10]){
					check[(newN/int(pow(10,i)))%10]=1;
					cnt++;
				}
			}
		}
		printf("Case #%d: %d\n",k,newN);
	}
	
	return 0;
}
