#include <bits/stdc++.h>
using namespace std;
bool comp(int a,int b)
{
    return (a>b);
}
int gcd(int a,int b)
{
    if(b==0)
        return a;
    else
        return gcd(b,a%b);
}
int main(void) {
    freopen("in.txt","rt",stdin);
    freopen("test.txt","wt",stdout);
    int t,x,r,c,i;
    scanf("%d",&t);
    for(i=1;i<=t;++i)
    {
        scanf("%d %d %d",&x,&r,&c);
        cout<<"Case #"<<i<<": ";
        if(x==1)
            cout<<"GABRIEL\n";
        else if(x==2)
        {
            if(r%2==0||c%2==0)
                cout<<"GABRIEL\n";
            else
                cout<<"RICHARD\n";
        }
        else if(x==3)
        {
            if((r%3==0||c%3==0)&&(r!=1&&c!=1))
                cout<<"GABRIEL\n";
            else
                cout<<"RICHARD\n";
        }
        else if(x==4)
        {
            if((r%4==0||c%4==0)&&(r>2&&c>2))
                cout<<"GABRIEL\n";
            else
                cout<<"RICHARD\n";
        }
    }
    return 0;
}
