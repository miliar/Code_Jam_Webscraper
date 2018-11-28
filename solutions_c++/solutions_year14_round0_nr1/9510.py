/*#include <iostream>
#include <cstdio>
#include <ctime>
using namespace std;

int main() 
{
	const int bufferSize = 64;
    char buffer[bufferSize];
    size_t size;

    FILE* read = fopen("read.txt", "r + b");
	if (read == NULL)
	{
		cout << "READ ERROR!" << endl;
		return 0;
	}
	FILE* write = fopen("write.txt", "w + b");
	if (write == NULL)
	{
		cout << "WRITE ERROR!" << endl;
		return 0;
	}

	size = fread(buffer, 1, bufferSize, read);
	while (size > 0) {
        fwrite(buffer, 1, size, write);
		size = fread(buffer, 1, bufferSize, read);
    }

    fclose(read);
    fclose(write);
	return 0;
}*/

/*
#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;

int n;
const int MAXN = 5007;
vector< vector < int > > g;
vector<int> ans;
bool used[MAXN];
int timer, tin[MAXN], fup[MAXN];

int main()
{
	//freopen("points.in", "r", stdin);
	//freopen("points.out", "w", stdout);
	int i, j;
	cin >> n;
	double points[MAXN][MAXN];
	int a, b;
	for(i = 0; i < n; ++i)
	{
		cin >> points[i][0] >> points [i][1];
	}
	for(i = 0; i < n; ++i)
	{
		for(j = 0; j < n; ++j)
		{
			g[i].push_back;
		}
	}
	dfs(g[a][0],-1);
	if(ans.size() == 0)
	{
		cout << 0 << endl;
		return 0;
	}
	sort(ans.begin(), ans.end());
	int cnt = 1;
	for(i = 0; i < ans.size() - 1; ++i)
	{
		if(ans[i] == ans[i+1])
			ans[i] = -1;
		else
			++cnt;
	}
		cout << cnt << endl;
	for(i = 0; i < ans.size(); ++i)
	{
		if(ans[i] != -1)
			cout << ans[i] << " ";
	}

	return 0;
}
*/
/*
#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cmath>

using namespace std;

const double PI = acos(-1.0);

int mas[100007][11];

int main()
{
	int n, i, j, m, sum, a, l, index;
	string c;
	cin >> n >> m;
	cin >> c;
	l = c.size();

	
	for(i = 0; i < 10; ++i)
		mas[0][i] = 0;
	for(i = 1; i <= l; ++i)
	{
		for(j = 0; j < 10; ++j)
			mas[i][j] = mas[i - 1][j];
		++mas[i][(int)(c[i - 1] - '0')];
	}
	
	while(m > 0)
	{
		cin >> a;
		sum = 0;
		index = (int)(c[a - 1] - '0');
		for(i = 0; i < 10; ++i)
			sum += mas[a][i]*abs((double)index - (double)i);
		cout << sum << endl;
		--m;
	}
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
	
	//printf("%.8f %.8f %.8f\n", A, B, C-R);
	
    return 0;
}*/

#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	//freopen("output.txt", "w", stdout);
	int t;
	cin >> t;

	int a[5][5], b[5][5];
	int i, j, k;
	int first, second, cnt, ans;
	for(i = 0; i < t; ++i)
	{
		cnt = 0;
		cin >> first;
		for(j = 0; j < 4; ++j)
			for(k = 0; k < 4; ++k)
				cin >> a[j][k];

		cin >> second;
		for(j = 0; j < 4; ++j)
			for(k = 0; k < 4; ++k)
				cin >> b[j][k];
		
		for(j = 0; j < 4; ++j)
			for(k = 0; k < 4; ++k)
				if(a[first-1][j] == b[second-1][k])
				{
					++cnt;
					ans = a[first-1][j];
				}
		cout << "Case #" << i + 1 << ": ";
		if(cnt == 1)
			cout << ans << endl;
		if(cnt == 0)
			cout << "Volunteer cheated!" << endl;
		if(cnt > 1)
			cout << "Bad magician!" << endl;
	}
}