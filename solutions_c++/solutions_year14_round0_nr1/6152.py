#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int main()
{
    int t;
    freopen("A-small-attempt4.in","r",stdin);
    freopen("out.out","w",stdout);
    cin>>t;
    for (int tt=1;tt<=t;tt++)
    {
        int a1,a2,ar1[5],ar2[5];
        int a,b,c,d;
        cin>>a1;
        for (int i=1;i<=4;i++)
        {
            if (i!=a1)
                cin>>a>>b>>c>>d;
            else
                cin>>ar1[1]>>ar1[2]>>ar1[3]>>ar1[4];
        }
        cin>>a2;
        for (int i=1;i<=4;i++)
        {
            if (i!=a2)
                cin>>a>>b>>c>>d;
            else
                cin>>ar2[1]>>ar2[2]>>ar2[3]>>ar2[4];
        }
        int br[20];
        memset(br,0,sizeof(br));
        for (int i=1;i<=4;i++)
            br[ar1[i]]=1;
        int tmp=0,ans;
        for (int i=1;i<=4;i++)
        {
            if (br[ar2[i]]==1)
            {
                tmp++;
                ans=ar2[i];
            }
        }
        cout<<"Case #"<<tt<<": ";
        if (tmp==0)
            cout<<"Volunteer cheated!";
        else if (tmp==1)
            cout<<ans;
        else if (tmp>1)
            cout<<"Bad magician!";
        if (tt<t)
            cout<<endl;
    }
    return 0;
}
