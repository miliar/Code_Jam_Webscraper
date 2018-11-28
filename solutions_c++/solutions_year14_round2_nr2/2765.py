#include<iostream>
using namespace std;
int main()
{
    short t,count=0;
    cin>>t;
    while(count++<t)
    {
        long a,b,k,i,j,temp;
        long long c=0;
        cin>>a>>b>>k;
        for(i=0;i<a;i++)
        for(j=0;j<b;j++)
        {
            temp=i&j;
            if(temp<k)
            c++;
        }   
        cout<<"Case #"<<count<<": "<<c<<endl;     
    }
    return 0;
}
