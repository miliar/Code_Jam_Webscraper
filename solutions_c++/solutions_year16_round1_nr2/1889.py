#include <iostream>
#include <string.h>
#include <cstdio>
#include <stack>
#include <string>
#include <algorithm>
using namespace std;
#define M 105
#define LL long long 
#define BB
int c,n,m,kk;
int s[200][55],d[2550],ans[2505];
int main()
{
#ifdef BB	
	freopen("E:\\22.in","r",stdin);
	freopen("E:\\22.out","w",stdout);
#endif
	int cc=1;
	cin>>c;
	while (c--)
	{
		cin>>n;
		memset(ans,0,sizeof(ans));
		memset(d,0,sizeof(d));
			for (int i=0;i<2*n-1;i++)
				for (int j=0;j<n;j++)
				{
					cin>>kk;
					d[kk]++;
				}
			int pos=0;
			for (int i=1;i<2501;i++)
			{
				if (d[i]%2==1)
					ans[pos++]=i;
			}
			sort(ans,ans+pos);
			cout<<"Case #"<<cc++<<": ";
			for (int i=0;i<pos;i++)
			{
				cout<<ans[i];	
				if (i<pos-1)
					cout<<" ";
				else
					cout<<endl;
			}
	}
#ifdef BB
	fclose(stdin);
	fclose(stdout);
#endif
	return 0;
}
