#include <iostream>
#include <algorithm>
using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	for(int t = 1; t <= T; ++t)
	{
		int n;
		cin>>n;
		int m[n];
		for(int i = 0; i < n; ++i)
			cin>>m[i];
		int a1 = 0,a2 = 0, mx = 0;
		for(int i = 0; i < n-1; ++i)
		{
			if(m[i] > m[i+1])
				a1 += m[i]-m[i+1];
			mx = max(mx, m[i]-m[i+1]);
		}

		for(int i = 0; i < n-1; ++i)
		{
			if(m[i] >= mx)
				a2 += mx;
			else
				a2 += m[i];
		}
		cout<<"Case #"<<t<<": "<<a1<<" "<<a2<<endl;
	}
	return 0;
}