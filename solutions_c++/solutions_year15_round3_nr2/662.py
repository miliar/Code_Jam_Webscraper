
#include<bits/stdc++.h>
//#include <windows.h>
using namespace std;

#define FRE(i,a,b)  for(i = a; i <= b; i++)
#define FRL(i,a,b)  for(i = a; i < b; i++)
#define mem(t, v)   memset ((t) , v, sizeof(t))
#define sqr(x)      ((x)*(x))
#define all(x)      x.begin(),x.end()
#define un(x)       x.erase(unique(all(x)), x.end())
#define sf(n)       scanf("%d", &n)
#define sff(a,b)    scanf("%d %d", &a, &b)
#define sfff(a,b,c) scanf("%d %d %d", &a, &b, &c)
#define D(x)        cout<<#x " = "<<(x)<<endl
#define pf          printf
#define VI          vector <int>
#define pii         pair <int, int>
#define pll         pair <LL, LL>
#define pb          push_back
#define mp          make_pair
#define pi          acos(-1.00)
#define DBG         pf("Hi\n")
#define sz          size()
#define ins         insert
#define fi          first
#define se          second
#define xx          first
#define yy          second
#define inf         (1<<29)
#define hp          (LL) 999983
#define MOD         100007
#define eps         1e-9
#define MAX         7

typedef long long int LL;
typedef double db;

//int dx[] = {+0,+1,+0,-1};
//int dy[] = {+1,+0,-1,+0};
//int dx[] = {-1,-1,-1,+0,+0,+1,+1,+1};
//int dy[] = {-1,+0,+1,-1,+1,-1,+0,+1};
//bool check(LL n, int pos) {return (bool) (n & ((LL)1<<pos));}
//LL on(LL n, int pos) {return n | ((LL)1<<pos); }
//LL off(LL n, int pos) {return n & ~((LL)1<<pos); }

char sq[MAX+5];

char str[MAX+5];
char tar[MAX+5];

int K, L, S, cnt[MAX+5], glb, mx;

int kmp()
{
    int i = 0, j = 0, ret = 0, k;

    for(i = 0; str[i]; i++)
    {
        j = 0;
        k = i;
        while(str[i] && tar[j] && str[i] == tar[j])
            i++, j++;

        ret += (!tar[j]);
        i = k;
    }
    return ret;
}


void bkt(int idx)
{
    if(idx == S)
    {
        //puts(str);
        glb++;
        int nw = kmp();
        mx = max(mx, nw);

        cnt[nw]++;
        return;
    }

    int i;
    FRL(i,0,K)
    {
        str[idx] = sq[i];
        bkt(idx+1);
    }
}

int main()
{
    freopen("c:\\Users\\User\\Desktop\\in.txt", "r", stdin);
    freopen("c:\\Users\\User\\Desktop\\out.txt", "w", stdout);
    //ios_base::sync_with_stdio(0); cin.tie(0);

    int i, j, k, t, cs, n, m, mn;
    double res;

    /*strcpy(str, "BA");
    strcpy(tar, "B");
    D(kmp());*/

    sf(t);
    FRE(cs,1,t)
    {
        glb = mx = 0;
        mem(cnt, 0);
        mem(sq,0);
        mem(str,0);
        mem(tar,0);

        res = 0;

        sfff(K,L,S);
        scanf("%s %s", sq, tar);

        bkt(0);
        FRE(i,1,7)
            res += ((LL)i * cnt[i])/(db) glb;


        pf("Case #%d: %0.10lf\n", cs, mx-res+eps);
    }

    return 0;
}



