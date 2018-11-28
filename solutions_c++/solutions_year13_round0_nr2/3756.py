#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int mp[110][110];
int np[110][110];
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int T;
    scanf("%d",&T);
    int cas = 1;
    while(T--)
    {
        printf("Case #%d: ",cas++);
        int n,m;
        scanf("%d%d",&n,&m);
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                np[i][j] = 100;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
                scanf("%d",&mp[i][j]);

        for(int i=0;i<n;i++)
        {
            int mm = 0;
            for(int j=0;j<m;j++)
                mm = max(mm,mp[i][j]);
            for(int j=0;j<m;j++)
                if(np[i][j]>mm)np[i][j] = mm;
        }
       /* cout << endl;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
                cout << np[i][j] << " ";
            cout << endl;
        }*/
        for(int j=0;j<m;j++)
        {
            int mm = 0;
            for(int i=0;i<n;i++)
                mm = max(mm,mp[i][j]);
            for(int i=0;i<n;i++)
                if(mm<np[i][j])np[i][j] = mm;
        }
        /*cout << endl;
        for(int i=0;i<n;i++)
        {
            for(int j=0;j<m;j++)
                cout << np[i][j] << " ";
            cout << endl;
        }*/
        int same = 1;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            if(np[i][j]!=mp[i][j])same = 0;
        if(same)printf("YES\n");
        else printf("NO\n");

    }
    return 0;
}
