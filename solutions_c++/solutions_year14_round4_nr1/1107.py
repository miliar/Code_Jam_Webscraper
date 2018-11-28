#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
using namespace std;
int N,s[10005],X;
int main(){
	int T;
	scanf("%d",&T);

	for(int ca = 1; ca <=T ;ca++){
		scanf("%d %d",&N, &X);
		for(int i=0;i<N;i++){
			scanf("%d",&s[i]);
		}


		
		sort(s,s + N);
		int ans = 0;
		int j = 0;
		for(int i=N - 1; i >=0 ; i--){
			if(i == j){
				ans++;
				break;
			}
			if(i < j){
				break;
			}
			if(s[i] + s[j] <= X){
				ans++;
				j++;
			}else{
				ans++;
			}
		}




		printf("Case #%d: ",ca);
		printf("%d\n",ans);
	}
	return 0;
}
