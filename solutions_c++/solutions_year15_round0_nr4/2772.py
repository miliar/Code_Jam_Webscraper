#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
int t;
int main()
{
    //freopen("in1.txt","r",stdin);
    //freopen("out1.txt","w",stdout);
    scanf("%d",&t);
    int tc=0;
    while(t--)
    {
        string ans="";
        int x,r,c;
        cin>>x>>r>>c;
        if(x==1)
            ans="GABRIEL";
        else if(x==2&&((r*c)&1))
            ans="RICHARD";
        else if(x==2)
            ans="GABRIEL";
        else if(x==3)
        {
            if((r*c)>3&&!((r*c)%3))
                ans="GABRIEL";
            else
                ans="RICHARD";
        }
        else if(x==4)
        {
            if((r*c)<12||(r*c)%4)
                ans="RICHARD";
            else
                ans="GABRIEL";
        }
        else if(x==5)
        {

        }
        else if(x==6)
        {

        }
        else
            ans="RICHARD";
        cout<<"Case #"<<++tc<<": "<<ans<<endl;
    }
}
