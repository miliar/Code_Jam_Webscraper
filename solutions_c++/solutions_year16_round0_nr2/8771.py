#include<bits/stdc++.h>
using namespace std;

int main()
{
	long long t,i,j,k,counta,countb,l,m,count;
	string s;
	scanf("%lld",&t);
	for(i=1;i<=t;i++)
	{
		count=0;
		counta=0;
		countb=0;
		cin >> s;
		k=s.length();
		printf("Case #%lld: ",i);
		for(j=0;j<k;j++)
			if(s[j]=='-')
				counta++;
			else	countb++;
		if(counta==k)
		{
			printf("1\n");
			continue;
		}
		if(countb==k)
		{
			printf("0\n");
			continue;
		}
		l=0;
		for(j=l;j<k-1;j++)
		{
			if(s[j]!=s[j+1])
			{
				for(m=0;m<=j;m++)
					s[m]=s[j+1];
				l=j+1;	
				count++;	
			}
			//cout << s<< ' ';
		}
		
		if(s[0]=='+')
			printf("%lld\n",count);	
		else	printf("%lld\n",count+1);	
	}
}
