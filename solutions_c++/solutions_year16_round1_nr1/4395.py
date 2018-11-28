#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<vector>
#include<queue>
#define LL long long
#define maxn 100100
#define inf 0x3f3f3f3f
#define IN freopen("in.txt","r",stdin);
using namespace std;

string s;
int n;

void solve(int r){
    if(r < 1) return;
    int ma = 0;
    for(int i=0; i<r; i++)
        if(s[i] > ma) ma = s[i];
    int macnt = 0;
    int l = -1;
    for(int i=0; i<r; i++)
        if(s[i] == ma){
            if(l == -1) l = i;
            macnt++;
        }
    for(int i=1; i<=macnt; i++) putchar(ma);
    solve(l);
    for(int i=l; i<r; i++)
        if(s[i] != ma) putchar(s[i]);
}

int main(int argc, char const *argv[])
{
    IN;
    freopen("out.txt","w",stdout);

    int t,ca=1; cin >> t;
    while(t--)
    {
        cin >> s;
        int n = s.size();

        printf("Case #%d: ", ca++);
        solve(n);
        printf("\n");
    }

    return 0;
}


