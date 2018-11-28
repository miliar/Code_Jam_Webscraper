#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <map>
#include <set>
#include <vector>
using namespace std;

#define mp(x, y) make_pair((x), (y))

int T;

int main()
{
	scanf("%d\n", &T);

	for(int t=1; t<=T; t++) {
		int r, c;
		scanf("%d %d\n", &r, &c);
		char g[123][123];
		for(int i=0; i<r; i++) {
			for(int j=0; j<c; j++) scanf("%c", &g[i][j]);
			scanf("\n");
		}
		int ans=0;
		int row[123][2], col[123][2];
		for(int i=0; i<r; i++) {
			row[i][0]=123;
			row[i][1]=-1;
		}
		for(int j=0; j<c; j++) {
			col[j][0]=123;
			col[j][1]=-1;
		}
		for(int i=0; i<r; i++) {
			for(int j=0; j<c; j++) {
				if(g[i][j]!='.') {
					row[i][0]=min(row[i][0], j);
					row[i][1]=max(row[i][1], j);
					col[j][0]=min(col[j][0], i);
					col[j][1]=max(col[j][1], i);
				}
			}
		}
		for(int i=0; ans!=-1 && i<r; i++) {
			for(int j=0; ans!=-1 && j<c; j++) {
				if(g[i][j]=='<') {
					if(row[i][0]>=j) {
						if(row[i][0]==j && row[i][1]==j && col[j][0]==i && col[j][1]==i) {
							ans=-1;
						} else {
							ans++;
						}
					}
				}
				else if(g[i][j]=='>') {
					if(row[i][1]<=j) {
						if(row[i][0]==j && row[i][1]==j && col[j][0]==i && col[j][1]==i) {
							ans=-1;
						} else {
							ans++;
						}
					}
				}
				else if(g[i][j]=='^') {
					if(col[j][0]>=i) {
						if(row[i][0]==j && row[i][1]==j && col[j][0]==i && col[j][1]==i) {
							ans=-1;
						} else {
							ans++;
						}
					}
				}
				else if(g[i][j]=='v') {
					if(col[j][1]<=i) {
						if(row[i][0]==j && row[i][1]==j && col[j][0]==i && col[j][1]==i) {
							ans=-1;
						} else {
							ans++;
						}
					}
				}
			}
		}
		if(ans==-1) {
			printf("Case #%d: %s\n", t, "IMPOSSIBLE");
		} else {
			printf("Case #%d: %d\n", t, ans);
		}
	}

	return 0;
}
