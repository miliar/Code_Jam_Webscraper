	#include <cstdio>
    #include <cstdlib>
    #include <iostream>
    #include <vector>
    #include <map>
    #include <set>
    #include <algorithm>
    #include <string>
    #include <cstring>
    #include <queue>
    #include <cmath>
    #include <ctime>
    

    using namespace std;

    typedef long long i64;
    typedef vector<int> vi;
    typedef vector<vi> vvi;
    typedef pair<int, int> pii;

    const double eps = 10e-9;
    const int MOD = 1000000007;
    const int INF = MOD;
    
	int a[100][100];
	int column[100];
	int row[100];
	int main()
    {
//      std::ios_base::sync_with_stdio(false);
		freopen("input.txt", "r", stdin);
		freopen("output.txt", "w", stdout);
		int t;
		cin >> t;
		for(int tcase = 1; tcase <= t; tcase++)
		{
			int n, m;
			cin >> n >> m;
			bool possible = true;
			for(int i = 0; i < n; i++)
				for(int j = 0; j < m; j++)
					cin >> a[i][j];
			for(int i = 0; i < n; i++)
				row[i] = *max_element(a[i], a[i] + m);
			for(int j = 0; j < m; j++)
			{
				column[j] = a[0][j];
				for(int i = 1; i < n; i++)
					column[j] = max(column[j], a[i][j]);
			}
			for(int i = 0; i < n; i++)
				for(int j = 0; j < m; j++)
					if(a[i][j] < row[i] && a[i][j] < column[j])
						possible = false;
			cout << "Case #" << tcase << ": ";
			cout << (possible ? "YES" : "NO");
			cout << endl;
		}
        //cerr << "Time -- " << clock() - t << endl;
        //system("PAUSE");
        return 0;
	}
	