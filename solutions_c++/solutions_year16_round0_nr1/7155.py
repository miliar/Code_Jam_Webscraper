#include<iostream>
using namespace std;
int main()
{
	freopen("A-large.in","r",stdin);
    freopen("outputlarge.out","w",stdout);
	int j,t,n,x=1,k,c;
	int a[10];
	cin>>t;
	while(x<=t)
	{
		cin>>n;
		for(int i=0;i<10;i++)
		a[i]=0;
		c=0;
		j=1;
		while(c!=10)
		{
		c=0;
		k=j*n;
		while(k>0)
		{
			a[k%10]=1;
			k=k/10;
		}
		for(int i=0;i<10;i++)
		c+=a[i];
		if(n==k&&j>1)
		break;
		j++;
	    }
	    j--;
	    if(c<10)
	    cout<<"Case #"<<x<<": "<<"INSOMNIA"<<endl;
	    else
	    cout<<"Case #"<<x<<": "<<n*j<<endl;
	    x++;
	}
	return 0;
}
