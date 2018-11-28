#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>
using namespace std;

bool check(bool A[10])
{
	for(int i=0;i<10;i++)
		if(!A[i])
			return false;
	return true;
}

void assign(unsigned long long int n, bool A[])
{
	while(n)
	{
		A[n%10]=true;
		n/=10;
	}
}

int main()
{
    int t,i;
    cin>>t;
    for(i=1;i<=t;i++)
    {
    	unsigned long int n;
    	unsigned long long int k=0;
    	cin>>n;
    	bool A[10]={false};
    	cout<<"Case #"<<i<<": ";
    	if(n)
    	{
    		while(!check(A))
    		{
    			k+=n;
    			assign(k,A);
    		}
    		cout<<k<<endl;
    	}
    	else
    		cout<<"INSOMNIA\n";
    }
    return 0;
}
