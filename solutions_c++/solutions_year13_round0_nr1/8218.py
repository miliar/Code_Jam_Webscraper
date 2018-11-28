#include <algorithm>
#include <iostream>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
# define LLU long long  int
# define LLD long long double
# define FOR(i,N) for(int i=0;i<(N);i++)
# define FOR1(i,a,N) for(int i=a;i<(N);i++)
# define pb push_back
# define in(x) scanf("%d",&x)
# define out(x) printf("%d\n",x)
# define clr(a) memset(a,0,sizeof(a))
# define fill(a,x) memset(a,x,sizeof(a))
# define mp make_pair
# define MX 51
using namespace std;
int main()
{
    string input[4];
    int T,r,c;
    bool checker=false;
    in(T);
    int cas=1;
    while(T--)
    {
        checker=false;
        FOR(i,4)
        cin>>input[i];
        int win=0;
        r=c=-1;
        FOR(i,4)
        {
            win=0;
            FOR(j,4)
            {
                if(input[i][j]==input[i][0] || input[i][j]=='T')
                win++;
            }
            if(win==4 && input[i][0]!='.')
            {
                checker=true;
                r=i;
                c=0;
                break;
            }
        }
        if(checker)
        {
            printf("Case #%d: %c won\n",cas++,input[r][c]);
            continue;
        }
        FOR(i,4)
        {
            win=0;
            FOR(j,4)
            {
                if(input[j][i]==input[0][i] || input[j][i]=='T')
                win++;
            }
            if(win==4 && input[0][i]!='.')
            {
                checker=true;
                r=0;
                c=i;
                break;
            }
        }
        if(checker)
        {
            printf("Case #%d: %c won\n",cas++,input[r][c]);
            continue;
        }
        win=0;
        FOR(i,4)
        if(input[i][i]==input[0][0] || input[i][i]=='T')
        win++;
        if(win==4 &&  input[0][0]!='.')
        {
            printf("Case #%d: %c won\n",cas++,input[0][0]);
            continue;
        }
        win=0;
        FOR(i,4)
        if(input[i][3-i]==input[0][3] || input[i][3-i]=='T')
        win++;
        if(win==4 &&  input[0][3]!='.')
        {
            printf("Case #%d: %c won\n",cas++,input[0][3]);
            continue;
        }
        checker=false;
        FOR(i,4)
        FOR(j,4)
        if(input[i][j]=='.')
        {
            checker=true;
            break;
        }
        if(checker)
        printf("Case #%d: Game has not completed\n",cas++);
        else
        printf("Case #%d: Draw\n",cas++);
    }
    return 0;
}
