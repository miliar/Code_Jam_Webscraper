#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main() {
	// your code goes here
	long long int t,n,n2,n1;
	int d;
	cin>>t;
	for(int i=1;i<=t;i++)
	{
	    bool a[10]={0,0,0,0,0,0,0,0,0,0};
	    cin>>n;
	    if(n==0)
	    {
	        cout<<"Case #"<<i<<": Insomnia"<<endl;
	        continue;
	    }
	    n1=n2=0;
	    while(!(a[0]&&a[1]&&a[2]&&a[3]&&a[4]&&a[5]&&a[6]&&a[7]&&a[8]&&a[9]))
	    {
	        n1+=n;
	        n2=n1;
	        while(n2)
	        {
	            d=n2%10;
	            n2/=10;
	            a[d]=1;
	        }
	    }
	    cout<<"Case #"<<i<<": "<<n1<<endl;
	}
	return 0;
}

