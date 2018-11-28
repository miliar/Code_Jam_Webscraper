#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <iomanip>
#include <windows.h>

using namespace std;

#define mp(a,b) make_pair(a,b)
#pragma comment(linker, "/STACK:26777216")

const int mod = 1e9+7;
const double eps = 1e-8;
const int N = 1e5+3;
const double pi = acos(-1.0);
const int inf = 0x3f3f3f3f;

int gcd(int a,int b){return !b?a:gcd(b,a%b);}

struct union_set{

    int fa[103];

    void init(int n){
        for(int i=0;i<=n;i++)
            fa[i] = i;
        return ;
    }

    int getroot(int i){
        if(fa[i] != i)
            fa[i] = getroot(fa[i]);
        return fa[i];
    }

    void _union(int i,int j){
        fa[i] = j;
    }
};

int pow_mod(int a,int b,int c){

    long long ans = 1;

    while(b){
        if(b&1)
            ans = ans*a%c;
        a = 1ll*a*a%c;
        b >>= 1;
    }

    return ans%c;
}

/**
ID: xianbin5
PROG: charrec
LANG: C++
*/

// ofstream fout ("charrec.out");
// ifstream fin ("charrec.in");

char s[10003];

int main()
{
    int t;
    cin >> t;
    for(int i=1;i<=t;i++)
    {

        int n;
        cin >> n;
        scanf("%s",s);
        int now = 0;
        int ans = 0;
        for(int j=0;j<=n;j++)
            if(j<=now)
                now += s[j]-'0';
            else if(s[j]>'0')
            {
                ans += j - now;
                now = j + s[j]-'0';
            }
        printf("Case #%d: %d\n",i,ans);
    }
    return 0;
}
