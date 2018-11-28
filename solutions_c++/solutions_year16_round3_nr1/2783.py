#include<bits/stdc++.h>
using namespace std;

int main()
{
	int t,k,i;
	scanf("%d",&t);
	k=1;
	while(t--)
	{
		int n;
		scanf("%d",&n);
		long long sum=0,tmp=0;
		int a[n+1];
		for( i=0;  i<n ; ++i)
		{
			scanf("%d",&a[i]);
			sum+=a[i];
		}
		printf("Case #%d: ",k);
		
		while(true)
		{
			if(sum<=0)
				break;
			int pos[n+1],maxa=-1,cnt=0;
			for(i=0 ; i<n ; ++i)
				maxa=max(a[i],maxa);
			for( i=0; i<n ;  ++i)
			{		
				if(a[i]==maxa)
				{
					maxa=a[i];
					pos[cnt]=i;
					cnt++;
					if(cnt==5)
						break;
				}
			}
			
			char x;
			if(cnt==1 || cnt==3)
			{
				 x = pos[0]+65;		 
				cout<<x<<" ";
				a[pos[0]]--;
				sum--;
			}	
			else 
			{
				x = pos[0]+65;
				cout<<x;
				x = pos[1]+65;
				cout<<x<<" ";
				a[pos[0]]--;
				a[pos[1]]--;
				sum-=2;
			}
		}
		cout<<endl;
			++k;
	}
}
