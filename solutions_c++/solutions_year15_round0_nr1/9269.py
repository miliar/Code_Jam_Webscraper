#include <bits/stdc++.h>

using namespace std;

#define mem(a, b) memset(a, b, sizeof(a))
#define MAX 105000
#define SZ(x) (int)x.size()
#define paii pair<int, int>
#define MP make_pair
#define pb push_back
#define fst first
#define snd second
#define INFI 1LL<<28
#define Reverse(x) reverse(x.begin(), x.end())

typedef long long ll;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A_out.out", "w", stdout);
    int i, j, k, n, t, kase=0;
    string s;
    cin>> t;
    while(t--)
    {
        int cost = 0;
        int tot = 0;
        cin >> n >> s;
        for(i=0; i<SZ(s); i++)
        {
            if(i<=tot) tot += (s[i]-'0');
            else {cost += (i-tot); tot = i; tot += (s[i]-'0');}
        }
        printf("Case #%d: %d\n", ++kase, cost);
    }
    return 0;
}
