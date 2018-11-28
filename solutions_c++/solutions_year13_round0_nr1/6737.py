#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstdlib>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <fstream>
#include <set>
#include <map>
#include <cmath>
#pragma comment(linker,"/STACK:16777216")

using namespace std;

int t,sayx,sayo,say;
bool ww;
string s[5];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    scanf("%d",&t);
    

    for(int o=1;o<=t;o++){
        getline(cin,s[0]);
        say=0;
        for(int i=1;i<=4;i++)
            getline(cin,s[i]);

        for(int i=1;i<=4;i++)
            {
                sayx=sayo=0;
                ww=0;
                for(int j=0;j<=3;j++){
                    if(s[i][j]=='X')
                        sayx++;
                    if(s[i][j]=='O')
                        sayo++;
                    if(s[i][j]=='T')
                        ww=1;
                }
                if( sayx == 4 || ( sayx == 3 && ww==1 ) )
                    {
                        printf("Case #%d: X won\n",o);
                        goto rr;
                    }
                if( sayo == 4 || ( sayo == 3 && ww==1 ) )
                    {
                        printf("Case #%d: O won\n",o);
                        goto rr;
                    }
            }
        for(int i=0;i<=3;i++)
            {
                sayx=sayo=0;
                ww=0;
                for(int j=1;j<=4;j++){
                    if(s[j][i]=='X')
                        sayx++;
                    if(s[j][i]=='O')
                        sayo++;
                    if(s[j][i]=='T')
                        ww=1;
                }
                if( sayx == 4 || ( sayx == 3 && ww==1 ) )
                    {
                        printf("Case #%d: X won\n",o);
                        goto rr;
                    }
                if( sayo == 4 || ( sayo == 3 && ww==1 ) )
                    {
                        printf("Case #%d: O won\n",o);
                        goto rr;
                    }
            }
        sayx=sayo=0;
        ww=0;
        for(int i=1;i<=4;i++)
            {
                if(s[i][i-1]=='X')
                    sayx++;
                if(s[i][i-1]=='O')
                    sayo++;
                if(s[i][i-1]=='T')
                    ww=1;
            }
        if( sayx == 4 || ( sayx == 3 && ww==1 ) )
            {
                printf("Case #%d: X won\n",o);
                goto rr;
            }
        if( sayo == 4 || ( sayo == 3 && ww==1 ) )
            {
                printf("Case #%d: O won\n",o);
                goto rr;
            }

        sayx=sayo=0;
        ww=0;
        for(int i=0;i<=3;i++)
            {
                if(s[4-i][i]=='X')
                    sayx++;
                if(s[4-i][i]=='O')
                    sayo++;
                if(s[4-i][i]=='T')
                    ww=1;
            }
        if( sayx == 4 || ( sayx == 3 && ww==1 ) )
            {
                printf("Case #%d: X won\n",o);
                goto rr;
            }
        if( sayo == 4 || ( sayo == 3 && ww==1 ) )
            {
                printf("Case #%d: O won\n",o);
                goto rr;
            }
        for(int i=1;i<=4;i++)
            for(int j=0;j<=3;j++)
                if(s[i][j]=='O' || s[i][j]=='T' || s[i][j]=='X')
                    say++;
        if(say==16){
            printf("Case #%d: Draw\n",o);
            goto rr;
        }
        printf("Case #%d: Game has not completed\n",o);

        rr:
            ww=ww;
        }



    return 0;
}
