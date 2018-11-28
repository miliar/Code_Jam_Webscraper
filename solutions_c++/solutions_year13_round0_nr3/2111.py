#include<cstdio>
#include<cstring>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<string>
#include<map>
#include<set>
using namespace std;
#define ll __int64
int c[1000];

bool huiwen(ll a)
{
     int j, i = 0;
     while (a){
           c[i++] = a % 10;
           a /= 10;
     }
     for (j = 0; j < i / 2; j++)
         if (c[j] != c[i - 1 - j]) return false;
     return true;
}

int main()
{
    freopen("C.in", "r", stdin);
    freopen("C.out", "w", stdout);
    int i, ans;
    ll a, b;
    int ts, ks;
    scanf("%d", &ts);
    for (ks = 0; ks < ts; ks++){
        scanf("%I64d %I64d", &a, &b);
        ans = 0;
        for (int i = int(sqrt(a)); i <= int(sqrt(b)) + 1; i++){
            if (i * i < a || i * i > b) continue;
            if (huiwen(i) && huiwen(i * i))
               ans++;
        }
        printf("Case #%d: %d\n", ks + 1, ans); 
    }
}
