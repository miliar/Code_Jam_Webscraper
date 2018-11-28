#include<iostream>

using namespace std;

int main()
{
	long long int i,j,k,l,m,t,n,x,sum,ans;
	char s[10000];
	cin>>t;
	for(i=0;i<t;i++)
	{
		sum=0;
		ans=0;
		cin>>n;
		cin>>s;
		for(j=0;j<=n;j++)
		{
			x=s[j]-'0';
		   	if(x!=0)
		    {
		    	if(sum>=j)
		        sum=sum+x;	
		        else
		        {
				  ans=j-sum+ans;
				  sum=j+x;
				}
			}
		///cout<<sum<<"      "<<j<<"    "<<x<<endl;
		}
      cout<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	
return 0;	
}
