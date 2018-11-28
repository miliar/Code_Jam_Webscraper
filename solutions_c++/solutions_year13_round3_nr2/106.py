#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
using namespace std; 
 
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int dx[] = {1, -1, 0, 0};
	int dy[] = {0, 0, 1, -1};
	int d[] = { 'W', 'E', 'S', 'N' };

	int n, T;
	cin >> T;
	pair<int, int> start(0, 0);
	for (int t = 1; t <= T; t++)
	{
        int x, y;
        cin >> x >> y;

        int l = 0;
        string path;

        while(true)
		{
            path.clear();
            l++;
            int h = l;
            pair<int, int> g(x,y);
            while(h > 0)
			{
                int mnum = 0, mval = 1e8;
                for (int i = 0; i < 4; i++)
				{
                    pair<int, int> z = g;
                    z.first += dx[i] * h;
                    z.second += dy[i] * h;
                    if(abs(z.first) + abs(z.second) < mval)
					{
						mval = abs(z.first) + abs(z.second);
						mnum = i;
                    }
                }

				path.push_back(d[mnum]);

                pair<int, int> z = g;
                z.first += dx[mnum] * h;
                z.second += dy[mnum] * h;
                g = z;
                h--;
            }

            if (g == start)
				break;
        }

        reverse(path.begin(), path.end());
		cout << "Case #" << t << ": " << path << endl;
	}
	return 0;
}