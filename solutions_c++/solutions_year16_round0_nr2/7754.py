#include <bits/stdc++.h>

using namespace std;

#define LL long long int
#define sd(x) scanf("%d", &x)
#define MP make_pair
#define PB push_back
#define vi vector<int> 
#define pii pair<int,int>
#define F first
#define S second
#define D double
#define LD long double

inline void solve()
{
	string order;
	cin >> order;

	vector<int> happyUp(110, 0), blankUp(110, 0);

	for(int i = 0; i < order.size(); i++)
	{
		if(order[i] == '+')
		{
			happyUp[i+1] = min(happyUp[i], blankUp[i] + 1);
			blankUp[i+1] = min(happyUp[i] + 1, blankUp[i] + 2);
		}
		else if(order[i] == '-')
		{
			blankUp[i+1] = min(blankUp[i], happyUp[i] + 1);
			happyUp[i+1] = min(blankUp[i] + 1, happyUp[i] + 2);
		}
	}
	cout << happyUp[order.length()] << endl;
}

int main()
{
	int t, i;
	sd(t);
	for(i = 1; i <= t; i++)
	{
		printf("Case #%d: ", i);
		solve();
	}
    return 0;
}