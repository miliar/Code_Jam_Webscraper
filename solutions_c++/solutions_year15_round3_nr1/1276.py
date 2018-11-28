#include<iostream>
using namespace std;

int main()
{
    int t,i=1;
    cin>>t;
    while(i<=t)
    {
        int r,c,w,re=0;
        cin>>r>>c>>w;
        re=r*(c/w)+w-1;
        if(c%w!=0)
            re+=1;
        cout<<"Case #"<<i<<": "<<re<<endl;
        i++;
    }
    return 0;
}
