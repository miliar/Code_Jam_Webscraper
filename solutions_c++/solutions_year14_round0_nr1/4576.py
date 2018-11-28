#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
using namespace std;
int r1[5],r2[5];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);


    int t;
    cin>>t;

    for(int ti=0;ti<t;ti++)
    {
        int a;
        cin>>a;
        a--;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int b;
                cin>>b;
                if(i==a)
                {
                    r1[j]=b;
                }
            }
        }
        cin>>a;
        a--;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                int b;
                cin>>b;
                if(i==a)
                {
                    r2[j]=b;
                }
            }
        }

        int cnt=0;
        int ans=-1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(r1[i]==r2[j])
                {
                    cnt++;
                    ans=r1[i];
                }
            }
        }
        cout<<"Case #"<<ti+1<<": ";
        if(cnt==1)
        {
            cout<<ans<<endl;
        }
        else if(cnt>1)
        {
            cout<<"Bad magician!"<<endl;
        }
        else
        {
            cout<<"Volunteer cheated!"<<endl;
        }


    }
    return 0;
}
