#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int t, i, j, ca=1, k;
    int a[10][10], b[10][10];
    int x, y, cnt, ans;
    cin>>t;
    while(t--)
    {
        cin>>x;
        for(i = 1; i < 5; i++)
            for(j = 1; j < 5; j++)
            cin>>a[i][j];
        cin>>y;
        for(i = 1; i < 5; i++)
            for(j = 1; j < 5; j++)
            cin>>b[i][j];

        cnt = 0;
        for(j = 1; j < 5; j++)
            for(k = 1; k < 5; k++)
            if(a[x][j] == b[y][k])
            {
                ans = a[x][j];
                cnt++;
            }
            printf("Case #%d: ", ca++);
            if(cnt==0)
             cout<<"Volunteer cheated!"<<endl;
             else if(cnt==1)
                cout<<ans<<endl;
             else
                cout<<"Bad magician!"<<endl;
    }
    return 0;
}
