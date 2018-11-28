#include <bits/stdc++.h>
using namespace std;
int main()
{
	int test;
	scanf("%d",&test);
	int iter;
	for(iter = 0; iter < test; iter++ ){
		int f[4][4],s[4][4],fa,sa;
		scanf("%d",&fa);
		int i,j;
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&f[i][j]);
			}
		}
		scanf("%d",&sa);
		for(i=0;i<4;i++){
			for(j=0;j<4;j++){
				scanf("%d",&s[i][j]);
			}
		}
		int cnt = 0;
		int val;
		for(i=0;i<4;i++){
			if(cnt>1)
			break;
			for(j=0;j<4;j++){
				if(f[fa-1][i]==s[sa-1][j]){
					cnt++;
					val = f[fa-1][i];
					break;
				}
			}
		}
		if(cnt==1)
		printf("Case #%d: %d\n",iter+1,val);
		else if( cnt > 1){
			printf("Case #%d: Bad magician!\n",iter+1);
		}
		else{
			printf("Case #%d: Volunteer cheated!\n",iter+1);
		}
	}
	return 0;
}
