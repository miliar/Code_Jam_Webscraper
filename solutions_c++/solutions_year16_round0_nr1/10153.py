#include <bits/stdc++.h>
#define fr(a, b, c) for(int a = b; a < c; ++a)
#define sc(a) scanf("%d", &a)

using namespace std;

int vis[10];

int main()
{
    int cases, cnt = 0;
    sc(cases);
    int conta = 0, iter = 0;
    long long int a;
    while (cases--) {
        memset(vis, 0, sizeof vis);
        scanf("%lld", &a);
        if (!a) {
            printf("Case #%d: INSOMNIA\n", ++cnt);
            continue;
        }
        const long long int ka = a;
        bool nice = false;
        while (!nice) {
            string str = to_string(a);
            int tam = str.size();
            fr(i, 0, tam) vis[(int)str[i]-'0']++;
            fr(i, 0, 10) if(vis[i] > 0) conta++;
            if (conta == 10) nice = true;
            else a += ka;
            iter++;
            conta = 0;
        }
        printf("Case #%d: %lld\n", ++cnt, a);
        iter = 0;
    }
    return 0;
}