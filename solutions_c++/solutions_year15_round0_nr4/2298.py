#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("D-small-attempt2.in","r",stdin);
    freopen("output.txt","w",stdout);
    long long int t,i,x,r,c;
    cin>>t;
    for(i=1;i<=t;i++)
    {
        cin>>x>>r>>c;
        cout<<"Case #"<<i<<": ";
        if((r*c)%x!=0 || (x>2 && (r==1 || c==1)))
        {
            cout<<"RICHARD"<<endl;
            continue;
        }
        if(x==1 || (x==2 && (r*c)%2==0))
        {
            cout<<"GABRIEL"<<endl;
            continue;
        }
        if(x==3 && ((r==2 && c==3)|| (r==3 && c==2) || (r==3 && c==4)||(r==4 && c==3) || (r==3 && c==3)))
        {
            cout<<"GABRIEL"<<endl;
            continue;
        }
        if(x==4 && ((r==3 && c==4)||(r==4 && c==3)||(r==4 && c==4)))
        {
            cout<<"GABRIEL"<<endl;
            continue;
        }
        cout<<"RICHARD"<<endl;
    }
    return 0;
}
