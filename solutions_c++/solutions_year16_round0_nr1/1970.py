#include<bits/stdc++.h>
using namespace std;
int a[10];
void number(int a[],int n)
{
	int k;
	k=n;
	while(k>0)
	{
		if(a[k%10]==0)
		a[k%10]++;
		k/=10;
	}
}
int main()
{
	int t,n,valid;
	scanf("%d",&t);
	for(int m=1;m<=t;m++)
	{
		memset(a,0,sizeof(a));
		scanf("%d",&n);
		if(n==0)
		//cout<<"Case #"<<m<<": INSOMNIA"<<endl;
		printf("Case #%d: INSOMNIA\n",m);
		else
		{
		  for(int i=1;;i++)
		  {
		  	valid=1;
		    number(a,i*n);
		    for(int j=0;j<10;j++)
		    {
		    	if(a[j]==0)
		    	{
		    	  valid=0;
		    	  break;
			    }
		    }
		    if(valid==1)
		    {
		     //cout<<"Case #"<<m<<":"<<i*n<<endl;
		     printf("Case #%d: %d\n",m,i*n);
		     break;
		   }
         
		 }
	 }
}
  return 0;
  }
  
