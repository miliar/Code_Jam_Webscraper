#include <iostream> 
#include <bits/stdc++.h>
    // std::cout, std::endl
#include <iomanip> 
#include <math.h>

using namespace std;
int main()
{
	int t,p=0;
	cin>>t;
	int i,j,in,de,n,temp;


	while(t--)
	{	p++;
		 
        int a[100000]={0};
        cin>>n;
        for(i=0;i<(2*n-1);i++)
        {
            for(j=0;j<n;j++)
            {
                cin>>temp;
                a[temp]++;
            }
        }
        cout<<"Case #"<<p<<": ";
        for(i=0;i<2500;i++)
        {
            if(a[i]%2==1)
            cout<<i<<" ";
        }
        cout<<"\n";


	}

	return 0;
}


