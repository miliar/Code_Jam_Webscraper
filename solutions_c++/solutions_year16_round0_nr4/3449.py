#include<iostream>
#include<algorithm>
#include<cstring>
#include<cmath>
#include<stdio.h>
#include<queue>
#include<set>
#include<vector>
#include<map>
#include<string>
#define pq priority_queue
using namespace std;
long long ans[105];
bool flag;
int main()
{
    freopen("date1.txt","r",stdin);
    freopen("date2.txt","w",stdout);
    int t=0, T, k, c, s;
    scanf("%d", &T);
    while(++t<=T)
    {
        scanf("%d %d %d", &k, &c, &s);
        for(int i=1; i<=k; i++)
            ans[i]=i;
        while(--c)
        {
            for(int i=1; i<=k; i++)
                ans[i]=(ans[i]-1)*k+i;
        }
        printf("Case #%d:", t);
        if(k>1 && c>1)
        {
            for(int i=1; i<=k; i++)
            {
                if(k%2)
                    printf(" %lld", ans[i]+1);
            }
        }
        else
        {
            for(int i=1; i<=k; i++)
                printf(" %lld", ans[i]);
        }
        printf("\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
