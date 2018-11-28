#include<iostream>
#include<algorithm>
using namespace std;

double a[1005], b[1005];

int main()
{
	freopen("d:\\4.in", "r", stdin);
	freopen("d:\\4-out.txt", "w", stdout);
	
	int T;
	cin>>T;
	for(int kase = 1; kase <= T; ++kase)
	{
		int n;
		cin>>n;
		for(int i = 0; i < n; ++i)
			cin>>a[i];
		for(int i = 0; i < n; ++i)
			cin>>b[i];
		sort(a, a+n);
		sort(b, b+n);
		
		int i = 0, j = 0;	
		int ans1 = 0, ans2 = 0;
		for(i = 0; i < n; ++i)
		{
			while(j<n && a[i] > b[j])
				j++;
			if(j < n && a[i] < b[j])
			{
				ans1++;
				j++;
			}
		}
		ans1 = n - ans1;
		i = 0;
		for(j = 0; j < n; ++j)
		{
			while(i < n && a[i] < b[j])
				i++;
			if(i < n)
			{
				ans2++;
				i++;
			}
		}
		
		cout<<"Case #"<<kase<<": "<<ans2<<" "<<ans1<<endl;
	}
	return 0;
}
