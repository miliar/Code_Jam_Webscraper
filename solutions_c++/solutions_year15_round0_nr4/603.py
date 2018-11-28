#include<bits/stdc++.h>
using namespace std;

int main ()
{
    freopen("C:\\Users\\DARPAN\\Desktop\\input.in","r",stdin);
    freopen("C:\\Users\\DARPAN\\Desktop\\output.txt","w",stdout);
    int t;
    cin>>t;
    int k=1;
    while(t--)
    {
        int x,r,c;
        cin>>x>>r>>c;
        int f=0;
        int m=r*c;
        switch(x)
        {
        case 1:
            f=1;
            break;
        case 2:
            if(m%2==0) f=1;
            else f=0;
            break;
        case 3:
            if(m==6||m==9||m==12) f=1;
            else f=0;
            break;
        case 4:
            if(m==12||m==16) f=1;
            else f=0;
            break;
        }
        if(f==0) cout<<"Case #"<<k<<": "<<"RICHARD"<<endl;
        else cout<<"Case #"<<k<<": "<<"GABRIEL"<<endl;
        k++;
    }
}


