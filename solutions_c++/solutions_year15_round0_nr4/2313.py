#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        int x,r,c;
        cin>>x>>r>>c;
        int flag=0;
        if(x==1)
        {
            flag=1;
        }
        else if(x==2)
        {
            if(r==2&&c==1)
                flag=1;
            else if(r==1&&c==2)
                flag=1;
            else if(r==2&&c==2)
                flag=1;
            else if(r==3&&c==2)
                flag=1;
            else if(r==2&&c==3)
                flag=1;
            else if(r==3&&c==4)
                flag=1;
            else if(r==4&&c==3)
                flag=1;
            else if(r==4&&c==4)
                flag=1;
            else if(r==1&&c==4)
                flag=1;
            else if(r==4&&c==1)
                flag=1;
            else if(r==2&&c==4)
                flag=1;
            else if(r==4&&c==2)
                flag=1;
        }
        else if(x==3)
        {
            if(r==2&&c==3)
                flag=1;
            else if(r==3&&c==2)
                flag=1;
            else if(r==3&&c==3)
                flag=1;
            else if(r==4&&c==3)
                flag=1;
            else if(r==3&&c==4)
                flag=1;
        }
        else if(x==4)
        {
            if(r==3&&c==4)
                flag=1;
            else if(r==4&&c==3)
                flag=1;
            else if(r==4&&c==4)
                flag=1;
        }
        if(flag==1)
            cout<<"Case #"<<(i+1)<<": "<<"GABRIEL"<<endl;
        else
            cout<<"Case #"<<(i+1)<<": "<<"RICHARD"<<endl;
    }
    return 0;
}
