#include <iostream>
using namespace std;

int main()
{
	freopen("test.in", "r", stdin);
	freopen("test.out", "w", stdout);

	int T;
	cin>>T;
	for (int TT = 1; TT < T+1; TT++)
	{
		int k,c,s;
		cin >> k >> c >> s;
		cout << "Case #" << TT << ":" ;
		for (int i = 0; i < k; i++)
		{
			cout << ' ' << i+1;
 		}
 		cout << endl;
	}
	return 0;
}