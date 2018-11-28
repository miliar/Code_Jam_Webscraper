//#include <bits/stdc++.h>

#include<cstdio>
#include<cstring>
#include<cctype>
#include<cmath>
#include<cstdlib>

#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<bitset>
using namespace std;

#define popc(a) (__builtin_popcount(a))
//ll bigmod(ll a,ll b,ll m){if(b == 0) return 1%m;ll x = bigmod(a,b/2,m);x = (x * x) % m;if(b % 2 == 1) x = (x * a) % m;return x;}
//ll BigMod(ll B,ll P,ll M){ ll R=1%M; while(P>0) {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R;} /// (B^P)%M

#define MX 100005
#define inf 100000000

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;

const ll mod = 1000000007ll;

int arr[100];
char str[100000];
int res = 0;

int func(char value[100])
{
    int len = strlen(value);
    //puts("------");
    //puts(value);
    int mini = 10000000;
    //printf("len %d\n", len);
    for(int i = 0; i < len; i++)
    {
        mini = min(mini,arr[value[i]]);
    }
    //printf("mini %d\n", mini);
    if(strcmp(value,"THREE") == 0 || strcmp(value,"SEVEN") == 0)
    {
        mini = min(mini,arr['E']/2);
    }
    if(strcmp(value,"NINE") == 0)
    {
        mini = min(mini,arr['N']/2);
    }
    for(int i = 0; i < len; i++)
    {
        arr[value[i]] -= mini;
    }
    //for(int i = 'A'; i <= 'Z'; i++)
        //printf("%c %d\n", i, arr[i]);
    //puts("end->>>>");
    res += mini*len;
    return mini;
}

vector<char> vc;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int te, ti;
    scanf("%d", &ti);

    for(te = 1; te <= ti; te++)
    {
        memset(arr,0,sizeof arr);
        vc.clear();
        res = 0;
        scanf("%s", str);
        printf("Case #%d: ", te);
        int len = strlen(str);
        for(int i = 0; i < len; i++)
        {
            arr[str[i]]++;
        }
        int val = func("ZERO");
        //printf("val %d\n", val);
        for(int i = 0; i < val; i++)
            vc.push_back('0');

        val = func("TWO");
        //printf("val %d\n", val);
        for(int i = 0; i < val; i++)
            vc.push_back('2');

         val = func("FOUR");
        //printf("val %d\n", val);
        for(int i = 0; i < val; i++)
            vc.push_back('4');

         val = func("FIVE");
        //printf("val %d\n", val);
        for(int i = 0; i < val; i++)
            vc.push_back('5');

         val = func("SIX");
        //printf("val %d\n", val);
        for(int i = 0; i < val; i++)
            vc.push_back('6');

         val = func("SEVEN");
        //printf("val %d\n", val);
        for(int i = 0; i < val; i++)
            vc.push_back('7');

         val = func("EIGHT");
        //printf("val %d\n", val);
        for(int i = 0; i < val; i++)
            vc.push_back('8');

         val = func("NINE");
        //printf("val %d\n", val);
        for(int i = 0; i < val; i++)
            vc.push_back('9');

        val = func("ONE");
       // printf("val %d\n", val);
        for(int i = 0; i < val; i++)
            vc.push_back('1');

        val = func("THREE");
        //printf("val %d\n", val);
        for(int i = 0; i < val; i++)
            vc.push_back('3');

        sort(vc.begin(),vc.end());
        for(int i = 0; i < vc.size(); i++)
            putchar(vc[i]);

        puts("");
        if(res != len)
            puts("Not Ok ->>>");
    }
    return 0;
}


