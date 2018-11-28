//---------------------------------------------------------------------
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


//---------------------------------------------------------------------

char s[110][110];
int const INT_INF = 1000000000;
int const DX[4] = {-1,1,0,0};
int const DY[4] = {0,0,-1,1};
int const MEGA_DX[8] = {-1,-1,-1,0,0,1,1,1};
int const MEGA_DY[8] = {-1,0,1,-1,1,-1,0,1};

int x[110*110],y[110*110],nnew[110][110],bad[110][110];

int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;
	scanf("%d",&t);
	for (int qq=0; qq<t; qq++) {
		int r,c,m;
		scanf("%d%d%d",&r,&c,&m);
		
		for (int i=0; i<r; i++)
			for (int j=0; j<c; j++)
				s[i][j] = '.';

		int Ok = 0;
		
		int DENS = 4;
		if (c == 1 || r == 1)
			DENS = 2;

		if (m == r*c-1) {
			Ok = 1;
			for (int i=0; i<r; i++)
				for (int j=0; j<c; j++)
					s[i][j] = '*';
			s[0][0] = 'c';
		}
		else if (m <= r*c-DENS) {
			Ok = 0;

			for (int fr_x = 0; fr_x<r && !Ok; fr_x++)
				for (int fr_y=0; fr_y<c && !Ok; fr_y++) {
					if (r*c-(r-fr_x)*(c-fr_y) < m) continue;

					for (int i=0; i<r; i++)
						for (int j=0; j<c; j++)
							s[i][j] = '*';
					int cnt = r*c-1;
					s[r-1][c-1] = '.';
					if (DENS <= 2) {
						if (r < c)
							s[r-1][c-2] = '.';
						else
							s[r-2][c-1] = '.';
						cnt--;
					}
					else {
						s[r-2][c-2] = s[r-2][c-1] = s[r-1][c-2] = '.';
						cnt-=3;
					}

					for (int i=fr_x; i<r; i++)
						for (int j=fr_y; j<c; j++)
							if (s[i][j]=='*') {
								s[i][j] = '.';
								cnt--;
							}

					int is_cur_Ok = 1;

					while (cnt > m) {
						int ans_x = -1, ans_y = -1;
						pair<int,int> mn;
						mn.first = mn.second = INT_INF;
						for (int i=0; i<r; i++)
							for (int j=0; j<c; j++)
								if (s[i][j]=='.')
									for (int k=0; k<4; k++) {
										int x = i + DX[k];
										int y = j + DY[k];
										if (x>=0 && x<r && y>=0 && y<c && s[x][y]=='*') {
											int d1 = r+1-x;
											int d2 = c+1-y;
											pair<int,int> mmmm;
											mmmm.first = max(d1,d2);
											mmmm.second = d1+d2;
											if (mmmm < mn) {
												mn = mmmm;
												ans_x = x;
												ans_y = y;
											}
										}
									}
						s[ans_x][ans_y] = '.';
						cnt--;
					}
					s[r-1][c-1]='c';

					for (int i=0; i<r; i++)
						for (int j=0; j<c; j++)
							bad[i][j] = 0;
					for (int i=0; i<r; i++)
						for (int j=0; j<c; j++)
							if (s[i][j] == '.')
								for (int k=0; k<8; k++) {
										int x = i + MEGA_DX[k];
										int y = j + MEGA_DY[k];
										if (x>=0 && x<r && y>=0 && y<c && s[x][y]=='*')
											bad[i][j] = 1;
									}

					for (int i=0; i<r; i++)
						for (int j=0; j<c; j++)
							nnew[i][j] = 0;

					int p_read = 0, p_write = 1;
					x[0] = r-1; y[0] = c-1;
					nnew[r-1][c-1] = 1;

					while (p_read < p_write) {
						int ii = x[p_read];
						int jj = y[p_read];
						p_read++;

						for (int k=0; k<4; k++) {
							int new_ii = ii + DX[k];
							int new_jj = jj + DY[k];
							if (new_ii>=0 && new_ii<r && new_jj>=0 && new_jj<c)
								if (s[new_ii][new_jj]!='*' && !bad[new_ii][new_jj] && !nnew[new_ii][new_jj]) {
									nnew[new_ii][new_jj] = 1;
									x[p_write] = new_ii;
									y[p_write] = new_jj;
									p_write++;
								}
						}
					}

					for (int i=0; i<r; i++)
						for (int j=0; j<c; j++)
							if (bad[i][j]) {
								int is_sos = 0;
								for (int k=0; k<8; k++) {
									int new_ii = i + MEGA_DX[k];
									int new_jj = j + MEGA_DY[k];
									if (new_ii>=0 && new_ii<r && new_jj>=0 && new_jj<c)
										if (nnew[new_ii][new_jj])
											is_sos = 1;
								}
								if (!is_sos)
									is_cur_Ok = 0;
							}

					if (is_cur_Ok) {
						Ok = 1;
						break;
					}
				}
		}

		printf("Case #%d:\n",qq+1);
		if (!Ok) printf("Impossible\n");
		else
			for (int i=0; i<r; i++) {
				for (int j=0; j<c; j++) printf("%c",s[i][j]);
				printf("\n");
			}
	}

	return 0;
}