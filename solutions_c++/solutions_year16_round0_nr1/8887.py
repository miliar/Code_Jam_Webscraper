#include<cstdio>

using namespace std;


void printBits(int a,int c){
	for(int i=0;i<=c;i++){
		printf("%d",(a&(1<<(c-i)))==0?0:1);
	}
	printf("\n");
}

int digitFinder(int n){
	int a = 0;
	while(n){
		a|=(1<<(n%10));
		n/=10;
	}
	return a;
}

int main(){
	int t,n;
	//freopen("input.txt","r",stdin);
	//freopen("output.txt","w",stdout);
	scanf("%d",&t);
	int tests=t;
	while(t--){
		scanf("%d",&n);
		printf("Case #%d: ",tests-t);
		if(n==0){
			printf("INSOMNIA\n");
		}
		else{
			int a=0;
			int ans=n;
			while(a^1023){
				a|=digitFinder(ans);
                //printf("ans=%d a=",ans);
				//printBits(a,11);

				ans+=n;

				//printf("\n\nxor %d\n\n",a^1023);
			}
			printf("%d\n",ans-n);
		}
	}
	return 0;
}
