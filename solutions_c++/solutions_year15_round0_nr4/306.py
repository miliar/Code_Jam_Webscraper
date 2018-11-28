//.RandomUsername (Nikola Jovanovic)
//Google Code Jam 2015
//Qualification Round
//D

#include <bits/stdc++.h>
#define MAXN 1005
#define lld long long
#define ff(i,a,b) for(int i=a; i<=b; i++)
#define fb(i,a,b) for(int i=a; i>=b; i--)
#define par pair<int, int>
#define fi first
#define se second
#define mid (l+r)/2
#define INF 1000000000LL

using namespace std;

int t;
int x,r,c;
int d;
bool moze;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &t);
    for(int tt=1; tt<=t; tt++)
    {
        moze = false;
        scanf("%d %d %d", &x, &r, &c);
        d = r * c;
        if(x <= 5 && d % x == 0 && min(r,c) >= x - 1)
                moze = true;
        if(x == 6 && d % 6 == 0 && min(r,c) >= 4 && max(r,c) >= 6)
                moze = true;
        if(moze)
            printf("Case #%d: GABRIEL\n", tt);
        else
            printf("Case #%d: RICHARD\n", tt);
    }
    return 0;
}
