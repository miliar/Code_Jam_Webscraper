#include<iostream>
#include<stdio.h>
#include<string.h>
#define read_ freopen("in.in","r",stdin)
#define write_ freopen("out.txt","w",stdout)
using namespace std;
const int S = 6;
const int SZ = 20;
int main()
{
    read_;
    write_;
    int T,fans,sans,fcon[S][S],scon[S][S],col[SZ];
    cin>>T;
    for(int t=1; t<=T; t++)
    {
        memset(col,0,sizeof(col));
        cin>>fans;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                cin>>fcon[i][j];
            }
        }
        for(int i=0; i<4; i++)col[fcon[fans-1][i]]=1;
        cin>>sans;
        for(int i=0; i<4; i++)
        {
            for(int j=0; j<4; j++)
            {
                cin>>scon[i][j];
            }
        }
        for(int i=0; i<4; i++)if(col[scon[sans-1][i]]==1)col[scon[sans-1][i]]=2;
        int c = 0;
        int ans = -1;
        for(int i=1; i<17; i++)
        {
            if(col[i]==2)
            {
                c++;
                ans=i;
            }
        }
        if(c==1)printf("Case #%d: %d\n",t,ans);
        else if(c==0)printf("Case #%d: Volunteer cheated!\n",t);
        else printf("Case #%d: Bad magician!\n",t);
    }
    return 0;
}


