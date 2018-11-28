#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
	freopen("A-large.in", "r", stdin);
//	freopen("A-small-attempt2.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int n, t, w;
	cin >> n;
	map <char, int> a;
	string s;
	char ans[1000];
	for(int q=0;q<n;q++)
	{
		t=0;
		cout << "Case #" << q+1 << ": ";
		cin >> s;
		w=s.length();
		for(int i=0;i<w;i++)
		{
			a[s[i]]++;
		}
		while(a['Z']>0)
		{
			a['Z']--;
			a['E']--;
			a['R']--;
			a['O']--;
			w-=4;
			ans[t]='0';
			t++;
		}
		while(a['W']>0)
		{
			a['T']--;
			a['W']--;
			a['O']--;
			w-=3;
			ans[t]='2';
			t++;
		}
		while(a['U']>0)
		{
			a['F']--;
			a['O']--;
			a['U']--;
			a['R']--;
			w-=4;
			ans[t]='4';
			t++;
		}
		while(a['X']>0)
		{
			a['S']--;
			a['I']--;
			a['X']--;
			w-=3;
			ans[t]='6';
			t++;
		}
		while(a['G']>0)
		{
			a['E']--;
			a['I']--;
			a['G']--;
			a['H']--;
			a['T']--;
			w-=5;
			ans[t]='8';
			t++;
		}
		while(a['R']>0)
		{
			a['T']--;
			a['H']--;
			a['R']--;
			a['E']--;
			a['E']--;
			w-=5;
			ans[t]='3';
			t++;
		}
		while(a['O']>0)
		{
			a['O']--;
			a['N']--;
			a['E']--;
			w-=3;
			ans[t]='1';
			t++;
		}
		while(a['F']>0)
		{
			a['F']--;
			a['I']--;
			a['V']--;
			a['E']--;
			w-=4;
			ans[t]='5';
			t++;
		}
		while(a['S']>0)
		{
			a['S']--;
			a['E']--;
			a['V']--;
			a['E']--;
			a['N']--;
			w-=5;
			ans[t]='7';
			t++;
		}
		while(a['N']>0)
		{
			a['N']--;
			a['I']--;
			a['N']--;
			a['E']--;
			w-=4;
			ans[t]='9';
			t++;
		}
		sort(ans, ans+t);
		for(int i=0;i<t;i++)
		{
			cout << ans[i];
		}
		cout << "\n";
	}
}
