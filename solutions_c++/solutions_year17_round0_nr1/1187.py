#include<cstdio>
#include<string>
#include<iostream>
using namespace std;
int main()
{
	int T,k,n,c;
	string s;
	bool chk;
	cin>>T;
	for(int I=1;I<=T;I++)
	{
		cin>>s>>k;
		n=s.length();
		c=0;

		//printf("-- %d %d --\n",n,k);
		for(int i=0;i<=n-k;i++)
		{
			if(s[i]=='-')
			{
				c++;
				for(int j=i;j<i+k;j++)
					if(s[j]=='-')
						s[j]='+';
					else
						s[j]='-';
			}
			/*
			printf("-> %3d\n",i);
			cout<<s;
			printf("\n");
			*/
		}

		chk=true;
		for(int i=n-k;i<n;i++)
			if(s[i]=='-')
				chk=false;

		if(chk)
			printf("Case #%d: %d\n",I,c);
		else
			printf("Case #%d: IMPOSSIBLE\n",I);

	}
}