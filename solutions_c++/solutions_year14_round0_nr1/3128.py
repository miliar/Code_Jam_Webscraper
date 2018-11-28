#pragma warning(disable:4996)
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<algorithm>
#include<vector>
using namespace std;

int C,n,m;
int a[4][4],b[4][4];

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&C);
	for(int tc=1;tc<=C;tc++){
		scanf("%d",&n);
		for(int i=0;i<4;i++)for(int j=0;j<4;j++)scanf("%d",&a[i][j]);
		scanf("%d",&m);
		for(int i=0;i<4;i++)for(int j=0;j<4;j++)scanf("%d",&b[i][j]);
		vector<int> ans;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(a[n-1][i]==b[m-1][j])
					ans.push_back(a[n-1][i]);
		printf("Case #%d: ",tc);
		if(!ans.size())
			puts("Volunteer cheated!");
		else if(ans.size()==1)
			printf("%d\n",ans[0]);
		else
			puts("Bad magician!");
	}
	return 0;
}