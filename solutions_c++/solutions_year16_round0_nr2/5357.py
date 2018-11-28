#include<iostream>
#include<cstring>
using namespace std;
int main()
{
	freopen("output.txt","w",stdout);
	freopen("B-large.in","r",stdin);
	int t,k;
	cin>>t;
	k=t;
	while(t--)
	{
		char a[105],ch;
		int ans=0,i;
		cin>>a;
		int l;
		l=strlen(a);
		if(l==1)
		{
			if(a[0]=='-')
			ans=1;
			else
			ans=0;
		}
		else
		{
			ch=a[0];
			i=1;
			while(a[i]!='\0')
			{
				if(a[i]!=ch)
				{
					ans++;
					ch=a[i];
				}
				i++;
			}
			if(a[l-1]=='-')
			ans++;
		}
		
		cout<<"Case #"<<k-t<<":"<<" "<<ans<<endl;
	}
	return 0;
}
