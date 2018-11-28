#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<queue>
#include<set>
#include<map>
#include<cstdlib>
using namespace std;
typedef long long ll;

int T, cas;
int X, R, C;
char s[10010];

int main()
{
//    freopen("D-small-attempt1.in", "r", stdin);
//    freopen("out.out", "w", stdout);
    scanf("%d", &T);
    for(cas = 1; cas <= T; cas++)
    {
        scanf("%d%d%d", &X, &R, &C);
        if(R > C)swap(R, C);
        printf("Case #%d: ", cas);
        if(X == 1)
        {
            printf("GABRIEL\n");
        }
        else if(X == 2)
        {
            bool ok = false;
            if(R == 1)
            {
                if(C == 1 || C == 3)ok = true;
            }
            if(R == 2)
            {

            }
            if(R == 3)
            {
                if(C == 3)ok = true;
            }
            if(R == 4)
            {

            }
            if(ok)printf("RICHARD\n");
            else printf("GABRIEL\n");
        }
        else if(X == 3)
        {
            bool ok = false;
            if(R == 1)
            {
                ok = true;
            }
            if(R == 2)
            {
                if(C == 2 || C == 4) ok = true;
            }
            if(R == 3)
            {

            }
            if(R == 4)
            {
                ok=true;
            }
            if(ok)printf("RICHARD\n");
            else printf("GABRIEL\n");
        }
        else if(X == 4)
        {
            bool ok = false;
            if(R == 1)
            {
                ok = true;
            }
            if(R == 2)
            {
                ok = true;
            }
            if(R == 3)
            {
                if(C == 3)ok = true;
            }
            if(R == 4)
            {

            }
            if(ok)printf("RICHARD\n");
            else printf("GABRIEL\n");
        }
    }
    return 0;
}

