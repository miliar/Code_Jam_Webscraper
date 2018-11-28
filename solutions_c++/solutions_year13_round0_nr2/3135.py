#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>

using namespace std;

bool Judge(vector<vector<int> >& p)
{
    int n = p.size();
    for(int i = 0; i < n; ++i)
    {
	int m = p[i].size();
	int max = -1;
	for(int j = 0; j < m; ++j)
	    if(max < p[i][j])
		max = p[i][j];
	for(int j = 0; j < m; ++j)
	    if(p[i][j] != max)
	    {
		for(int row = 0; row < n; ++row)
		{
		    if(p[i][j] < p[row][j])
			return false;
		}
	    }
    }
    return true;
}
int main()
{
    int T;
    cin >> T;
    for(int iCase = 1; iCase <= T; ++iCase)
    {
	int n, m;
	cin >> n >> m;

	vector<vector<int> > pattern(n);
	int a; 
	for(int i = 0; i < n; ++i)
	    for(int j = 0; j < m; ++j)
	    {
		cin >> a;
		pattern[i].push_back(a);
	    }
	bool ans = Judge(pattern);
	cout << "Case #" << iCase << ": ";
	if( ans )
	    cout << "YES";
	else cout << "NO";
	cout << endl;
    }
}
