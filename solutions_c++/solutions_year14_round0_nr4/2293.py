#include<cstdio>
#include<vector>
#include<algorithm>
using namespace std;
int ans1,ans2,N;
vector<double>N1,K1;
void game1()
{
    int done[1001];
    int i,j,k;

    for(i=0;i<N;i++)
    {
        done[i]=0;
    }
    sort(N1.begin(),N1.end());
    sort(K1.begin(),K1.end());
    j=0;
    k=0;
    i=N-1;
    for(k=N-1;k>=0;k--)
    {
        if(N1[i]<K1[k])
        {
            done[j]=1;
            j++;
        }
        else
        {
            i--;
            ans1++;
            done[i]=1;
        }
    }
}
void game2()
{
    int i,j;
    int done[1001];
    for(i=0;i<N;i++)
    {
        done[i]=0;
    }
    j=0;
    for(i=0;i<N;i++)
    {
        for(j=0;j<N;j++)
        {
            if(K1[j]>N1[i]&&done[j]==0)
            {
                break;
            }
        }
        if(j>=N)
        {
            for(j=0;j<N;j++)
            {
                if(done[j]==0)
                break;
            }
            done[j]=1;
            ans2++;
        }
        else
        {
            done[j]=1;
        }
    }
}
void reset()
{
    N1.clear();
    K1.clear();
    ans1=ans2=0;
}
int main()
{
    int T,k,j;
    double temp;
    scanf("%d",&T);
    for(k=1;k<=T;k++)
    {
        reset();
        scanf("%d",&N);
        for(j=1;j<=N;j++)
        {
            scanf("%lf",&temp);
            N1.push_back(temp);
        }
        for(j=1;j<=N;j++)
        {
            scanf("%lf",&temp);
            K1.push_back(temp);
        }
        game1();
        game2();

        printf("Case #%d: %d %d\n",k,ans1,ans2);
    }
    return 0;
}
