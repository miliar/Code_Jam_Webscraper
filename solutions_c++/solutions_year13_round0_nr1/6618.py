#include <iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
char data[6][6];
int solve()
{
    int numx,numo;
    for(int i=0; i<4; i++)
    {
        numx=numo=0;
        for(int j=0; j<4; j++)
            if(data[i][j]=='O')
                numo++;
            else if(data[i][j]=='X')
                numx++;
            else if(data[i][j]=='T')
                numx++,numo++;
        if(numx==4)
            return 1;
        if(numo==4)
            return 2;
        numx=numo=0;
        for(int j=0; j<4; j++)
            if(data[j][i]=='O')
                numo++;
            else if(data[j][i]=='X')
                numx++;
            else if(data[j][i]=='T')
                numx++,numo++;
        if(numx==4)
            return 1;
        if(numo==4)
            return 2;
    }
    numx=numo=0;
    for(int i=0; i<4; i++)
        if(data[i][i]=='O')
            numo++;
        else if(data[i][i]=='X')
            numx++;
        else if(data[i][i]=='T')
            numx++,numo++;
    if(numx==4)
        return 1;
    if(numo==4)
        return 2;
    numx=numo=0;
    for(int i=0; i<4; i++)
        if(data[i][3-i]=='O')
            numo++;
        else if(data[i][3-i]=='X')
            numx++;
        else if(data[i][3-i]=='T')
            numx++,numo++;
    if(numx==4)
        return 1;
    if(numo==4)
        return 2;
    for(int i=0; i<4; i++)
        for(int j=0; j<4; j++)
            if(data[i][j]=='.')
                return 3;
    return 4;
}
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    int t,s=0;
    cin>>t;
    while(t--)
    {
        cin>>data[0]>>data[1]>>data[2]>>data[3];
        int ans=solve();
        printf("Case #%d: ",++s);
        if(ans==1)
        puts("X won");
        if(ans==2)
        puts("O won");
        if(ans==3)
        puts("Game has not completed");
        if(ans==4)
        puts("Draw");
    }
    return 0;
}
