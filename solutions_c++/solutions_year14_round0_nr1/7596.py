#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
using namespace std;
int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    int i,n,t,q1,q2,first[5][5],sec[5][5],j,k,cas=1;
    //scanf("%d",&t);
    cin>>t;
    for(i=1; i<=t; i++)
    {
        //scanf("%d",&q1);
        cin>>q1;
        for(j=1; j<=4; j++)
        {
            for(k=1; k<=4; k++)
            {
                //scanf("%d",&first[j][k]);
                cin>>first[j][k];
            }
        }
        //scanf("%d",&q2);
        cin>>q2;
        for(j=1; j<=4; j++)
        {
            for(k=1; k<=4; k++)
            {
                //scanf("%d",&sec[j][k]);
                cin>>sec[j][k];
            }
        }
        int c=0,ans=0;
        for(j=1; j<=4; j++)
        {
            for(k=1; k<=4; k++)
            {
                if(first[q1][j]==sec[q2][k])
                {
                    ans=first[q1][j];
                    c++;
                }
            }
        }
        if(c==1)
        {
            //printf("Case #%d: %d\n",cas++,ans);
            cout<<"Case #"<<cas++<<": "<<ans<<endl;
        }
        else if(c==0)
        {
            //printf("Case #%d: Volunteer cheated!\n",cas++);
            cout<<"Case #"<<cas++<<": "<<"Volunteer cheated!"<<endl;
        }
        else
        {
            //printf("Case #%d: Bad magician!\n",cas++);
            cout<<"Case #"<<cas++<<": "<<"Bad magician!"<<endl;
        }
    }
    return 0;
}
