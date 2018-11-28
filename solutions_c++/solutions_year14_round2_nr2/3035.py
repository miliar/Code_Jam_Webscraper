#include <iostream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	cin >> t;
	for (int w = 0; w < t; w++)
	{
		int a,b,k;
		cin >> a >> b >> k;
		int ans = 0;
		for (int i = 0; i < b; i++)
		{
			for (int j = 0; j < a; j++)
			{
				if ((i & j) < k)
				{
					ans++;
				}
			}
		}
		cout << "Case #" << w + 1 << ": " << ans << endl;
	}
	return 0;
}
