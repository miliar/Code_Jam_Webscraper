#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	string s;
	int cnt=1;
	while(t--)
	{
		cin>>s;
		int f=0,l=0,len=2*s.length()+1;
		int k=s.length();
		f=k;

		char ch[len+1];
		for(int i=0 ; i<len+1 ; ++i)
			ch[i]='*';
		for(int i=0 ; i<s.length() ; ++i)
		{
			if(i==0)
			{
				f=l=k;
				ch[k]=s[0];	
			}
			else if(i==1)
			{
				if(s[i]>s[i-1])
				{
					--f;
					ch[f]=s[i];
				}
				else
				{
					l++;
					ch[l]=s[i];
				}
			}
			else
			{
				if(s[i]>=ch[f])
				{
					f--;
					ch[f]=s[i];
				}
				else
				{
					l++;
					ch[l]=s[i];
				}
			}
		}
		printf("Case #%d: ",cnt);
		for(int i=f ; i<=l ; ++i)
		{
			if(ch[i]!='*')
				cout<<ch[i];
		}
		cout<<endl;
		cnt++;
	}
}
