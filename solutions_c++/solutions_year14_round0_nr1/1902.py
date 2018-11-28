#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string.h>

using namespace std;

int map1[5][5];
int map2[5][5];
int flag[17];

int main()
{
    int t,c=0;
    cin>>t;
    while(t--)
    {
        memset(flag,0,sizeof(flag));
        int a,b;
        c++;
        cin>>a;
        for(int i = 1; i < 5; ++ i)
            for(int j = 1; j < 5; ++ j)
            cin>>map1[i][j];
        cin>>b;
        for(int i = 1; i <5; ++ i)
            for(int j = 1; j < 5; ++ j)
            cin>>map2[i][j];
        int x = 0;
        int ans;
        for(int i = 1; i < 5; ++ i)
        {
            flag[map1[a][i]]=1;
        }
        for(int i = 1; i < 5; ++ i)
        {
            if(flag[map2[b][i]])
            {
                x++;
                ans = map2[b][i];
            }
        }
        printf("Case #%d: ",c);
        if( x == 0)
            puts("Volunteer cheated!");
        else if(x == 1)
            printf("%d\n",ans);
        else
            puts("Bad magician!");
    }
    return 0;
}
