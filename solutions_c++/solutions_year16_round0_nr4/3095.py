#define _USE_MATH_DEFINES
#include <iostream>
#include <cstring>
#include <cmath>
using namespace std;


int main()
{
    unsigned int t,i,k,c,s,j;
    cin>>t;
    for(i=1;i<=t;i++)
    {
    	cin>>k>>c>>s;
    	cout<<"Case #"<<i<<":";
    	for(j=1;j<=k;j++)
    	{
    		cout<<" "<<j;
    	}
    	cout<<endl;
    }
    return 0;
}
