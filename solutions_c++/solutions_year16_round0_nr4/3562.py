#include <bits/stdc++.h>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		int K,C,S;
		scanf("%d %d %d",&K,&C,&S);
		if(S<=K-1){
			printf("Case #%d: IMPOSSIBLE\n",i+1);
		}else{
			printf("Case #%d: ",i+1);
			for(int j=0;j<S;j++){
				printf("%d ",j+1);
			}
			puts("");
		}	
	}
	return 0;
}


