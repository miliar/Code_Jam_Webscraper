#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
using namespace std;

int main() {
	freopen("in.in","r",stdin);
	freopen("out.out","w",stdout);
	int TEST = 1,T;
	cin >> T;
	while(T--)
	{
		vector<int> ans;
		int vis[16];
		for(int i = 0; i < 16; i++)
			vis[i] = 0;
		for(int k = 0 ; k < 2; k++)
		{
			int a,t;
			cin >> a;
			for(int i = 0 ; i < 4; ++i)
				for(int j = 0 ; j < 4; j++)
				{
					cin >> t;
					if(i == a - 1)
						vis[t - 1]++;
				}
		}
		for(int i = 0 ; i < 16; i++)
			if(vis[i] == 2)
				ans.push_back(i);
		cout << "Case #"<<TEST++<<": ";
		if(ans.size() == 1)
			cout << ans[0] + 1 << endl;
		else if(ans.size() > 1)
			cout << "Bad magician!" << endl;
		else
			cout << "Volunteer cheated!" << endl;
	}
	return 0;
}
