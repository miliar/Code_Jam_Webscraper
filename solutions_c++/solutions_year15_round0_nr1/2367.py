#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen("input.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int t;
	cin>>t;
	for(int T=0;T<t;T++)
	{
		char a[2000];
		int n;
		cin>>n;
		scanf("%s",a);
		int cur=0,p=0;
		for(int i=0;i<=n;i++)
		{
			int z=a[i]-'0';
			while(p<i&&z>0)
			{
				cur++;p++;
			}
			p+=z;
		}
		cout<<"Case #"<<T+1<<": "<<cur<<endl;
	}
	return 0;
}