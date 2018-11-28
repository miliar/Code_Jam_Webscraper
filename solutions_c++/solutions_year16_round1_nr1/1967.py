#include<bits/stdc++.h>
#define ll  long long int
using namespace std;
int main (void)
{
	freopen("A-large.in","r",stdin);
	freopen("out60.out","w",stdout);
	int t,p;
	cin>>t;
	for( p=0;p<t;p++)
	{
		char c[1005];
		cin>>c;
		int l=strlen(c);
		int count=1;
		char res[1005];
		res[0]=c[0];
		for(int i=1;i<l;i++)
		{
			if(c[i]>=res[0])
			{
				int s=count;
				for(int j=s-1;j>=0;j--)
				{
					res[j+1]=res[j];
				}
				res[0]=c[i];
				count++;
			}
			else
			{
				res[i]=c[i];
				count++;
			}
		}
		cout<<"Case #"<<p+1<<": ";
		for(int i=0;i<l;i++)
		cout<<res[i];
		cout<<endl;
	}
}

