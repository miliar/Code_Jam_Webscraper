#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,c=0;
    freopen("inp.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    while(t--)
    {
       int x,n,m;
       cin>>x>>n>>m;
       c++;
       bool ch=false;
       switch(x)
       {
       case 1:ch=true;
        break;

       case 2:if(n%2==0 || m%2==0)
        ch=true;
        break;

       case 3:if(n>1 && m>1 && (n%3==0 || m%3==0))
        ch=true;
        break;

       case 4:if((n>2 && m>2) && (n%4==0 || m%4==0))
        ch=true;
        break;
}
    cout<<"Case #"<<c<<": ";
    if(ch)
        cout<<"GABRIEL"<<endl;
    else
        cout<<"RICHARD"<<endl;
        }

    return 0;
}

