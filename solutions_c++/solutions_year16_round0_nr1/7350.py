#include<bits/stdc++.h>
using namespace std;
#define lld long long int

bool count_digits(lld n,int ar[])
{
   while(n>0)	
   {
   	int temp=n%10;
   	ar[temp]++;
   	n=n/10;
   }
   for(int i=0;i<10;i++)
   {
   	if(ar[i]==0)
   	return true;
   }
   return false;
}

int main()
{
    int t,g=1;
    lld n;
	scanf("%d",&t);
	while(t--)
	{
	    
	    scanf("%lld",&n);
		int ar[10]={0};
		if(n==0)
		{
			cout<<"Case #"<<g<<": "<<"INSOMNIA"<<endl;g++;
			continue;
		}
		lld i=0;
		while(1)
		{
			i++;
			lld N=n*i;
			bool ans=count_digits(N,ar);
			if(ans==false)
			{
				cout<<"Case #"<<g<<": "<<N<<endl;
				break;
			}
	    }
	    g++;
		
	}	
	return 0;
}
