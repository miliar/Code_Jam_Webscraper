#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
double a[1100],b[1100],copyb[1100],copya[1100];
bool vis[1100];
int T,n;
int main()
{
	fstream in("D-large.in");
	fstream out("ans.out");
	in>>T;
	for(int kcase=1;kcase<=T;kcase++)
	{
		in>>n;
		memset(vis,0,sizeof(vis));
		for(int i=0;i<n;i++)
			in>>a[i];
		for(int i=0;i<n;i++)
			in>>b[i];
		sort(a,a+n);
		sort(b,b+n);
		int cnt1,cnt2;
		cnt1=cnt2=0;
		for(int i=0;i<n;i++)
			for(int j=0;j<n;j++)
			{
				if(!vis[j]&&(b[j]>a[i]))
				{
					cnt2++;
					vis[j]=1;
					break;
				}
			}
		cnt2=n-cnt2;
		for(int i=0;i<n;i++)
			copyb[i]=b[i];
		for(int i=0;i<n;i++)
			copya[i]=a[i];
		a[n]=b[0];
		b[n]=a[n-1];
		sort(a,a+n+1);
		sort(b,b+n+1);
		int tmp=0;
		for(int i=0;i<=n;i++)
			if(a[i]==b[0])
				tmp=i;
		int ans1=0;
		for(int j=0;j<n;j++)
		{
			ans1=0;
			for(int i=tmp+j;i<n;i++)
				if(copya[i]>copyb[i-tmp-j])
						ans1++;
			cnt1=max(cnt1,ans1);
		}
		cout<<"Case #"<<kcase<<": "<<cnt1<<' '<<cnt2<<endl;
		out<<"Case #"<<kcase<<": "<<cnt1<<' '<<cnt2<<endl;
	}
}

			

