#include <bits/stdc++.h>

using namespace std;

int main()
{
	ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);
	freopen("A-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	long long t, n, a[10], m ,k;
	cin >> t;
	for(int i=0;i<t;i++)
	{
		cin >> n;
		if(n==0)
		{
			cout << "Case #" << i+1 << ": INSOMNIA\n";
			continue;
		}
		for(int j=0;j<10;j++)
			a[j]=0;
		bool f=false;
		k=0;
		while(!f)
		{
			f=true;
			k++;
			m=n*k;
			while(m!=0)
			{
				a[m%10]++;
				m=m/10;
			}
			for(int j=0;j<10;j++)
			{
				if(a[j]==0)
				{
					f=false;
					break;
				}
			}
		}
		cout << "Case #" << i+1 << ": " << n*k << "\n";
	}
}
