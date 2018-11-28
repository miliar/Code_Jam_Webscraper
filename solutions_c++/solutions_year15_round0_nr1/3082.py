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

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    li t, n, i, cnt = 0;
    string str;
    cin >> t;
    while(t--){
        cin >> n;
        cin >> str;
        li sum = 0, ans = 0;
        for(i = 0;i < str.size(); ++i){
            if(i <= sum && str[i] != '0'){
                sum += str[i] - '0';
            }
            else if(str[i] != '0'){
                ans += i - sum;
                sum += i - sum;
                sum += str[i] - '0';
            }
        }
        printf("Case #%lld: %lld\n", ++cnt, ans);
    }
}
