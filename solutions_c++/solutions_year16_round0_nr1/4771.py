#include <cstdio>
bool digit[10];
void count(int num);

int main(){
	int T,N,total,Case=1;
	scanf("%d",&T);
	while(T--){
		for(int i=0;i<10;i++){
			digit[i]=false;
		}
		scanf("%d",&N);
		total=N;
		count(total);
		if(N+total==N){
			printf("Case #%d: INSOMNIA\n",Case++);
			continue;
		}else{
			for(int i=0;i<10;i++){
				if(digit[i]&&i==9){
					printf("Case #%d: %d\n",Case++,N);
				}else if(digit[i]==false){
					count(N+total);
					N+=total;
					i=-1;
				}
			}
		}
	}
}

void count(int num){
	while(num){
		digit[num%10]=true;
		num/=10;
	}
}