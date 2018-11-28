#include <cstdio>
#include <map>
#include <queue>
#include <string>
#include <algorithm>

using namespace std;

typedef pair<int, int> pii;

map<pii, int> m1;
map<pii, char> m2;
queue <int> q;
int t, x, y, tx, ty, ch;

string ans;

int main(){
	scanf("%d", &t);
	
	for (int Q = 0; Q < t; Q++){
		scanf("%d%d", &x, &y);
		
		m1.clear();
		m2.clear();
		while (!q.empty()) q.pop();
		
		m1[make_pair(0, 0)] = 0;
		q.push(1);
		q.push(0);
		q.push(0);
		
		while (!q.empty()){
			ch = q.front(); q.pop();
			tx = q.front(); q.pop();
			ty = q.front(); q.pop();
			
			//printf("%d %d  %d  %c\n", tx, ty, ch, m2[make_pair(tx,ty)]);
			
			if (tx == x && ty == y)
				break;
			
			if (!m1.count(make_pair(tx - ch, ty))){
				m1[make_pair(tx - ch, ty)] = m1[make_pair(tx, ty)] + 1;
				m2[make_pair(tx - ch, ty)] = 'W';
				
				q.push(ch + 1);
				q.push(tx - ch);
				q.push(ty);
			}
			if (!m1.count(make_pair(tx + ch, ty))){
				m1[make_pair(tx + ch, ty)] = m1[make_pair(tx, ty)] + 1;
				m2[make_pair(tx + ch, ty)] = 'E';
			
				q.push(ch + 1);
				q.push(tx + ch);
				q.push(ty);
			}
			
			if (!m1.count(make_pair(tx, ty + ch))){
				m1[make_pair(tx, ty + ch)] = m1[make_pair(tx, ty)] + 1;
				m2[make_pair(tx, ty + ch)] = 'N';
			
				q.push(ch + 1);
				q.push(tx);
				q.push(ty + ch);
			}
			if (!m1.count(make_pair(tx, ty - ch))){
				m1[make_pair(tx, ty - ch)] = m1[make_pair(tx, ty)] + 1;
				m2[make_pair(tx, ty - ch)] = 'S';
			
				q.push(ch + 1);
				q.push(tx);
				q.push(ty - ch);
			}
		}
		
		ans.clear();
		while (tx != 0 || ty != 0){
			ans.push_back(m2[make_pair(tx, ty)]);
			if(m2[make_pair(tx, ty)] == 'W')
				tx += --ch; else
			if(m2[make_pair(tx, ty)] == 'E')
				tx -= --ch; else
			if(m2[make_pair(tx, ty)] == 'N')
				ty -= --ch; else
			if(m2[make_pair(tx, ty)] == 'S')
				ty += --ch;
		}
		
		reverse(ans.begin(), ans.end());
		printf("Case #%d: %s\n", Q + 1, ans.c_str());
	}
}
