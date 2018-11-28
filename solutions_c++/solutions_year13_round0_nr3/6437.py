#include<iostream>
using namespace std;
int main()
{
    int t,x,y,f=1;
    cin>>t;
    while(t!=0)
    {
        int count=0;
        cin>>x>>y;
        for(int i=x;i<=y;i++)
        {
            if(i==1||i==4||i==9||i==121||i==484)
                count++;
        }
        cout<<"Case #"<<f<<": "<<count<<"\n";
        t--;
        f++;
    }
    return 0;
}