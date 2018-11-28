#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <string>
using namespace std;
typedef long long int64;
const int maxn=110;

char s[1000];
int mp[maxn][maxn];
int forbid[maxn][maxn];
void testcase() {
	int row, col;
	scanf("%d%d",&row,&col);
	for(int i=1;i<=row;i++) {
		scanf("%s",&s);
		for(int j=1;j<=col;j++) {
			if(s[j-1]=='.')
				mp[i][j]=0;
			if(s[j-1]=='^')
				mp[i][j]=1; //up
			if(s[j-1]=='>')
				mp[i][j]=2; //right
			if(s[j-1]=='v')
				mp[i][j]=3; //down
			if(s[j-1]=='<')
				mp[i][j]=4; //left
		}
	}
	
	memset(forbid,0,sizeof(forbid));
	for(int i=1;i<=row;i++) {
		for(int j=1;j<=col;j++)
			if(mp[i][j]) { //left
				forbid[i][j]|=1<<4;
				break;
			}
		for(int j=col;j>=1;j--)
			if(mp[i][j]) { //right
				forbid[i][j]|=1<<2;
				break;
			}
	}
	for(int i=1;i<=col;i++) {
		for(int j=1;j<=row;j++)
			if(mp[j][i]) { //up
				forbid[j][i]|=1<<1;
				break;
			}
		for(int j=row;j>=1;j--)
			if(mp[j][i]) { //down
				forbid[j][i]|=1<<3;
				break;
			}
	}
	
	int ans=0;
	for(int i=1;i<=row;i++)
	for(int j=1;j<=col;j++)
		if(mp[i][j])
			if(forbid[i][j]&(1<<mp[i][j])) {
				if(forbid[i][j]==(1<<1)+(1<<2)+(1<<3)+(1<<4)) {
					printf("IMPOSSIBLE\n");
					return;
				} else
					ans++;
			}
	printf("%d\n",ans);
}
int main() {
	int T;
	scanf("%d",&T);
	for(int i=1;i<=T;i++) {
		printf("Case #%d: ",i);
		testcase();
	}
	scanf("%*s");
	return 0;
}
