#include<bits/stdc++.h>
using namespace std;
int main()
{
	freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
  long long int t,n,i,j,val,k,flag;
  int a[10];
  cin>>t;
  k=t;
  while(t--)
  {
  	cin>>n;
  	if(n==0)
  	{
  		cout<<"Case #"<<k-t<<": "<<"INSOMNIA"<<endl;	
  		continue;
	  }
  	for(i=0;i<10;i++)
  	a[i]=0;
  	for(i=1;i<100000000;i++)
  	{
  		val=n*i;
  		while(val!=0)
  		{
  			a[val%10]=1;
  			val=val/10;
  		 }
  		 flag=0;
  		 for(j=0;j<10;j++)
  		 {
  		 	if(a[j]==0)
  		    {
  		    		flag=1;
			}
		 }
		 if(flag==0)
		 {
		 	cout<<"Case #"<<k-t<<": "<<n*i<<endl;
		 	break;
		 }
  		
	  }
  	
  	
  }
	
}
