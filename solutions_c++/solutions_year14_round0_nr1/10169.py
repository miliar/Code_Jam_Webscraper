#include<iostream>
using namespace std;
int main()
{
    int t,c[8][8],a1,pos[8],a2,i,j,br=0,ans,caseno=1;
    cin>>t;
    while(t)
    {
        cin>>a1;
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        cin>>c[i][j];
        for(i=1;i<=4;i++)
        pos[i]=c[a1][i];
        cin>>a2;
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        cin>>c[i][j];
        for(j=1;j<=4;j++)
        {
            for(i=1;i<=4;i++)
            if(c[a2][j]==pos[i])
            {
                br++;
                ans=c[a2][j];
            }
        }
        if(br==0) cout<<"Case #"<<caseno<<": "<<"Volunteer cheated!"<<endl;
        if(br==1) cout<<"Case #"<<caseno<<": "<<ans<<endl;
        if(br>1) cout<<"Case #"<<caseno<<": "<<"Bad magician!"<<endl;
        br=0;
        caseno++;
        t--;
    }
    return 0;
}