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
char c[105], f[2];
bool flag;
int main()
{
    freopen("date1.txt","r",stdin);
    freopen("date2.txt","w",stdout);
    int t=0, T,ans,l;
    f[0]='+';
    f[1]='-';
    scanf("%d", &T);
    while(++t<=T)
    {
        ans=0;
        flag=0;
        scanf("%s", c);
        l=strlen(c);
        for(int i=l-1; i>=0; i--)
        {
            if(c[i]!=f[flag])
            {
                ans++;
                flag=!flag;
            }
        }
        printf("Case #%d: %d\n", t, ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
