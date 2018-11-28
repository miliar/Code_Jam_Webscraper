#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    int n,x,y;
    for(int i=0;i<t;i++)
    {
        cin>>n>>x>>y;
        if(n==1)
        {
            cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
            continue;
        }
        if(n==2)
        {
            if((x*y)%2!=0)
            cout<<"Case #"<<i+1<<": RICHARD"<<endl;
            else
            cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
            continue;
        }
        if(n==3)
        {
            if(!((x==3 && y>1) || (y==3 && x>1)))
            cout<<"Case #"<<i+1<<": RICHARD"<<endl;
            else
            cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
            continue;
        }
        if(n==4) 
        {
            if(!((x==4 && y>2) || (y==4 && x>2)))
            cout<<"Case #"<<i+1<<": RICHARD"<<endl;
            else
            cout<<"Case #"<<i+1<<": GABRIEL"<<endl;
            continue;
        }
    }
    return 0;
}