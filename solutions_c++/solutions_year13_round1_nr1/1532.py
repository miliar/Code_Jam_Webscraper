#include<cstdio>
#include<algorithm>
#include<iostream>
#include<cstring>
#include<stack>
#include<vector>
using namespace std;
int main()
{
    freopen( "input.txt", "r", stdin );
	freopen( "output.txt", "w", stdout );
    long long t,r,n,count,k=1;
    cin>>t;
    while(t--)
    {
           cin>>r>>n;
           count=0;
              while(n>=0)
              {
                         n-=(r+1)*(r+1)-r*r;
                         r+=2;
                         count++;
              }
              cout<<"Case #"<<k++<<": "<<count-1<<endl;
              
    }
}
