#include <bits/stdc++.h>

using namespace std;

#define ll long long
#define all(v) v.begin(), v.end()
#define F first
#define S second
#define make0 memset(a,0,sizeof(a))
#define p push_back
#define fast_cin() ios_base::sync_with_stdio(false)
#define pi pair <int,int>
#define pll pair <ll,ll>

int main()
{
	fast_cin();
	int T;
	cin >> T;
	for(int f=1;f<=T;f++)
	{
		string s;
		int K;
		cin >> s;
		cin >> K;
		int N = s.size();
		int A[N];
		for(int i=0;i<N;i++)
		{
			if(s[i] == '-')
				A[i] = 0;
			else
				A[i] = 1;
		}
		int ans = 0;
		bool flag = true;
		cout << "Case #" << f << ": ";
		for(int i=0;i<N;i++)
		{
			if(A[i] == 0)
			{
				ans++;
				if(i + K > N)
				{
					flag = false;
					cout << "IMPOSSIBLE\n";
					break;
				}
				for(int j=i;j<i+K;j++)
					A[j] = !A[j];
			}
		}
		if(flag)
			cout << ans << endl;
	}
	return 0;
}