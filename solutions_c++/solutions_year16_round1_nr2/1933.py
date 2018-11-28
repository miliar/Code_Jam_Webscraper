#include <iostream> 
#include <cstdio> 
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
int main()
{
	freopen("B-large .in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		int n;
		cin >> n;
		int y = (2 * n-1)*n;
		vector<int>sold(y,0);
		vector<int>fs(2501);
		for (int j = 0; j < y;j++)
		{
			cin >> sold[j];
			fs[sold[j]]++;
		}
		vector<int>ans;
		for (int j = 0; j < 2501; j++)
		{
			if ((fs[j] != 0) && (fs[j] % 2 == 1))
			{
			ans.push_back(j);
			}
		}
		sort(ans.begin(), ans.end());
		cout << "Case #" << i + 1 << ": ";
		for (int k = 0; k < ans.size(); k++)
		{
			cout << ans[k] << " ";
		}
		cout << endl;
	}
	return 0;
}
