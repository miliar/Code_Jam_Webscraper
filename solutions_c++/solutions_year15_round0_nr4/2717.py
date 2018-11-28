#include <bits/stdc++.h>
#define f(x) for(int j=0;j<x;++j)


using namespace std;

int main()
{
 freopen("D-small-attempt6.in","r",stdin);
 freopen("out.out","w",stdout);
    int t;
    cin>>t;


    for(int i=1;i<=t;++i)

    {

       cout<<"Case #"<<i<<": ";
        int x,r,c;
        cin>>x>>r>>c;
        string ans;
        if(x==1){ans="GABRIEL";}
        else if(x==2){(r*c%2==0)?ans="GABRIEL":ans="RICHARD";}
        else if(x==3) {(r*c%3==0 && min(r,c)>1)?ans="GABRIEL":ans="RICHARD";}
        else if (x==4){((r*c)%4==0 && min(r,c)>2)?ans="GABRIEL":ans="RICHARD";}


            cout<<ans<<endl;
    }



    return 0;
}
