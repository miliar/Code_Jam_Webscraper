#include <iostream>
#include <set>
#define forn(i, n) for(int i = 0; i < int(n); i++)
using namespace std;
set<pair<int, pair<int, int> > > s;
bool row[100000], col[100000];
int main(){
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int tests;
	cin >> tests;
	forn(test, tests){
		int n, m;
		scanf("%d %d", &n, &m);
		s.clear(); 
		forn(i, n)
			forn(j, m){
				int x;
				scanf("%d", &x);
				s.insert(make_pair(-x, make_pair(i, j)));
			}
		forn(i, n)
			row[i] = false;
		forn(i, m)
			col[i] = false;
		bool good = true;
		for(set<pair<int, pair<int, int> > >::iterator it = s.begin(); it != s.end();){
			set<pair<int, pair<int, int> > >::iterator it1;
			for(it1 = it; it1 != s.end() && it1->first == it->first; it1++){
				int x = (*it1).second.first;
				int y = (*it1).second.second;
				if(row[x] && col[y])
					good = false;
			}
			for(it1 = it; it1 != s.end() && it1->first == it->first; it1++){
				int x = (*it1).second.first;
				int y = (*it1).second.second;
				row[x] = col[y] = true;
			}
			it = it1;

		}
		printf("Case #%d: ", test + 1);
		if(good){
			puts("YES");
		}else
			puts("NO");
	}
	return 0;
}