#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <map>
#include <queue>
#include <set>
#include <vector>
#include <stack>
using  namespace std;

int main()
{
    freopen("A-small-attempt4.in","r",stdin);
    freopen("A-small-attempt1.out","w",stdout);
    int t,a,b,i,j,k;
    int s[20];
    cin>>t;
    int cas=1;
    while(t--)
    {
        memset(s,0,sizeof(s));
        cin>>a;
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        {
            cin>>k;
            if(a==i)
                s[k]++;
        }
        cin>>a;
        for(i=1;i<=4;i++)
        for(j=1;j<=4;j++)
        {
            cin>>k;
            if(a==i)
                s[k]++;
        }
        int cnt=0;
        for(i=1;i<=16;i++)
            if(s[i]==2)
        {
            k=i;
            cnt++;
        }
        printf("Case #%d: ",cas++);
        if(cnt==0)
            puts("Volunteer cheated!");
        else if(cnt==1)
            printf("%d\n",k);
        else if(cnt>1)
            printf("Bad magician!\n");
    }
    return 0;
}
