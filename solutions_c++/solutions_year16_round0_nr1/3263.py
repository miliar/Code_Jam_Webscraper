#include<bits/stdc++.h>

#define ll long long
#define ld long double
#define pb push_back
#define mp make_pair
#define PI 3.14159265359
#define endl '\n'

using namespace std;

ll test,n;
bool t[10];
string s;

int main()
{
	ios_base::sync_with_stdio(0);
	
	cin >> test;
	for(int te=1;te<=test;te++)
	{
		cin >> n;
		for(int i=0;i<10;i++)
			t[i] = 0;
		ll ans,lim = 1000000*n;
		for(ans=n;ans<lim;ans+=n)
		{
			stringstream ss;
			ss << ans;
			ss >> s;
			for(char c : s)
				t[c - '0'] = 1;
			bool b = 1;
			for(int i=0;i<10;i++)
				if(!t[i])
				{
					b = 0;
					break;
				}
// 			cout << ans << endl;
			if(b)
				break;
		}
		bool bo = 1;
		for(int i=0;i<10;i++)
			if(!t[i])
				bo = 0;
		cout << "Case #" << te << ": ";
		if(bo)
			cout << ans;
		else
			cout << "INSOMNIA";
		cout << endl;
	}
	return 0;
}