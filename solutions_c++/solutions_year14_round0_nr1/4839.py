#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("question.txt","r",stdin);
	freopen("B_ans.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int ctr,x,y,ans,j,i,k=0;
	while(t--){
		map<int,int> m;
			   k++;
		int a[4][4];
		int b[4];
		scanf("%d",&x);
		for( i = 0; i<4; i++){
			for(j = 0 ;j<4; j++){
				scanf("%d",&a[i][j]);
			}
		}
		for(i = 0 ; i < 4 ;i++){
			m[a[x-1][i]] = 1;
		}
		scanf("%d",&y);
			for( i = 0; i<4; i++){
			for(j = 0 ;j<4; j++){
				scanf("%d",&a[i][j]);
			}
		}
		ctr = 0;
		for(i = 0; i < 4;i++){
			if(m[a[y-1][i]] == 1){
				ctr++;
				ans = a[y-1][i];
			}
		}
		if(ctr == 1){
			printf("Case #%d: %d\n",k,ans);
		} else if(ctr > 1){
			printf("Case #%d: Bad magician!\n",k );
		} else printf("Case #%d: Volunteer cheated!\n",k);
		ctr++;
	}
	fclose(stdout);
}
