/*
 Created by Saidolda Bayan.
 Copyright (c) 2015 Bayan. All rights reserved.
 LANG: C++
 */
#include <bits/stdc++.h>

#define _USE_MATH_DEFINES
#define y1 lalka
#define right napravo
#define left nalevo
#define pb push_back
#define mp make_pair
#define f first
#define s second

using namespace std;
using pii = pair<int, int>;
using ll = long long;

const int INF = (int)1e9+7, mod = (int)1e9+9, pw = 31, N = (int)1e5+123, M = (int)1e6+123;
const double eps = 1e-11;
const long long inf = 1e18;

int test, n;
bitset<10> used;
inline bool f(ll x){
    while(x){
        used[x%10] = 1;
        x /= 10;
    }
    return used.count() == 10;
}
int main ()
{
    freopen("A-large.in.txt","r",stdin);
    freopen("ans.txt","w",stdout);
    scanf("%d", &test);
    for(int c = 1; c <= test; c++){
        cerr<<c<<"\n";
        used.reset();
        scanf("%d", &n);
        bool check = 0;
        printf("Case #%d: ", c);
        for(int i=1; i<=100000; i++){
            if(f(1ll * i * n)){
                printf("%lld", 1ll * i * n);
                check = 1;
                break;
            }
        }
        if(!check)printf("INSOMNIA");
        printf("\n");
    }
    
    
    
    
    return 0;
}
