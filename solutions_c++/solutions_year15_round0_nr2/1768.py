#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<iostream>
#include<queue>
#include<stack>
#include<vector>
#include<map>
#include<set>
#include<string>
using namespace std;
#define INF 0x3f3f3f3f
#define eps 1e-8
#define maxn 200005
int num[1005];
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cas=1;cas<=t;cas++)
    {
        int d;
        int ma=0;
        scanf("%d",&d);
        for(int i=0;i<d;i++)
        {
            scanf("%d",num+i);
            ma=max(ma,num[i]);
        }
        int fin=INF;
        for(int i=1;i<=ma;i++)
        {
            int temp=0;
            for(int j=0;j<d;j++)
            {
                if(num[j]%i)    temp+=num[j]/i;
                else    temp+=num[j]/i-1;
            }
            temp=i+temp;
            fin=min(fin,temp);
        }
        printf("Case #%d: %d\n",cas,fin);
    }
}
