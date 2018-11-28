#include<stdio.h>
#include<stdlib.h>

int main() {
	freopen("1B/A-small-attempt3.in", "r", stdin);
	freopen("1B/out.txt","w",stdout);

	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		int N;
		scanf("%d",&N);

		char strs[2][101];

		scanf("%s",strs[0]);
		scanf("%s",strs[1]);

		bool isNo=false;
		int i=0,j=0,count=0,state=0;

		if(strs[0][0] != strs[1][0])isNo=true;
		while(!isNo && (strs[0][i] != '\0' || strs[1][j] != '\0')) {
			if(strs[0][i] == strs[1][j]){
				i++;
				j++;
			}else{
				if(state == 0){
					if(strs[0][i] == strs[0][i-1])state=1;
					else if(strs[1][j] == strs[1][j-1])state =2;
					else {
						isNo=true;
						break;
					}
				}
				if(state==1){
					count++;
					i++;
					state=0;
				}else if(state==2){
					count++;
					j++;
					state=0;
				}
			}
		}

		if(isNo) {
			printf("Case #%d: Fegla Won\n",t);
		} else {
			printf("Case #%d: %d\n",t,count);
		}
	}
}
