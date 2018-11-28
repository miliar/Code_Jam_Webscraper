#include<bits/stdc++.h>

using namespace std;

#define LL long long int
#define ULL unsigned long long
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
	int x,r,c;
	cin >> x >> r >> c;
	if(x == 1)
		cout << "GABRIEL" << endl;
	else if(x == 2)
	{
		if((r*c)%2 == 0)
			cout << "GABRIEL" << endl;
		else
			cout << "RICHARD" << endl;
	}
	if(x == 3)
	{
		if(r == 1 || c == 1)
			cout << "RICHARD" << endl;
		else if((r*c)%3 == 0)
			cout << "GABRIEL" << endl;
		else
			cout << "RICHARD" << endl;
	}
	if(x == 4)
	{
		if(r == 4 && c == 4)
			cout << "GABRIEL" << endl;
		else if(r == 3 && c == 4)
			cout << "GABRIEL" << endl;
		else if(r == 4 && c == 3)
			cout << "GABRIEL" << endl;
		else
			cout << "RICHARD" << endl;
	}
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