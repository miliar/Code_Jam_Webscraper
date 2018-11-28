#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	cin>>t;
	int tc=t;
	while(t--)
	{
		int n,i,j,lj;
		cin>>n;
		int ans1=0,ans2=0;
		double a[n],b[n];
		for(int i=0;i<n;i++)
			cin>>a[i];
		for(int i=0;i<n;i++)
			cin>>b[i];
		i=0,j=0;
		sort(a,a + n);
		sort(b,b + n);
		for(int m=0;m<n;m++)
		{
			if(j>=n)
			{
				break;
			}
			if(a[i]<b[j])
			{
				i++,j++;
			}
			else
				j++;
		}
		ans1=n-i;
		i=0,j=0,lj=n-1;
		for(int m=0;m<n;m++)
		{
			if(a[i]>b[j])
			{
				ans2++;
				i++,j++;
			}
			else
			{
				b[lj]=1.9;
				lj--;
				i++;
			}
		}
		cout<<"Case #"<<tc-t<<": "<<ans2<<" "<<ans1<<endl;
	}
	return 0;
}