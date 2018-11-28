#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t=0,count=0,ans=0;
    cin>>t;
    int a[4][4],b[4][4];
    int aa[4],bb[4];
    int r1,r2;
    for(int test=1;test<=t;test++)
    {
        count=0;ans=0;
        cin>>r1;
        r1--;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>a[i][j];
            }

        }

        for(int i=0;i<4;i++)
        {
            aa[i]=a[r1][i];
        }
        cin>>r2;
        r2--;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                cin>>b[i][j];
            }

        }

        for(int i=0;i<4;i++)
        {
            bb[i]=b[r2][i];
        }

        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(aa[i]==bb[j])
                {count++;ans=aa[i];}
            }
        }
        if(count>1)
        {
            cout<<"Case #"<<test<<":"<<" "<<"Bad magician!"<<endl;
        }
        else if (count==1)
        {
            cout<<"Case #"<<test<<":"<<" "<<ans<<endl;
        }
        else
        {
            cout<<"Case #"<<test<<":"<<" "<<"Volunteer cheated!"<<endl;
        }
    }
}
