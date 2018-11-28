#include<iostream>
using namespace std;

int main()
{
    int t,k,x,r,c,f;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        f=0;
        cin>>x>>r>>c;

        //if((r*c)%x==0)
        {
            if(x==1)
            {
                f=1;
            }
            else if(x==2)
            {
                if(r==2||c==2) f=1;
                else if(r==3&&c==4) f=1;
                else if(r==4&&c==3) f=1;
                else if(r==4&&c==4) f=1;
                else if(r==1&&c==4) f=1;
                else if(r==4&&c==1) f=1;
            }
            else if(x==3)
            {
                if(r==3 && (c==2||c==4||c==3)) f=1;
                else if(c==3 && (r==2||r==4)) f=1;
            }
            else if(x==4)
            {
                if(r==4&&c==4) f = 1;
                else if(r==4&&c==3) f = 1;
                 else if(r==3&&c==4) f = 1;
            }

        }
        if(f==1) cout<<"Case #"<<k<<": GABRIEL\n";
        else cout<<"Case #"<<k<<": RICHARD\n";
    }
}
