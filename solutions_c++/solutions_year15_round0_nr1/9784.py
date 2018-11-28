#include <iostream>
using namespace std;

int main() {
	long long int t,s,m=0,j=0,k=0,t1,x;
	char a[1005];
	cin>>t;
	t1=t;
	while(t--)
	{
	    cin>>s;
	    for(int i=0;i<=s;i++)
	    {
	    cin>>a[i];
	    if(i==0)
	    m+=(int)a[i]-48;
	    else
	    {
	        
	        if(m<i)
	        {
	        j+=i-m;
	        k=i-m;
	        m+=k;
	        }
	        m+=(int)a[i]-48;
	    }
	    }
	    x=t1-t;
	    cout<<"Case #"<<x<<": "<<j<<endl;
	    m=0;
	    j=0;
	    k=0;
	}
	return 0;
}
