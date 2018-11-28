#include<iostream>
#include<string>
using namespace std;
const int mN=110;
int a[mN][mN],mx[mN],my[mN];
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("large.out","w",stdout);
	int T;
	cin>>T;
	for (int tT=1;tT<=T;tT++)
	{
		int n,m;
		cin>>n>>m;
		memset(mx,0,sizeof(mx));
		memset(my,0,sizeof(my));
		for (int i=0;i<n;i++)
		{
			for (int j=0;j<m;j++)
			{
				cin>>a[i][j];
				mx[i]=max(mx[i],a[i][j]);
				my[j]=max(my[j],a[i][j]);
			}
		}
		string ans="YES";
		for (int i=0;i<n;i++)
			for (int j=0;j<m;j++)
				if (a[i][j]!=min(mx[i],my[j]))
					ans="NO";
		printf("Case #%d: %s\n",tT,ans.c_str());
	}
}
