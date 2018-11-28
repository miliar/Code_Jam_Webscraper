#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>

#include <vector>
#include <set>
#include <map>
#include <deque>
#include <string>
#include <bitset>

#include <algorithm>
#include <cmath>
using namespace std;

int const MAX_N = 1510;

struct pp {
	int x0,y0,x1,y1;
} bld[MAX_N];


int const DX[8] = {-1,-1,-1,0,0,1,1,1};
int const DY[8] = {-1,0,1,-1,1,-1,0,1};
int const INF = 1000000000;

char s[MAX_N][MAX_N];
int d[MAX_N][MAX_N];

struct pt {
	int x,y;
	pt():x(-1),y(-1) {}
	pt(int x, int y):x(x),y(y) {}
} from[MAX_N][MAX_N];
deque<pt> q;

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for (int QQ=0; QQ<t; QQ++) {
		int W,H,B;
		cin>>W>>H>>B;
		for (int i=0; i<B; i++) {
			cin>>bld[i].x0>>bld[i].y0>>bld[i].x1>>bld[i].y1;
			swap(bld[i].x0,bld[i].y0);
			swap(bld[i].x1,bld[i].y1);
		}

		int mn = 2000000000;

		set<int> ms;
		for (int i=0; i<B; i++) {
			ms.insert(bld[i].x0);
			ms.insert(bld[i].x1);
		}

		int CNT = 0;
		map<int,int> mpp;
		for (set<int>::iterator iter = ms.begin(); iter!=ms.end(); ++iter) {
			mpp[*iter] = CNT;
			CNT += 2;
		}

		int mx_HH = max(H, CNT+1);

		//
		{
			int n = H; //mx_HH;
			int m = W;

			for (int i=0; i<n; i++)
				for (int j=0; j<=m+2; j++)
					s[i][j] = '.';

			for (int i=0; i<B; i++) {
				int min_y = bld[i].y0+1;
				int max_y = bld[i].y1+1;
				int min_x = bld[i].x0; //mpp[bld[i].x0];
				int max_x = bld[i].x1; //mpp[bld[i].x1];

				for (int kk=min_x; kk<=max_x; kk++)
					for (int rr=min_y; rr<=max_y; rr++)
						s[kk][rr] = '*';
			}

			for (int i=0; i<MAX_N; i++)
				for (int j=0; j<MAX_N; j++)
					d[i][j] = INF;

			for (int i=0; i<n; i++) {
				d[i][0] = 0;
				q.push_back(pt(i,0));
			}
			while (!q.empty()) {
				int x = q.front().x;
				int y = q.front().y;
				q.pop_front();

				if (y > m) continue;

				for (int k=0; k<8; k++) {
					int new_x = x + DX[k];
					int new_y = y + DY[k];
					if (new_x >= 0 && new_x < n && new_y >= 1 && new_y <= m+1)
						if (s[new_x][new_y]=='.') {
							if (d[new_x][new_y] > d[x][y] + 1) {
								d[new_x][new_y] = d[x][y] + 1;
								from[new_x][new_y] = pt(x,y);
								q.push_back(pt(new_x,new_y));
							}
						}
						else {
							if (d[new_x][new_y] > d[x][y]) {
								d[new_x][new_y] = d[x][y];
								from[new_x][new_y] = pt(x,y);
								q.push_front(pt(new_x,new_y));
							}
						}
				}
			}
			
			int ans_i = -1, ans_j = -1;
			for (int i=0; i<n; i++)
				if (d[i][m+1] < mn) {
					mn = d[i][m+1];
					ans_i = i;
					ans_j = m+1;
				}

			int cur = 0;
			while (ans_j > 0) {
				if (s[ans_i][ans_j] == '.') {
					s[ans_i][ans_j] = '#';
					if (ans_i >= 0 && ans_i<n && ans_j>=1 && ans_j<=m)
						cur++;
				}
				int new_ans_i = from[ans_i][ans_j].x;
				int new_ans_j = from[ans_i][ans_j].y;
				ans_i = new_ans_i;
				ans_j = new_ans_j;
			}

			mn = cur;
			/*for (int i=0; i<n; i++) {
				for (int j=1; j<=m; j++)
					printf("%c",s[i][j]);
				printf("\n");
			}*/
		}
		//

		int cnt = 0;
		printf("Case #%d: %d\n",QQ+1,mn);
	}

	return 0;
}