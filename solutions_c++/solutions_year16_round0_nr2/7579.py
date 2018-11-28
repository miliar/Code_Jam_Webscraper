#include<bits/stdc++.h>
using namespace std;
char s[1005];


void rev(int st,int e)
{
	while(st<e)
	{
		int t;
		t=s[st];
		s[st++]=s[e];
		s[e--]=t;
		
		
	}
	
}
void change(int st,int e)
{
	int i;
	for(i=st;i<=e;i++)
	{
		if(s[i]=='+')
		s[i]='-';
		else
		s[i]='+';
	}
}

int main()
{
	int T;
	scanf("%d",&T);
	int t;
	ofstream o("program3data.txt");
	for(t=0;t<T;t++)
	{
		int ans=0,f1=1,f2=0;
		scanf("%s",s);
		
		int l=strlen(s);
		int i=l-1;
		
		while(i>=0)
		{
			if(f1==1){
			
			if(s[0]==s[i] && s[i]=='-')
			{
				rev(0,i);
				change(0,i);ans++; // cout<<ans;
				i--;continue;
			}
			if(s[0]==s[i] && s[i]=='+')
			{i--;
			continue;}
			if(s[0]!=s[i] &&s[i]=='-')
			{
				ans+=1;
				f2=1;f1=0;
				i--;
				
				continue;
			}
			if(s[0]!=s[i] &&s[i]=='+')
			{
				i--;
				
				continue;
			}
		}
		
		
			else if(f2==1){
			
			if(s[0]==s[i] && s[i]=='+')
			{
				rev(0,i);
				change(0,i);ans++;
				i--;continue;
			}
			if(s[0]==s[i] && s[i]=='-')
			{i--;
			continue;}
			if(s[0]!=s[i] &&s[i]=='+')
			{
				ans+=1;
				f1=1;f2=0;
				i--;
				
				continue;
			}
			if(s[0]!=s[i] &&s[i]=='-')
			{
				i--;
				
				continue;
			}
		}
			
		}
		
		cout<<"Case #"<<t+1<<": "<< ans<<"\n";
		o<<"Case #"<<t+1<<": "<< ans<<"\n";
	}
	return 0;
}
