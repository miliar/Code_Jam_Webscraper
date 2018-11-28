#include <cstdio>
#include <queue>
#include <string>
#include <map>
using namespace std;
struct Pos{
	int x, y;
	string path;
	int currentMove;
	Pos(){x = y = 0; path = ""; currentMove = 0;}
	Pos(int cx, int cy, string p, int cm) { x = cx; y = cy; path = p; currentMove = cm; }
};
typedef pair<int,int> pii;
typedef map<pii, Pos>::iterator iter;

map<pii, Pos > mp;
int main() {
	int tc, x, y;
	scanf("%d", &tc);
	queue<Pos> q;
	q.push(Pos());
	const int dir[][2] = { {1,0}, {0,1}, {0,-1}, {-1,0}};
	const char *move = "ENSW";
	for(int cs=1; cs<=tc; cs++) {
		printf("Case #%d: ", cs);
		scanf("%d %d", &x, &y);
		pii pi = make_pair(x, y);
		iter curr = mp.find(pi);
		while(curr == mp.end()) {
			if(!q.empty()) {
				Pos p = q.front();
				q.pop();
				int nm = p.currentMove + 1;
				for(int i=0; i<4; i++) {
					int nx = p.x + dir[i][0] * nm;
					int ny = p.y + dir[i][1] * nm;
					if(nx >=-500 && nx <= 500 && ny >= -500 && ny <= 500) {
						pii cpi = make_pair(nx, ny);
						iter cp = mp.find(cpi);
						if(cp == mp.end() || cp->second.path.length() > p.path.length() + 1) {
							Pos next(nx, ny, p.path + move[i], nm);
							mp[cpi] = next;
							q.push(next);
						}
					}
				}
				curr = mp.find(pi);			
			} else break;
		}
		printf("%s\n", curr->second.path.c_str());
	}
	return 0;
}
