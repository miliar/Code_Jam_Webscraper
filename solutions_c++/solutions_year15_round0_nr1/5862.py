#include<iostream>
#include<math.h>
using namespace std;
main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	long int t,s,i,sum,temp,z,b;
	cin>>t;
	z=0;
	while(z<t)
	{
		sum=0;
		temp=0;
		cin>>s;
	    char a[s+1];
	    cin>>a;
	    for(i=1;i<s+1;i++)
	    {
	    	temp=temp+a[i-1]-48;
	      	if(i>temp)
	      	{
	            sum=sum+i-temp;
	            b=i-temp;
				temp+=b;	
	      	}
	      	
	    }
	    cout<<"Case #"<<z+1<<":"<<" "<<sum<<"\n";
	    z++;
	}
}
