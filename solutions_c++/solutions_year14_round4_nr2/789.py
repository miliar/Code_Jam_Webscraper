#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
ifstream cin("B-large.in");
ofstream cout("out.txt");

int a[1005],n,b[1005];

int asc(int st, int ed)
{
	if (st>=ed) return 0;
	int i,j,k,rtn=0;
	for (i=ed-1;i>=st;i--)
		for (j=i;j<ed;j++)
			if (a[j]>a[j+1])
			{
				k=a[j];
				a[j]=a[j+1];
				a[j+1]=k;
				rtn++;
			}
	return rtn;
}

int desc(int st, int ed)
{
	if (st>=ed) return 0;
	int i,j,k,rtn=0;
	for (i=ed-1;i>=st;i--)
		for (j=i;j<ed;j++)
			if (a[j]<a[j+1])
			{
				k=a[j];
				a[j]=a[j+1];
				a[j+1]=k;
				rtn++;
			}
	return rtn;
}

int main()
{
	int t,i,j,k,count=0,ans,pos;
	int l,r;
	cin>>t;
	while (t--)
	{
		ans=0;
		count++;
		cin>>n;
		for (i=1;i<=n;i++)
			cin>>b[i];
		for (i=1;i<=n;i++)
			a[i]=b[i];
		sort(b+1,b+n+1);
		l=1;
		r=1;
		for (i=1;i<=n;i++)
		{
			for (j=1;j<=n;j++)
				if (a[j]==b[i])
				{
					pos=j;
					break;
				}
			if (pos-l<=n-r+1-pos)
			{
				while (pos!=l)
				{
					swap(a[pos],a[pos-1]);
					pos--;
					ans++;
				}
				l++;
			}
			else
			{
				while (pos!=n-r+1)
				{
					swap(a[pos],a[pos+1]);
					pos++;
					ans++;
				}
				r++;
			}
		}
		cout<<"Case #"<<count<<": "<<ans<<endl;
	}
	return 0;
}