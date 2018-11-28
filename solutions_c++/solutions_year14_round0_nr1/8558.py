#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;

typedef long long ll;

ll ar1[4][4];
ll ar2[4][4];
ll finar1[4];
ll finar2[4];

int main()
{
    freopen("//home//vivek//Desktop//input.txt","r",stdin);
    freopen("//home//vivek//Desktop//output.txt","w",stdout);
    ll t,cases,i,j,r1,r2,ans,cnt;
    cin>>cases;
    for(t=1;t<=cases;t++)
    {
        cin>>r1;
        for(i=0;i<4;i++)
        {
           for(j=0;j<4;j++)
              cin>>ar1[i][j];
        }
        finar1[0]=ar1[r1-1][0];   finar1[1]=ar1[r1-1][1];
        finar1[2]=ar1[r1-1][2];   finar1[3]=ar1[r1-1][3];

        cin>>r2;
        for(i=0;i<4;i++)
        {
           for(j=0;j<4;j++)
              cin>>ar2[i][j];
        }
        finar2[0]=ar2[r2-1][0];   finar2[1]=ar2[r2-1][1];
        finar2[2]=ar2[r2-1][2];   finar2[3]=ar2[r2-1][3];

        //for(i=0;i<4;i++) cout<<finar1[i]<<" "; cout<<endl;
        //for(i=0;i<4;i++) cout<<finar2[i]<<" "; cout<<endl;

        cnt=0;
        for(i=0;i<4;i++)
        {
           for(j=0;j<4;j++)
           {
               if(finar1[i]==finar2[j])
               {
                   cnt++;
                   ans=finar1[i];
               }
           }
        }
        cout<<"Case #"<<t<<": ";
        if(cnt==1) cout<<ans<<endl;
        else if(cnt==0) cout<<"Volunteer cheated!"<<endl;
        else cout<<"Bad magician!"<<endl;

    }
    return 0;
}

