#include<cstdio>
#include<iostream>
#include<queue>
using namespace std;
int g[1000][1000];

int main()
{
    int test,three,t,i,j,m,n,flg,fst,snd,one;
    freopen("C://Users//Sheemul//Downloads//B-small-attempt2.in","r",stdin);
    scanf("%d",&test);
    for(t=0;t<test;t++)
    {
        scanf("%d%d",&n,&m);
        one=0;
        int srt[200]={0};
        //priority_queue<int> Q;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                scanf("%d",&g[i][j]);
                if(g[i][j]==1) one++;
                //srt[g[i][j]]++;
                //Q.push(200-g[i][j]);
            }
        }
        //for(i=0;i<105;i++)
        //if(srt[i]) Q.push(200-i);
        //fst=200-Q.top();
        //Q.pop();
        //printf("anamul\n");
        //while(!Q.empty())
        {
            //printf("anamul\n");
            //snd=200-Q.top();
            //Q.pop();
            //printf("%d %d\n",fst,snd);
            for(i=0;i<n;i++)
            {
                if(g[i][0]==1)
                {
                    int fl=2;
                    for(j=0;j<m;j++)
                    {
                        if(g[i][j]!=1) fl=0;
                    }
                    if(fl)
                    {
                        for(j=0;j<m;j++)
                        {
                            g[i][j]=3;
                        }
                    }
                }
            }
            /*for(i=0;i<n;i++)
            {
                for(j=0;j<m;j++)
                {
                    printf("%d ",g[i][j]);
                }
                printf("\n");
            }*/
            for(i=0;i<m;i++)
            {
                if(g[0][i]==1||g[0][i]==3)
                {
                    int fl=2;
                    for(j=0;j<n;j++)
                    {
                        if(g[j][i]!=1&&g[j][i]!=3) fl=0;
                    }
                    if(fl)
                    {
                        for(j=0;j<n;j++)
                        g[j][i]=3;
                    }
                }
            }
            three=0;
            for(i=0;i<n;i++)
            {
                for(j=0;j<m;j++)
                {
                    if(g[i][j]==3) three++;
                }
                //printf("\n");
            }
            //fst=snd;
        }
         freopen("E://Anamul Kabir//output.txt","a",stdout);
        /*flg=2;
        for(i=0;i<n;i++)
        {
            for(j=0;j<m;j++)
            {
                if(g[i][j]!=snd&&g[i][j]!=snd+48)
                {
                    flg=0;
                    break;
                }
            }
        }*/
        if(one==three) printf("Case #%d: YES\n",t+1);
        else printf("Case #%d: NO\n",t+1);
    }
}
