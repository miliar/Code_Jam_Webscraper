#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<vector>
#include<math.h>
#include<stdlib.h>
#include<set>
#include<ctype.h>
#include<set>
#include<string>
using namespace std;

#define X first
#define Y second
typedef long long ll;
typedef pair<int,int> Pi;

char ch[11][110];
int chk[100010];
set <string> S[4];

int main()
{
	freopen("input.txt","r",stdin);
	FILE *fp = fopen("output.txt","w");
	int Tc;
	scanf("%d",&Tc);
	for(int tt=1;tt<=Tc;tt++){
		fprintf(fp,"Case #%d: ", tt);
		int m, n;
		scanf("%d%d",&m,&n);
		for(int i=1;i<=m;i++)scanf("%s",ch[i]+1);
		memset(chk,0,sizeof chk);
		int r[10];
		for(int i=0;i<10;i++)r[i] = 0;
		while(!r[m+1]){
			int cki = 0;
			int i;
			for(i=1;i<=m;i++){
				string temp;
				for(int j=1;ch[i][j];j++){
					temp += ch[i][j];
					if(S[r[i]].find(temp) == S[r[i]].end()){
						if(S[r[i]].empty())cki += 2;
						else cki++;S[r[i]].insert(temp);
					}
				}
			}
			++chk[cki];
			if(n == 1)break;
			r[1]++;
			int now = 1;
			while(r[now] == n){
				r[now] = 0;
				r[++now]++;
			}
			for(i=0;i<n;i++)S[i].clear();
		}
		int i;
		for(i=100000;i>=0;i--){if(chk[i]){fprintf(fp,"%d %d\n",i,chk[i]);break;}}
		if(i == -1)fprintf(fp,"0 0\n");
		printf("%d",tt);
	}
	return 0;
}
