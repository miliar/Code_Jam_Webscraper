#include<iostream>
using namespace std;
int result(int t,int r)
{
    int area=0;
    int counter=0;
    while(t>=0)
    {
        area=((r+1)*(r+1)-r*r);
        t=t-area;r+=2;
        if(t>=0)
            counter++;
    }
    return counter;
}
int main()
{
    int T,r,t,res;
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        cin>>r>>t;
        res=result(t,r);
        cout<<"Case #"<<i<<": "<<res<<endl;
    }
    return 0;
}
