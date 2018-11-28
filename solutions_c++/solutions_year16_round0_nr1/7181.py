#include <cstdio>
#include <cstdlib>

using namespace std;

int main(){
	int t;
	scanf("%d",&t);
	for(int index = 1;index <= t;index++){
		long long int n;
		long long int k = 0;
		long long int temp;
		long long int check = 0;
		scanf("%lld",&n);
		if(n == check){
			printf("Case #%d: INSOMNIA\n",index);
			continue;
		}
		int * flags = (int *)calloc(sizeof(int),10);
		int count = 0;
		while(count < 10){
			k++;
			temp = k * n;
			while(temp){
				if(flags[temp%10]==0){
					flags[temp%10] = 1;
					count++;
				}
				temp = temp / 10;
			}	
		}
		printf("Case #%d: %lld\n",index,k*n );		

	}
	return 0;
}