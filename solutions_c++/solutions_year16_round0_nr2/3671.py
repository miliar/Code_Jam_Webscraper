#include<bits/stdc++.h>
using namespace std;
typedef long long ll;
int reverse(char s[],ll i)
{
	ll c=i,k;
	for(k=0,c=i;k<=c;k++,c--)
	{
		if(s[c]=='-' && s[k]=='-')
		{
			s[k]='+';
			s[c]='+';
		}
		else if(s[c]=='-' && s[k]=='+')
		{
			s[k]='+';
			s[c]='-';
		}
		else if(s[c]=='+' && s[k]=='-')
		{
			s[k]='-';
			s[c]='+';
		}
		else
		{
			s[k]='-';
			s[c]='-';
		}
	}
	return 1;
}
int main()
{
	//freopen("C:\\Users\\P\\Downloads\\B-large.in","r+",stdin);
	//freopen("C:\\Users\\P\\Desktop\\abhi\\output_large.txt","w",stdout);
	ll i,j,k,l,n,tc,cntplus,cnt;
	char s[101];
	cin>>tc;
	l=1;
	while(l<=tc)
	{
		cnt=0;
		cntplus=0;
		cin>>s;
		n=strlen(s);
		while(cntplus!=strlen(s))
		{
			if(s[n-1]=='-')
			{
				i=0;
				while(s[i]=='+' && i<n-1)
				i++;
				if(i>0)
				{
				cnt=cnt+reverse(s,i-1);
			/*	for(k=0;s[k]!=0;k++)
				cout<<s[k];
				cout<<endl;*/
				}
				cnt=cnt+reverse(s,n-1);
				/*for(k=0;s[k]!=0;k++)
				cout<<s[k];
				cout<<endl;*/
			}
			n--;
			cntplus++;
		}
		
		cout<<"Case #"<<l<<": "<<cnt<<endl;
		l++;
	}
	return 0;
}
