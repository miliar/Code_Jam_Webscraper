#include <iostream>
#include <stdio.h>

//#define pi 3.14159

using namespace std;

int main()
{
    freopen("C:/Users/Doris/code practise/google-jam-2.1/a.in", "r", stdin);
    freopen("C:/Users/Doris/code practise/google-jam-2.1/a.out", "w", stdout);

    int T, n;
    int r,t, tmp=0, x=0;
    int i=0;
    cin>>T;
    n=T;
    while(T--)
    {
        i=0;
        cin>>r>>t;
        tmp=2*r+1;

       // cout<<t<<endl;
        while(tmp<=t)
        {
            i++;
            x=((r+2*i)*2+1);
            tmp+=x;
        }
        //cout<<x<<endl;
       // if(x+((r+2*i-2)*2+1)>t)
        //    i--;
        cout<<"Case #"<<n-T<<": "<<i<<endl;

    }
    return 0;
}
