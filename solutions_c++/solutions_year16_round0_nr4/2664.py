#include<bits/stdc++.h>

#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define PI 3.14159265359
#define endl '\n'

using namespace std;

int test;

int main()
{
	ios_base::sync_with_stdio(0);
	
	cin >> test;
	for(int te=1;te<=test;te++)
	{
		ll k,c,s;
		cin >> k >> c >> s;
		ll x = 1;
		for(int i=0;i<c-1;i++)
			x *= k;
		
		cout << "Case #" << te << ": ";
		for(int i=0;i<s;i++)
			cout << i*x+1 << " ";
		cout << endl;
	}
	
	return 0;
}