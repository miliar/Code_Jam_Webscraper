#include <stdio.h>
#include <functional>
#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <stack>
#include <map>
#include <set>
using namespace std;

int N,M;
char S[101][101];

int main()
{
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);

	int Test; scanf ("%d",&Test); for (int Case=1;Case<=Test;Case++){
		printf ("Case #%d: ",Case);

		scanf ("%d %d",&N,&M);
		for (int i=0;i<N;i++) scanf ("%s",S[i]);
		int ans = 0;
		for (int i=0;i<N;i++) for (int j=0;j<M;j++) if (S[i][j] != '.'){
			bool good[4] = {0,};
			int dx[4] = {0,1,0,-1};
			int dy[4] = {1,0,-1,0};
			char s[6] = ">v<^";
			for (int k=0;k<4;k++){
				int x = i + dx[k];
				int y = j + dy[k];
				while (0 <= x && x < N && 0 <= y && y < M){
					if (S[x][y] != '.'){
						good[k] = 1;
						break;
					}
					x += dx[k];
					y += dy[k];
				}
			}

			int ad = -200000;
			for (int k=0;k<4;k++) if (good[k]){
				if (s[k] == S[i][j]) ad = 0;
				else if (ad < 0) ad = 1;
			}
			ans += ad;
		}
		if (ans < -100000) puts("IMPOSSIBLE");
		else printf ("%d\n",ans);
	}

	return 0;
}