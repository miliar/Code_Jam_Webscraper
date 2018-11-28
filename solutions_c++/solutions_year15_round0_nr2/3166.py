#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
using namespace std;

const int MAXP = 9;
int T,n,m;
vector<int> num;

int main()
{
    char inpath[100] = "C:\\Users\\Bin\\Downloads\\B-large.in";
    char outpath[100] = "C:\\Users\\Bin\\Downloads\\B-large.out";
    freopen(inpath,"r",stdin);
    freopen(outpath,"w",stdout);

    scanf("%d",&T);
    for(int t=1;t<=T;t++)
    {
        num.clear();
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",&m);
            num.push_back(m);
        }

        int ans = 10000;
        for(int i=1;i<=1000;i++)
        {
            int cnt = 0;
            for(int j=0;j<n;j++)
            {
                if(num[j]>i)
                {
                   cnt += num[j]/i + (num[j]%i==0?0:1)-1;
                }
            }
            ans = min(ans,i+cnt);
        }

        printf("Case #%d: %d\n", t,ans);
    }
}
