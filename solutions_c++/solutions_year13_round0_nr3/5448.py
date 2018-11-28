#include<iostream>


using namespace std;

int main()
{
    int c[]={1,4,9,121,484};
    int t,a,b,i,q,count;
    cin>>t;
    for(q=0; q<t; q++)
    {
         cin>>a>>b;
         count=0;
         for(i=0; i<5; i++)
         {
             if(c[i]>=a && c[i]<=b)
             count++;
         }
         cout<<"Case #"<<q+1<<": "<<count<<endl;
    }
    return 0;
}

