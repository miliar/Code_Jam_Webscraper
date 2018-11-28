#include <iostream>
#define ll long long
using namespace std;

int main()
{
	
	freopen("A-large.in","r",stdin),freopen("op.out","w",stdout);
	ll t,count=0;
	cin>>t;
	while(t--)
	{
		count++;
	    ll n,temp,temp1,k=0,i=1,a[10]={0};
	    cin>>n;
	    if(n!=0)
	    {
	        while(k!=10)
	        {
	            temp=i*n;
	            while(temp!=0)
	            {
	                temp1=temp%10;
	                temp=temp/10;
	                if(a[temp1]==0)
	                    k++;
	                a[temp1]++;
	            }
	            i++;
	        }
	        cout<<"Case #"<<count<<": "<<(i-1)*n<<endl;
	    }
	    else
	    {
	        cout<<"Case #"<<count<<": "<<"INSOMNIA"<<endl;
	    }
	}
	return 0;
}
