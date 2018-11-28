#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<vector>
#include<string>
#include<stack>
using namespace std;

int calc(int num)
{
	int ans = 0;
	while(num)
	{
		num--;
		num /= 2;
		ans++;
	}
	return ans;
}
long long T,N,P;
int tobin(int x)
{
	int ans = 0;
	int n = 1;
	for(int i = N - 1 ; i >= 0; i--)
	{
		if(i < x)
			ans += n;
		n *= 2;
	}
	return ans;
}

int tobin2(int x)
{
	int ans = 0;
	int n = 1;
	for(int i = 0; i < N - x; i++)
	{
		ans += n;
		n *= 2;
	}
	return ans;
}

int main()
{
	freopen("text.txt","r",stdin);
	freopen("sol.txt","w",stdout);
	cin >> T;
	for(long long TEST = 1 ; TEST <= T; TEST++)
	{
		cin >> N >> P;
		int ans1 = 0,ans2 = 0;
		for(int i = 1 ; i < (1<<N); i++)
		{
			int num = calc(i);
			num = tobin(num);
			if(num < P)
				ans1 = i;

			num = calc((1<<N) - i - 1);
			num = tobin2(num);
			if(num < P)
				ans2 = i;
		}

		cout << "Case #"<<TEST<<": " << ans1 << " " << ans2 << endl;
	}
}
