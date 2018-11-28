# include<cstdio>
# include<cmath>
# include<algorithm>
using namespace std;
int main()
{
    int i,j;
    int sum = 0, req = 0;
    int n,t,k;
    char in[100000];
    scanf("%d",&t);
    for(i=1;i<=t;i++)
    {
        req = 0;
        sum = 0;
        scanf("%d%s",&k,in);
        sum = in[0] - '0';
        for(j=1;j<=k;j++)
        {
            if(sum<j)
            {
                req += j-sum;
                sum += j-sum;
            }
            sum += in[j] - '0';
        }
        printf("Case #%d: %d\n",i, req);
    }
}