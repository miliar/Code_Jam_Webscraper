#include <bits/stdc++.h>

#define ll long long
#define ff first
#define ss second
#define mp make_pair

using namespace std;

typedef pair < ll , ll > pie;

bool s[10];
void sbool()
{
	for(int i = 0; i < 10; i++)
		s[i] = false;
	return;
}
bool isbool()
{
	for(int i = 0; i < 10; i++)
		if(!s[i])
			return false;
	return true;
}
void ssbool(ll l)
{
	do
	{
		s[l%10] = true;
		l /= 10;
	}
	while(l > 0);
	return;
}
int main()
{
	ios_base::sync_with_stdio(false);
	int T,N;
	cin >> T;
	for(int k = 1; k <= T; k++)
	{
		cin >> N;
		bool shit = false;
		ll t = N;
		sbool();
		for(int j = 1; j < 100; j++)
		{
			ssbool(t * j);
			if(isbool())
			{
				shit = true;
				cout << "Case #" << k << ": " << t*j << endl;
				break;
			}
		}
		if(!shit)
			cout << "Case #" << k << ": INSOMNIA" << endl;
	}
	// bool shit;
	// for(int i = 0; i <= 1e6; i++)
	// {
	// 	ll t = i;
	// 	sbool();
	// 	shit = false;
	// 	for(int j = 0; j < 100; j++)
	// 	{
	// 		ssbool(t * j);
	// 		if(isbool())
	// 		{
	// 			shit = true;
	// 			break;
	// 		}
	// 	}
	// 	if(!shit)
	// 	{
	// 		cout<<i<<endl;
	// 	}
	// }
	return 0;
}