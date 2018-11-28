#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
ifstream cin("A-large.in");
ofstream cout("out.txt");

int a[10005],n,cap;

int main()
{
	int t,i,j,k,count=0,ans;
	cin>>t;
	while (t--)
	{
		count++;
		cin>>n>>cap;
		for (i=1;i<=n;i++)
			cin>>a[i];
		sort(a+1,a+n+1);
		i=1;
		j=n;
		ans=0;
		while (i<=n)
		{
			if (a[i]==-1)
			{
				i++;
				continue;
			}
			ans++;
			while (j>i&&a[i]+a[j]>cap) j--;
			if (j>i)
			{
				a[j]=-1;
				j--;
			}
			i++;
		}
		cout<<"Case #"<<count<<": "<<ans<<endl;
	}
	return 0;
}