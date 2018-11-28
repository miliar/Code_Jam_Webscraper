#include<bits/stdc++.h>
using namespace std;
// Ayush Garg
int main()
{
    freopen("D-small-attempt0.in","r",stdin);
    freopen("ans4.txt","w",stdout);


    int i,J,t,ans,x,r,c,r1,c1;


    cin>>t;
    for(J=1;J<=t;J++)
    {
        cin>>x>>r1>>c1;
        r=min(r1,c1);
        c=max(r1,c1);

        if(x==1)
            ans=0;
        else if(x==2)
        {
            if((r==1 && c==1)|| (r==1 && c==3) || (r==3 && c==3))
                ans=1;
            else
                ans=0;
        }
        else if(x==3)
        {
            if( (r==2 && c==3) || (r==3 && c==3) || (r==3 && c==4) )
                ans=0;
            else
                ans=1;
        }
        else
        {
            ans=1;
            if(c==4)
            {
                if(r>=3)
                    ans=0;
            }
        }

        if(ans==0)
            cout<<"Case #"<<J<<": GABRIEL"<<endl;
        else
            cout<<"Case #"<<J<<": RICHARD"<<endl;
    }
    return 0;
}
