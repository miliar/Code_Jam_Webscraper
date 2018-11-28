#include<iostream>
#include<stdio.h>
using namespace std;
int a[4][4],b[4][4];
int main()
{
    int t,c,i,j,g1,g2,ans,r;
    freopen("A-small-attempt0.in","r",stdin);
    freopen("aout.txt","w",stdout);
    cin>>t;
    r=1;
    while(t--)
    {
        cin>>g1;
        g1--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>a[i][j];
            }
        }
        cin>>g2;
        g2--;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                cin>>b[i][j];
            }
        }
        c=0;
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                // cout<<a[g1][i]<<' '<<b[g2][j]<<endl;
                if(a[g1][i]==b[g2][j])
                {
                   //cout<<"yes\n";
                    c++;
                    ans=a[g1][i];
                }
            }
        }
        cout<<"Case #"<<r<<": ";
        r++;
        if(c==0)cout<< "Volunteer cheated!\n";
        else if(c==1)cout<<ans<<endl;
        else cout<<"Bad magician!\n";
    }
}
