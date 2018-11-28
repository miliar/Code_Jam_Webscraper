#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <set>
#include <iostream>

using namespace std;
int S[10];
int main(){
	freopen("A-small-attempt0.in","r",stdin);
	freopen("a.out.txt","w",stdout);
	
	int T,row,now,idx,cas;
	scanf("%d",&T);
	for(cas = 1; cas <= T; cas++){
		idx = 0;
		for(int i = 1; i <= 2; i ++){
			scanf("%d",&row);
			for(int j = 1; j <= 16; j ++){
				scanf("%d",&now);
				if(j > (row - 1) * 4 && j <= row * 4){
					S[idx ++] = now;
				}
			}
		}
		sort(S,S+8);
		printf("Case #%d: ",cas);
		int ans,num = 0;
		for(int i = 0; i < 7; i ++){
			if(S[i] == S[i + 1]){
				ans = S[i];
				num ++;
			}
		}
		if(num == 1){
			printf("%d\n",ans);
		}
		if(num > 1){
			printf("Bad magician!\n");
		}
		if(num == 0){
			printf("Volunteer cheated!\n");
		}
		
	}
	return 0;
}