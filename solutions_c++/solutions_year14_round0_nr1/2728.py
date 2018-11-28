#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>

using namespace std;

int maze[5][5];
int vis[20];

int main () 
{
    freopen("1.txt", "r", stdin);	
	freopen("2.txt", "w", stdout);
    int cas, T;
	
	for (cas=scanf("%d", &T); cas<=T; cas++)
	{
        memset(vis, 0, sizeof(vis));
        
        int x, y;
        cin >> x;
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
                cin >> maze[i][j];

		for (int j=1; j<=4; j++) vis[maze[x][j]]++;
		
		cin >> y;
        for (int i=1; i<=4; i++)
            for (int j=1; j<=4; j++)
                cin >> maze[i][j];
		
		for (int j=1; j<=4; j++) vis[maze[y][j]]++;
		
		vector <int> ans;
        for (int i=1; i<=16; i++)  if (vis[i] == 2) ans.push_back(i);

        printf("Case #%d: ", cas);
        if (ans.size() == 0) puts("Volunteer cheated!");
        if (ans.size() == 1) cout << ans[0] << endl;
        if (ans.size() >= 2) puts("Bad magician!");
    }

    return 0;
}
