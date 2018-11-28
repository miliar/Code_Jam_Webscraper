#include <stdio.h>

bool visit[12];
int summ = 0;
int n;
int x;
int i;
int mod10;
int nex;
bool out;
int nq;
int tmp;

int main(){
	freopen("input1L.txt","r",stdin);
	freopen("output1L.txt","w",stdout);
	scanf("%d",&nq);
	tmp = nq;
	while(nq--){
		scanf("%d",&n);
	//	printf("n = %d\n",n);
		printf("Case #%d: ",tmp-nq);
		for(i=0;i<10;i++) visit[i] = 0;
		summ = 0;
		out = 0;
		for(i=1;i<=100;i++){
			x = n*i;
			//printf("x = %d\n",x);
			while(x>0){
			//	printf("x2 = %d\n",x);
				nex = x/10;
				mod10 = x-nex*10;
				if(!visit[mod10]){
					visit[mod10] = 1;
					summ++;
				}
				x = nex;
			}
			if(summ==10){
				printf("%d",n*i);
				out = 1;
				break;
			}
		}
		if(!out) printf("INSOMNIA");
		printf("\n");
		//getchar();
	}
	return 0;
}
