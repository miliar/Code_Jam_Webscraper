#include<bits/stdc++.h>
using namespace std;
int main()
{
freopen("0.in","r",stdin);
freopen("op.txt","w",stdout);
long long int t,i,l,ans;
char ch[10001];
cin>>t;
int cnt=1;
	while(cnt<=t)
	{
		ans=0;
		cin>>ch;
		l = strlen(ch);
		while(true)
		{
			i=0;
			if(ch[i]=='-')
			{
				while(ch[i]=='-' && i<l)
				{
					i++;
				}
				if(i==l)
				{
					ans+=1;
					break;
				}
				else
				{

					for(int r=0;r<i;r++)
						ch[r]='+';
					ans+=1;
				}

			}




			else if(ch[i]=='+')
			{
				while(ch[i]=='+' && i<l)
				{
					i++;
				}
				if(i==l)
				{
					break;
				}
				else
				{

					for(int r=0;r<i;r++)
						ch[r]='-';
					ans+=1;
				}
			}

		}
		cout<<"Case #"<<cnt<<": "<<ans<<endl;
		cnt++;
	}
	return 0;
}
