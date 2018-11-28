#include <iostream>
#include <string>
#include <iomanip>
#include <stdio.h>
#include <vector>
#include <map>
#include <sstream>
#include <algorithm>
using namespace std;

#define rep(i, n) for (int i = 0; i < n; ++i)
#define rep2(i, x, n) for (int i = x; i < n; ++i)
#define repd(i, n) for (int i = n - 1; i >= 0; --i)
#define repd2(i, x, n) for (int i = n - 1; i >= x; --i)
#define _(a, b) memset(a, b, sizeof(a))
int ri() { int a; scanf( "%d", &a ); return a; }
double rf() { double a; scanf( "%lf", &a ); return a; }
char sbuf[100005]; 
string rs() { scanf( "%s", sbuf ); return sbuf; }
long long rll() { long long a; scanf( "%lld", &a ); return a; }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;
typedef map<string,string> mss;

int main()
{
	freopen("C:\\Users\\Administrator\\Desktop\\B-large.in","rt",stdin);
	freopen("C:\\Users\\Administrator\\Desktop\\C-large-practice.out","wt",stdout);
	
	int T = ri();
	rep(t, T)
	{
		int row = ri();
		int col = ri();
		vector<vector<int>> v;
		rep(i, row) 
		{
			vector<int> c;
			rep(j, col)
				c.push_back(ri());
			v.push_back(c);
		}
		
		// row max
		vector<int> rowmax;
		vector<int> rowmin;
		rep(i, row)
		{
			rowmax.push_back(*(max_element(v[i].begin(), v[i].end())));
			rowmin.push_back(*(min_element(v[i].begin(), v[i].end())));
		}

		vector<int> colmax;
		vector<int> colmin;
		rep(j, col)
		{
			vector<int> temp;
			rep(i, row) temp.push_back(v[i][j]);
			colmax.push_back(*(max_element(temp.begin(), temp.end())));
			colmin.push_back(*(min_element(temp.begin(), temp.end())));
		}

		bool success = true;
		rep(i, row) rep(j, col)
		{
			if ((v[i][j] != rowmax[i] && v[i][j] != colmax[j]) ||
				v[i][j] < min(rowmin[i], colmin[j]))
			{
				success = false;
				goto pr;
			}
		}
pr:;
		printf("Case #%d: ", t+1);
		if (success)
			printf("YES\n");
		else
			printf("NO\n");
	}
	
	return 0;
}