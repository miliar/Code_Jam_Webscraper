#include <bits/stdc++.h>
using namespace std;
#define in(n) scanf("%d",&n)
int main() {
	// your code goes here
	int t,n,ct,T,a,b;
	bool flag=false;
	
	in(t);
	T=t;
	while(t--)
	{
		bool arr[10];
		for(int i=0;i<=9;i++)
		arr[i]=false;
		
		flag=false;
		ct=10;
		
		in(n);
		for(int i=1;i<=100;i++)
		{
			a=n*i;
			while(a>0)
			{
				b=a%10;
				if(arr[b]==false)
				{
					arr[b]=true;
					ct--;
				}
				a=a/10;
			}
			if(ct==0)
			{
				a=n*i;
				flag=true;
				break;
			}
		}
		if(flag==true)
		printf("Case #%d: %d\n",T-t,a);
		else
		printf("Case #%d: INSOMNIA\n",T-t);
	}
	return 0;
}