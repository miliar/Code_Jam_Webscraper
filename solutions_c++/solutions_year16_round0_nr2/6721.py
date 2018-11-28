#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
char str[101];
int flag[2001];
int bit[11];
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int len,t,cas = 0,ans;
    queue<int> que;
    que.push(0);
    flag[0] = 1;
    while(!que.empty())
    {
        int tp = que.front();
        for(int i = 0;i < 10;i ++)
        {
            if(tp&(1<<i))
            bit[i] = 1;
            else
            bit[i] = 0;
        }
        for(int i = 1;i <= 10;i ++)
        {
            int temp = 0;

            for(int j = 0;j < 10;j ++)
            {
                if(j >= i)
                {
                    if(bit[j])
                    temp += 1<<j;
                }
                else
                {
                    if(1^bit[i-j-1])
                    temp += 1<<j;
                }
            }
            if(!flag[temp])
            {
                que.push(temp);
                //if(temp == 11) printf("%d %d\n",tp,i);
                flag[temp] = flag[tp] + 1;
                //if(flag[temp] <= 3)
                //printf("%d %d\n",temp,flag[temp]);
            }
        }
        que.pop();
    }
    //for(int i = 0;i <= 16;i ++)
    //printf("%d %d\n",i,flag[i]);
    scanf("%d",&t);
    while(t--)
    {
        cas ++;
        scanf("%s",str);
        len = strlen(str);
        ans = 0;
        for(int i = 0;i < len;i ++)
        {
            if(str[i] == '-')
            ans += 1<<(i);
        }
        printf("Case #%d:  %d\n",cas,flag[ans]-1);
    }
}
