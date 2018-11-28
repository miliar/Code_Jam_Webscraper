#include <iostream>
using namespace std;
int used[10];
int main(){
	int Test;
	scanf(" %d",&Test);
	for(int tt = 1 ; tt <= Test ; tt++){
		int n;
		scanf(" %d",&n);
		for(int i = 0 ; i < 10 ; i++) used[i]=0;
		printf("Case #%d: ",tt);
		if(n == 0) printf("INSOMNIA\n");
		else{
			int count = 0;
			for(int i = 1 ; ;i++){
				int k = i*n;
				while(k){
					int digit = k%10;
					if(!used[digit]) count++;
					used[digit]=1;
					k/=10;
				}
				if(count == 10){
					printf("%d\n",i*n);
					break;
				}
			}
		}
	}
	return 0;
}