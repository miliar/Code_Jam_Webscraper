#include <stdio.h>
#include <stdlib.h>
#include <string.h>

using namespace std;

void solve();

int main(){
	int cases;
	scanf("%d", &cases);
	for(int i=0; i<cases; i++){
		printf("Case #%d: ", (i+1));
		solve();
	}
	return 0;
}

void solve(){
	int choice, used[17], tmp, res = 0, ret;
	
	memset(used, 0, sizeof(used));

	scanf("%d", &choice);
	choice--;
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			scanf("%d", &tmp);
			if(i==choice){
				used[tmp]++;
			}
		}
	}

	scanf("%d", &choice);
	choice--;	
	for(int i=0; i<4; i++){
		for(int j=0; j<4; j++){
			scanf("%d", &tmp);
			if(i==choice){
				if(used[tmp]){
					res++;
					ret = tmp;
				}
			}
		}
	}

	if(res == 0){
		printf("Volunteer cheated!\n");
	}else if(res == 1){
		printf("%d\n", ret);
	}else{
		printf("Bad magician!\n");
	}
}