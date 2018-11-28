#include<iostream>
using namespace std;
int main()
{
    int T,t,r,circle=0,n=4;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
            circle=0;
            cin>>r>>t;
            int j=0;
            while((2*r+1+(n*j))<=t)
            {
             
             t=t-(2*r+1+(n*j));
             j++;         
             circle++;
            }
            cout<<"Case #"<<i<<": "<<circle<<endl;
    }
    return 0;
}
