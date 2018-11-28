#include <bits/stdc++.h>

using namespace std;

typedef long long int li;

#define mod 1000000007
#define MAXN 100015

#define getcx getchar
inline void inp( li &n )//fast input function
{
n=0;
li ch=getcx();li sign=1;
while( ch < '0' || ch > '9' ){if(ch=='-')sign=-1; ch=getcx();}
while( ch >= '0' && ch <= '9' )
n = (n<<3)+(n<<1) + ch-'0', ch=getcx();
n=n*sign;
}

li a[1024];

int main() {
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    li i, j;

    li t, cnt = 0;

    cin >> t;

    while(t--){
        li n;
        cin >> n;
        for(i = 0;i < n; ++i){
            cin >> a[i];
        }

        li ans = 1000000000000000ll;
        li cur = 0;

        for(i = 1;i <= 1024; ++i){
            li cur = 0;
            for(j = 0;j < n; ++j){
                if(a[j] > i){
                    if(a[j] % i == 0)
                        cur += (a[j] / i);
                    else
                        cur += ((a[j] / i) + 1);
                    --cur;
                }
            }
            ans = min(ans, cur + i);
        }

        printf("Case #%lld: %lld\n", ++cnt, ans);

    }

}
