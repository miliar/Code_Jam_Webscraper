#include<stdio.h>
#include<string.h>
#include<iostream>
#include<algorithm>
#include<math.h>
#include<map>
#include<vector>
#include<string>
#include<set>
#include<queue>
#define MP(x,y) make_pair(x,y)
#define clr(x,y) memset(x,y,sizeof(x))
#define forn(i,n) for(int i=0;i<n;i++)
#define sqr(x) ((x)*(x))
#define MAX(a,b) if(a<b) a=b;
#define ll long long
using namespace std;


int a[2][10000];
int cnt;
int p, r, s, n;
char c[3] = {0, 0, 0};


int cmp(char s[], int l, int r, int sz)
{
    for(int i = 0; i < sz; i++)
    {
        if(s[l + i] != s[r + i]) return s[l + i] - s[r + i];
    }
    return 0;
}
void sp(char s[], int l, int r, int sz)
{
    for(int i = 0; i < sz; i++)
    {
        swap(s[l + i], s[r + i]);
    }
}

string gao(int k)
{
    string x = "";
    char s[10000];
    for(int i = 0; i < cnt; i++) s[i] = c[a[k][i]];
    for(int i = 0; i < n; i++)
    {
        for(int j = 0; j + 2 * (1 << i) <= (1 << n); j += 2 * (1 << i))
        {
            if(cmp(s, j, j + (1 << i), 1 << i) > 0) 
            {
                sp(s, j, j + (1 << i), 1 << i);
            }
        }
    }

    for(int i = 0; i < (1 << n); i++) x += s[i];
    //cout << x << endl;
    return x;
}
int main() {
    freopen("in","r",stdin);
    freopen("out", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++)
    {
        scanf("%d%d%d%d", &n, &r, &p, &s);

        cnt = 1;
        a[0][0] = 0;

        for(int i = 0; i < n; i++, cnt *= 2)
        {
            int *u = a[i % 2];
            int *v = a[(i + 1) % 2];
            for(int j = 0; j < cnt; j++)
            {
                int w1 = u[j];
                int w2 = (u[j] + 1) % 3;
                v[2 * j] = w1;
                v[2 * j + 1] = w2;
            }
        }
        int k = n % 2;
        //for(int i = 0; i < cnt; i++) printf("%d ", a[k][i]);
        //puts("");

        int b[3] = {0, 0, 0};
        for(int i = 0; i < cnt; i++)
        {
            b[a[k][i]] += 1;
        }
        string res1, res2, res3;
        if(b[0] == p && b[1] == r && b[2] == s)
        {
            c[0] = 'P', c[1] = 'R', c[2] = 'S';
            res1 = gao(k);
        }
        if(b[0] == r && b[1] == s && b[2] == p)
        {
            c[0] = 'R', c[1] = 'S', c[2] = 'P';
            res2 = gao(k);
        }
        if(b[0] == s && b[1] == p && b[2] == r)
        {
            c[0] = 'S', c[1] = 'P', c[2] = 'R';
            res3 = gao(k);
        }
          
        printf("Case #%d: ", cas);
        if(res1.size() != 0 || res2.size() != 0 || res3.size() != 0)
        {
            string ans = "";
            if(ans.size() == 0 || (res1.size() != 0 && res1 < ans)) ans = res1;
            if(ans.size() == 0 || (res2.size() != 0 && res2 < ans)) ans = res2;
            if(ans.size() == 0 || (res3.size() != 0 && res3 < ans)) ans = res3;
            cout << ans;
            puts("");
        }
        else
        {
            puts("IMPOSSIBLE");
        }
    }
    return 0;
}
