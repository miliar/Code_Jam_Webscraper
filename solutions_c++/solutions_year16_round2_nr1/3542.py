#include<cstdio>
#include<cstring>

char a[2005],chk;
int mycount[30],mynum[15][30],ans[1005],round;

void dfs(int last,int idx)
{
    if(chk)
        return;
    if(mycount[0] == 0)
    {
        printf("Case #%d: ",round);
        for(int i=0;i<idx;i++)
        {
            printf("%d",ans[i]);
        }
        printf("\n");
        chk = true;
        return;
    }
    if(last == 10)
    {
        return;
    }
    for(int i=last;i<=9;i++)
    {
        bool q = true;
        for(int j=1;j<=26;j++)
        {
            if(mynum[i][j] > mycount[j])
            {
                q = false;
                break;
            }
        }
        if(q)
        {
            ans[idx] = i;
            for(int j=1;j<=26;j++)
            {
                mycount[j] -= mynum[i][j];
                if(mynum[i][j] != 0)
                    mycount[0]-= mynum[i][j];
            }
            dfs(i,idx+1);
            for(int j=1;j<=26;j++)
            {
                mycount[j] += mynum[i][j];
                if(mynum[i][j] != 0)
                    mycount[0]+= mynum[i][j];
            }
        }
        else
        {
            dfs(i+1,idx);
        }
    }
}

int main()
{
    freopen("A-small-attempt0 (1).in","r",stdin);
    freopen("eq.out","w",stdout);
    int n,t;
    scanf("%d",&t);
    mynum[0]['Z'-'A'+1] = 1;
    mynum[0]['E'-'A'+1] = 1;
    mynum[0]['R'-'A'+1] = 1;
    mynum[0]['O'-'A'+1] = 1;

    mynum[1]['O'-'A'+1] = 1;
    mynum[1]['N'-'A'+1] = 1;
    mynum[1]['E'-'A'+1] = 1;

    mynum[2]['T'-'A'+1] = 1;
    mynum[2]['W'-'A'+1] = 1;
    mynum[2]['O'-'A'+1] = 1;

    mynum[3]['T'-'A'+1] = 1;
    mynum[3]['H'-'A'+1] = 1;
    mynum[3]['R'-'A'+1] = 1;
    mynum[3]['E'-'A'+1] = 2;

    mynum[4]['F'-'A'+1] = 1;
    mynum[4]['O'-'A'+1] = 1;
    mynum[4]['U'-'A'+1] = 1;
    mynum[4]['R'-'A'+1] = 1;

    mynum[5]['F'-'A'+1] = 1;
    mynum[5]['I'-'A'+1] = 1;
    mynum[5]['V'-'A'+1] = 1;
    mynum[5]['E'-'A'+1] = 1;

    mynum[6]['S'-'A'+1] = 1;
    mynum[6]['I'-'A'+1] = 1;
    mynum[6]['X'-'A'+1] = 1;

    mynum[7]['S'-'A'+1] = 1;
    mynum[7]['E'-'A'+1] = 2;
    mynum[7]['V'-'A'+1] = 1;
    mynum[7]['N'-'A'+1] = 1;

    mynum[8]['E'-'A'+1] = 1;
    mynum[8]['I'-'A'+1] = 1;
    mynum[8]['G'-'A'+1] = 1;
    mynum[8]['H'-'A'+1] = 1;
    mynum[8]['T'-'A'+1] = 1;

    mynum[9]['N'-'A'+1] = 2;
    mynum[9]['I'-'A'+1] = 1;
    mynum[9]['E'-'A'+1] = 1;

    for(round = 1;round<=t;round++)
    {
        chk = false;
        for(int i=1;i<=26;i++)
        {
            mycount[i] = 0;
        }
        scanf("%s",a);
        n = strlen(a);
        mycount[0] = n;
        for(int i=0;i<n;i++)
        {
            mycount[a[i]-'A'+1]++;
        }
        dfs(0,0);
    }
}
