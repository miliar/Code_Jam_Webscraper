#include<cstdio>
#include<cstring>
using namespace std;

typedef long long ll;

const int N = 55;

#define fo(i , st , en) for (int i = st; i <= en; i++)
#define fd(i , st , en) for (int i = st; i >= en; i--)
#define Me(x , y) memset(x , y , sizeof(x))

int t , n;
ll p;

ll check(ll need){
    fo (i , 0 , n)
        if ((1LL << n - i) <= need) return 1LL << i;
}

ll Calc(ll need){
    int cur = 0;
    if (need == 1LL << n) return need - 1;
    fo (i , 0 , n - 1){
        cur += 1LL << n - i - 1;
        if (cur >= need) return (1LL << i + 1) - 2;
    }
}

int main(){
    freopen("B.in" , "r" , stdin);
    freopen("B.out" , "w" , stdout);
    scanf("%d" , &t);
    fo (i , 1 , t){
        scanf("%d%I64d" , &n , &p);
        printf("Case #%d: %I64d %I64d\n" , i , Calc(p) , (1LL << n) - check(p));
    }
    return 0;
}
