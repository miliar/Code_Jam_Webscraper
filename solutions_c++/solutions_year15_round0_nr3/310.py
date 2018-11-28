//.RandomUsername (Nikola Jovanovic)
//Google Code Jam 2015
//Qualification Round
//C

#include <bits/stdc++.h>
#define lld long long
#define ff(i,a,b) for(int i=a; i<=b; i++)
#define fb(i,a,b) for(int i=a; i>=b; i--)
#define par pair<int, int>
#define fi first
#define se second
#define mid (l+r)/2
#define INF 1000000000LL
#define MAXN 10005

using namespace std;

int t;
lld l, xmod;
lld x;
char s[MAXN];

lld mul(lld a, lld b)
{
    lld z = 1;
    if(a<0)
    {
        z *= -1;
        a *= -1;
    }
    if(b<0)
    {
        z *= -1;
        b *= -1;
    }
    if(b == 1)
        return z * a;
    if(a == 1)
        return z * b;

    if(a == 2)
    {
        if(b == 2)
            return z * (-1);
        if(b == 3)
            return z * 4;
        if(b == 4)
            return z * (-3);
    }

    if(a == 3)
    {
        if(b == 2)
            return z * (-4);
        if(b == 3)
            return z * (-1);
        if(b == 4)
            return z * 2;
    }

    if(a == 4)
    {
        if(b == 2)
            return z * 3;
        if(b == 3)
            return z * (-2);
        if(b == 4)
            return z * (-1);
    }
}
//i = 2 j = 3 k = 4
map<char, lld> m;
bool moze;
lld fnd;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &t);
    m['i'] = 2, m['j'] = 3, m['k'] = 4;
    for(int tt=1; tt<=t; tt++)
    {
        moze = false;
        scanf("%lld %lld", &l, &x);
        scanf("%s", s);
        lld curr = 1;
        lld all = 1;

        for(lld i=0; i<l; i++)
        {
            curr = mul(curr, m[ s[i] ]);
        }
        for(lld i=1; i<=x%4; i++)
        {
            all = mul(all, curr);
        }

        if(all != -1)
        {
            printf("Case #%d: NO\n", tt);
            continue;
        }

        if(x >=4) fnd = 1;
        if(x == 2) fnd = -1;
        if(x == 1) fnd = curr;
        if(x == 3) fnd = -curr;

        curr = 1;
        lld levo = -1;
        lld desno = -1;
        for(lld i=0; i<min(x * l, 4 * l); i++)
        {
            curr = mul(curr, m[ s[i%l] ]);
            if(curr == 2 && levo == -1)
                levo = i+1;
            if( mul(curr, 4) == fnd)
                desno = min(x * l, 4 * l) - i - 1;
        }

        //cout<<levo<<" "<<desno<<endl;

        if(levo == -1 || desno == -1)
        {
            printf("Case #%d: NO\n", tt);
            continue;
        }

        if(levo + desno > x * l)
        {
            printf("Case #%d: NO\n", tt);
            continue;
        }

        printf("Case #%d: YES\n", tt);
    }
    return 0;
}
