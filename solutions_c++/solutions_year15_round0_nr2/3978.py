#include <iostream>
using namespace std;

inline int min(const int &a, const int &b)
{return a<b?a:b;}

int main()
{
	ios_base::sync_with_stdio(0);
	int T;
	cin>>T;
	for (int t = 1; t <= T; ++t)
	{
		int d;
		cin>>d;
		int p[1003], ext, ans, max = 0;

		for (int i = 0; i < d; ++i)
		{
			cin>>p[i];
			if(max < p[i])
				max = p[i];
		}

		ans = max;
		for(int i = 1; i <= max; ++i)
		{
			int curr = i;
			for(int j = 0; j < d; ++j)
			{
				if(p[j] > i)
				{
					curr += p[j]/i;
					if(p[j]%i == 0)
						curr--;
				}
			}
			ans = min(ans, curr);
		}
		cout<<"Case #"<<t<<": "<<ans<<endl;
	}
	return 0;
}