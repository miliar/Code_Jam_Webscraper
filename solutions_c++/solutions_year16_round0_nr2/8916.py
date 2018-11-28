#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t,n,k,cost,flag;
	scanf("%d",&t);
	k=1;
	while(t--)
	{
		string s;
		flag=0;
		cost=0;
		cin>>s;
		for(int i=0 ; i<s.length() ; ++i)
		{
		//	cout<<"cost: "<<cost<<endl;	
			if(s[0]=='-' && i==0)
				cost+=1;
			else
			{
				if(s[i]=='+')
					flag=1;
				if(flag && s[i]=='-')
				{
					cost+=2;
					flag=0;
				}
			}
		}
		printf("Case #%d: %d\n",k,cost);
		++k;
	}
}
