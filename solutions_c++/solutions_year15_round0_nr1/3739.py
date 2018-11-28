#include<bits/stdc++.h>
using namespace std;


int main()
{
	int t,j;
	scanf("%d",&t);
	for(j=0;j<t;j++)
	{
		int sm,temp=0,ans=0;
		scanf("%d",&sm);
		char arr[sm+2];
		scanf("%s",arr);
		for(int i=0;i<=sm;i++)
		{
			if(temp>=i) temp+=(int)(arr[i]-'0');
			else {ans+=i-temp; temp=(int)(arr[i]-'0')+i;}
		}
		printf("Case #%d: %d\n",j+1,ans );	
	}

	
}	
