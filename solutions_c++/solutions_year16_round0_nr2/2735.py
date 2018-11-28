#include <iostream>
using namespace std;
char ar[200];
int main(){
	int Test;
	scanf(" %d",&Test);
	for(int tt = 1 ; tt <= Test ; tt++){
		int n;
		scanf(" %s",ar);
		printf("Case #%d: ",tt);
		n= strlen(ar);
		bool flag = false;
		int res = 0;
		for(int i = n-1 ; i >= 0 ; i--){
			while(i > 0 && ar[i] == ar[i-1]) i--;
			if(i == 0){
				if(ar[i] == '+' && flag) res++;
				if(ar[i] == '-' && !flag) res++;
				break;
			}
			res++;
			flag = !flag;
		}
		printf("%d\n",res);
	}
	return 0;
}