#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cmath>
using namespace std;

const int di[] = {-1, 0, 1, 0}, dj[] = {0, 1, 0, -1};
int R, C;
string a[105];

bool out(int i, int j, int dir)
{
	do {
		i += di[dir];
		j += dj[dir];
		if (i < 0 || i >= R || j < 0 || j >= C)
			return true;
		if (a[i][j] != '.')
			return false;
	}while (true);
	return false;
}

void work()
{	
	int ans = 0;	
	cin >> R >> C;
	for (int i = 0; i < R; ++i)
		cin >> a[i];	
	for (int i = 0; i < R; ++i)
		for (int j = 0; j < C; ++j) {
			int dir = -1;
			switch (a[i][j]) {
			case '^':
				dir = 0;
				break;
			case '>':
				dir = 1;
				break;
			case 'v':
				dir = 2;
				break;
			case '<':
				dir = 3;
				break;
			}
			if (dir == -1)
				continue;
			if (out(i, j, dir)) {
				bool flag = false;
				for (int d = 0; d < 4; ++d)
					if (d != dir && !out(i, j, d))  {
						flag = true;
						break;
					}
				if (flag)
					++ans;
				else {
					cout << "IMPOSSIBLE" << endl;
					return;
				}				
			}				
		}				
	cout << ans << endl;
}

int main()
{
    freopen("a2.in", "r", stdin);
    freopen("a2.out", "w", stdout);

    int t2;
    cin >> t2;
    for (int t1 = 1; t1 <= t2; ++t1) {
        printf("Case #%d: ", t1);        
        work();
    }
    
    return 0;
}

