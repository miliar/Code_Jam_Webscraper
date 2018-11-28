#include "bits/stdc++.h"
#define int long long
using namespace std;

signed main()
{
	int t; cin >> t;
	for (int tc=1; tc<=t; tc++)
	{
		int n; cin >> n;
		if (not n)
		{
			cout << "Case #" << tc << ": INSOMNIA\n";
			continue;
		}
		int ar[10];
		for (int i=0;i<10;i++)
		ar[i]=0;
		int flag=0, s=1, f;
		while (not flag)
		{
			int temp=s*n, sum=0; f=temp;
			s++;
			while(temp) ar[temp%10]=1, temp/=10;
			for (int i=0; i<=9; i++) if(ar[i]==1) sum++;
			if (sum==10) flag=1;
		}
		cout << "Case #" << tc << ": " << f << '\n';
	}
}
