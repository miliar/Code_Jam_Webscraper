// Aditya Varshney - coderaditya

#include <iostream>
#include <bitset>
#include <cmath>
#include <queue>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <map>
#include <climits>

#define pb push_back
#define mp make_pair

typedef long long int ll;

using namespace std;

#define getcx getchar//_unlocked

ll scan()
{
    ll n=0;
    char ch = getcx();
    int sign=1;
    while( ch < '0' || ch > '9' ) {
        if(ch=='-')
            sign = -1;
        ch=getcx();
    }
    while( ch >= '0' && ch <= '9' ) {
        n = (n<<3)+(n<<1) + ch-'0';
        ch=getcx();
    }
    return(n * sign);
}

int main()
{
    freopen("S.in","r",stdin);
    freopen("MYO.txt","w",stdout);
    int t,n,i,p=0;
    string s;
    t=scan();
    while(t--) {
        p++;
        n=scan();
        int a[n+1];
        cin>>s;
        for(i=0;i<=n;i++) {
            a[i]=s[i] - 48;
        }
        int ans = 0,clap = 0;
        for(i=0;i<=n;i++) {
            if(clap < i) {
                ans += (i-clap);
                clap = i;
                clap += a[i];
            } else {
                clap += a[i];
            }
        }
        printf("Case #%d: %d\n",p,ans);
    }
    return 0;
}
