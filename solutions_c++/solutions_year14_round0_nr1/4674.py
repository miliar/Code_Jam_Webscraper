#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    freopen("Input.txt","r",stdin);
    freopen("Output.txt","w",stdout);
	bool hash[20];
	int mat[5][5];
	int T,a,b,kase;
	scanf("%d",&T);
	for(kase = 1;kase <= T;++kase)
	{
		int i,j,cnt = 0,res = -1;
		scanf("%d",&a);
		memset(hash,false,sizeof(hash));
		for(i = 1;i <= 4;++i){
			for(j = 1;j <= 4;++j){
				scanf("%d",&mat[i][j]);
				if(i==a) hash[mat[i][j]] = true;
			}
		}
		scanf("%d",&b);
		for(i = 1;i <= 4;++i){
			for(j = 1;j <= 4;++j){
				scanf("%d",&mat[i][j]);
				if(i==b&&hash[mat[i][j]]){cnt++;res = mat[i][j];}
			}
		}
		if(cnt==1)
			printf("Case #%d: %d\n",kase,res);
		else if(cnt>1)
			printf("Case #%d: Bad magician!\n",kase);
		else
			printf("Case #%d: Volunteer cheated!\n",kase);
	}
	return 0;
}
