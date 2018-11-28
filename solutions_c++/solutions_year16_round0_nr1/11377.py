#include<bits/stdc++.h>
using namespace std;

set<int> s;
void ins(int num)
{
	int temp;
	while(num>0)
	{
		temp=num%10;
		s.insert(temp);
		num=num/10;
	}	
}

int main() 
{
	int t,k,cs=1;
	long long int n,temp,i,ans;
	
	scanf("%d",&t);
	
	while(t--)
	{
		s.clear();
		k=1;
		scanf("%lld",&n);
		temp=n;
		
		if(n==0)
			printf("Case #%d: INSOMNIA\n",k);
		else
		{
			while(true)
			{
				i=temp*k;
				ins(i);
				if(s.size()==10)
				{
					ans=i;
					printf("Case #%d: %lld\n",cs,ans);
					break;
				}
				k++;
			}
		}
		cs++;
	}
	return 0;
}