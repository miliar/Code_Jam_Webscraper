#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
	freopen("A-large.in", "r", stdin);
//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-out.txt", "w", stdout);
	freopen("A-large-out.txt", "w", stdout);
	int w;
	cin >> w;
	for(int q=0;q<w;q++)
	{
		cout << "Case #" << q+1 << ": ";
		int n, a[26], k, m, x;
		string e;
		e="ABCDEFGHIJKLMNOPQRSTUVWXYZ";
		cin >> n;
		k=0, m=0, x=0;
		for(int i=0;i<n;i++)
		{
			cin >> a[i];
			k+=a[i];
		}
		while(k>3)
		{
			m=0;
			for(int i=0;i<n;i++)
			{
				if(a[i]>m)
				{
					m=a[i];
					x=i;
				}
			}
			a[x]--;
			cout << e[x];
			k--;
			m=0;
			for(int i=0;i<n;i++)
			{
				if(a[i]>m)
				{
					m=a[i];
					x=i;
				}
			}
			a[x]--;
			cout << e[x] << " ";
			k--;
		}
		if(k==2)
		{
			for(int i=0;i<n;i++)
			{
				if(a[i]!=0)
					cout << e[i];
			}
		}
		else
		{
			bool f=false;
			for(int i=0;i<n;i++)
			{
				if(a[i]!=0&&!f)
				{
					f=true;
					cout << e[i] << " ";
				}
				else if(a[i]!=0&&f)
				{
					cout << e[i];
				}
			}
		}
		cout << "\n";
	}
}
