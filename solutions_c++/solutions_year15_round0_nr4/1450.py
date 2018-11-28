#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("D-small-attempt0.in", "rt", stdin);
    freopen("dominoes.out", "wt", stdout);
    int t;
    cin>>t;
    int k;
    for(k=1;k<=t;k++)
    {
        /****1=Gabriel and 0 = Richard*****/
        int x,r,c,i,j,flag=0;
        cin>>x>>r>>c;
        if(x==1)
            flag=1;
        else if(x==2)
        {
            if(r%2==1&&c%2==1)
                flag=0;
            else
                flag=1;
        }
        else if(x==3)
        {
            if( (r==2&&c==3)||(r==3&&c==2)||(r==3&&c==3)||(r==3&&c==4)||(r==4&&c==3) )
                flag=1;
            else
                flag=0;
        }
        else
        {
            if((r==3&&c==4)||(r==4&&c==3)||(r==4&&c==4))
                flag=1;
            else
                flag=0;
        }
        printf("Case #%d: ",k);
        if(flag)
            cout<<"GABRIEL"<<endl;
        else
            cout<<"RICHARD"<<endl;

    }
    return 0;
}
