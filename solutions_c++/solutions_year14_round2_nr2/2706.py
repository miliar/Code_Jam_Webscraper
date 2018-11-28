#include<iostream>
using namespace std;
int main()
{
int a,b,k;
int t,i,j,count=0;
cin>>t;
int d=0;
while(d<t)
{
count=0;
cin>>a>>b>>k;
for (i=0;i<a;i++)
{
    for(j=0;j<b;j++)
    {

        { //  cout<<i<<" "<<j<<" "<<count<<endl;
            if((i&j)<k and (i&j)>=0 )
                ++count;

        }
    }
}
cout<<"Case #"<<d+1<<": "<<count<<endl;
++d;
}


return 0;
}
