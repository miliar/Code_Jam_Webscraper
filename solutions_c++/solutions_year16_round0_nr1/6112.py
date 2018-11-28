#include<bits/stdc++.h>

using namespace std;
int a[12],ans,tmp,n;
int main(void)
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	cin>>T;
	for(int tt=1;tt<=T;tt++)
	{
		cout<<"Case #"<<tt<<": ";
		cin>>n;
		if(n==0)
		{
			cout<<"INSOMNIA";
		}
		else
		{
			for(int i=1;i<1000;i++)
			{
				int nn=n*i;
				tmp=nn;
				//scout<<tmp;
				while(tmp)
				{
					a[tmp%10]=1;
					tmp=tmp/10;
				}
				for(int k=0;k<10;k++)
				{
					ans+=a[k];
				}
				//cout<<ans<<endl;
				if(ans==10)
				{
					cout<<nn;
					break;
				}
				ans=0;
			}
		}
				for(int k=0;k<10;k++)
				{
					a[k]=0;
				}
		cout<<endl;
	}

	return 0;
}
