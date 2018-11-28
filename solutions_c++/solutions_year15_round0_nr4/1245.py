#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;
int T;
int x,r,c;
int a[22][22][22];
int main()
{
    freopen("D-small-attempt4.in","r",stdin);
    freopen("D-small-attempt4.out","w",stdout);
    memset(a,0,sizeof(a));
    a[1][1][1]=1;
    a[1][2][1]=1;a[1][2][2]=1;
    a[1][3][1]=1;
    a[1][4][1]=1;a[1][4][2]=1;
    a[2][2][1]=1;a[2][2][2]=1;
    a[2][3][1]=1;a[2][3][2]=1;a[2][3][3]=1;
    a[2][4][1]=1;a[2][4][2]=1;
    a[3][3][1]=1;a[3][3][3]=1;
    a[3][4][1]=1;a[3][4][2]=1;a[3][4][3]=1;a[3][4][4]=1;
    a[4][4][1]=1;a[4][4][2]=1;a[4][4][4]=1;
    cin>>T;
    int t = 0;
    int ans;
    while(t < T)
    {
        cin>>x>>r>>c;
        if (r > c)
        {
            int k = r;
            r = c;
            c = k;
        }
        ans = a[r][c][x];
        t++;
        printf("Case #%d: ",t);
        if (ans == 1) printf("GABRIEL\n"); else printf("RICHARD\n");
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}
