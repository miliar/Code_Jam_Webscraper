#include<iostream>
#include<stdio.h>
#include<string>

using namespace std;
int MINUS=0,PLUS=1;
int main()
{

	int t;
	scanf("%d",&t);
	for(int T=0;T<t;T++)
	{
		string s;
		cin>>s;
		int p=0,n=s.size(),ans=0;
		int CURR,PREV;
		for(int i=0;i<s.size();i++)
		{


			if(i==0){ if(s[i]=='+') CURR=PLUS; else CURR=MINUS,++ans; continue;}
			PREV = CURR;
			if(s[i]=='+')
				CURR=PLUS;
			else CURR=MINUS;

			if((CURR==MINUS)&&(CURR!=PREV))
			{

				
				 ans+=2;

			}

		}
		printf("Case #%d: %d\n",T+1,ans);
	}
	return 0;
}
