#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int main(){
	int TN, X, R, C, ca=0;
	scanf("%d", &TN);
	while(TN--){
		scanf("%d%d%d", &X, &R, &C);
		int ans;
		if(R%X==0||C%X==0){
			if(C%X==0)swap(R, C);
			if(X==1||X==2){
				ans=1;
			}
			else if(X==3){
				if(C>=2){
					ans=1;
				}
				else{
					ans=0;
				}
			}
			else if(X==4){
				if(C>=3){
					ans=1;
				}
				else{
					ans=0;
				}
			}
		}
		else{
			ans=0;
		}
		if(ans){
			printf("Case #%d: GABRIEL\n", ++ca);

		}else{
			printf("Case #%d: RICHARD\n", ++ca);

		}
	}
	return 0;
}