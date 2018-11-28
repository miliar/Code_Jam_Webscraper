#include<bits/stdc++.h>
typedef long long ll;
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,k;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        int x,r,c,i,j,ans;
        cin>>x>>r>>c;
        if(x==1)
            ans=1;
        else if(x==2)
        {
            if(((r%2)!=0)&&((c%2)!=0))
                ans=0;
            else
                ans=1;
        }
        else if(x==3)
        {
            if((r==2&&c==3)||(r==3&&c==2)||(r==3&&c==3)||(r==3&&c==4)||(r==4&&c==3))
                ans=1;
            else
                ans=0;
        }
        else if(x==4)
        {
            if((r==4&&c==4)||(r==3&&c==4)||(r==4&&c==3))
                ans=1;
            else
                ans=0;
        }
        if(ans==0)
            cout<<"Case #"<<k<<": RICHARD\n";
        else
            cout<<"Case #"<<k<<": GABRIEL\n";
    }
    return 0;
}
