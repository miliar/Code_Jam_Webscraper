#include<bits/stdc++.h>
#define ll  long long int
using namespace std;
int main (void)
{	
    freopen("A-large.in","r",stdin);
   	freopen("outohbabyatriple.out","w",stdout);
	int test,x;
	cin>>test;
	for( x=0;x<test;x++)
	{
		char ch[1005];
		cin>>ch;
		int l=strlen(ch);
		int cnt=1;
		char result[1005];
		result[0]=ch[0];
		for(int i=1;i<l;i++)
		{
			if(ch[i]>=result[0])
			{
				int s=cnt;
				for(int j=s-1;j>=0;j--)
				{
					result[j+1]=result[j];
				}
				result[0]=ch[i];
				cnt++;
			}
			else
			{
				result[i]=ch[i];
				cnt++;
			}
		}
		cout<<"Case #"<<x+1<<": ";
		for(int i=0;i<l;i++)
		cout<<result[i];
		cout<<endl;
	}
}
