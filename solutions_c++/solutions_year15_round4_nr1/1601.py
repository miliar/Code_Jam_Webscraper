#include<bits/stdc++.h>

using namespace std;
const int INF = 99999999;

const int px[] = {1,0,-1,0};
const int py[] = {0,1,0,-1};

int R, C;
int T;
char m[200][200];
int ans;
int main() {
	freopen("A-large.in","r",stdin);
	freopen("a.txt","w",stdout);
	cin >> T;
	for (int cs = 1; cs <= T; ++cs) {
		ans = 0;
		cin >> R >> C;
		for (int i = 1; i <= R; ++i)
			cin >> (m[i] + 1);
		for (int i = 1; i <= R; ++i)
            for (int j = 1; j <= C; ++j)
                if (m[i][j] != '.') {
        			char c = m[i][j];
        			int dx = 0, dy = 0;
        			if (c == '^')
        				dx = -1, dy = 0;
        			if (c == '<')
        				dx = 0, dy = -1;
        			if (c == 'v')
        				dx = 1, dy = 0;
        			if (c == '>')
        				dx = 0, dy = 1;

					bool flag = false ;
					int cx = i + dx, cy = j + dy;
					for (;1 <= cx && cx <= R &&
							 1 <= cy && cy <= C;) {
						if (m[cx][cy] != '.') {
							flag = true; 
							break ;
						}
						cx += dx; cy += dy;
					}
					if (flag) continue ;
					++ans;
					flag = false ;
					for (int p = 0; p < 4; ++p) {
						cx = i + px[p];
						cy = j + py[p];
						for (;1 <= cy && cy <= C && 1 <= cx && cx <= R;) {
							if (m[cx][cy] != '.') {
								flag = true; 
								break ;
							}
							cx += px[p];
							cy += py[p];
						}
						if (flag) break ;
					}
					if (!flag) ans = INF;
				}
		cout << "Case #" << cs << ": ";

		if (ans >= INF)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << ans << endl;
	}
	return 0;
}

