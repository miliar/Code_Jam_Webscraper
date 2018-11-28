#include <stdio.h>
#include <iostream>
#include <vector>
#include <cmath>

using namespace std;


int main()
{
	int T;
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>T;
	for (int i = 0; i < T; ++i)
	{
		bool ans = true;
		int n, m;
		cin>>n>>m;
		vector<vector<int>> arr(n);
		for (int j = 0; j < n; ++j)
		{
			arr[j].resize(m);
			for (int k = 0; k < m; ++k)
			{
				cin>>arr[j][k];
			}
		}
		vector<int> maxN(n), maxM(m);
		for (int j = 0; j < n; ++j)
		{			
			for (int k = 0; k < m; ++k)
			{
				maxN[j] = max(maxN[j], arr[j][k]);
				maxM[k] = max(maxM[k], arr[j][k]);
				
			}
		}
		for (int j = 0; j < n && ans == true; ++j)
		{			
			for (int k = 0; k < m; ++k)
			{
				if (arr[j][k] != maxN[j] && arr[j][k] != maxM[k])
				{
					ans = false;
					break;
				}
				
			}
		}


		cout<<"Case #"<<i+1<<": ";
		if (true == ans)
			cout<<"YES";
		else
			cout<<"NO";
		cout<<endl;
	}



	return 0;
}