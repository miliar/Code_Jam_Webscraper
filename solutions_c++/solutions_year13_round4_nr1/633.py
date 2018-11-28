#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

typedef long long ll;

const int N = 1005 , mod = 1000002013;

#define fo(i , st , en) for (int i = st; i <= en; i++)
#define mymin(x , y) ((x) < (y) ? (x) : (y))
#define Me(x , y) memset(x , y , sizeof(x))

struct _three{
    int a , b , c;
    _three(int A , int B , int C) : a(A) , b(B) , c(C) {}
    _three(){}
}a[N + N];

struct _two{
    int a , b;
    _two(int A , int B) : a(A) , b(B) {}
    _two(){}
}stack[N];

bool operator < (const _three &x , const _three &y){
    return x.a < y.a || x.a == y.a && x.c < y.c;
}

int n , m , t , ans;

void Init(){
    scanf("%d%d" , &n , &m); int x , y , z; ans = 0;
    fo (i , 1 , m){
        scanf("%d%d%d" , &x , &y , &z);
        ans = (ans + (ll)(n + n - y + x + 1) * (y - x) / 2 % mod * z) % mod;
        a[i] = _three(x , z , 0); a[i + m] = _three(y , z , 1);
    }
    sort(a + 1 , a + m + m + 1);
}

void Work(){
    int tot = 0;
    fo (i , 1 , m + m)
        if (!a[i].c)
            stack[++tot] = _two(a[i].a , a[i].b);
        else{
            while (a[i].b){
                int num = mymin(a[i].b , stack[tot].b);
                ans = (ans - (ll)(n + n - a[i].a + stack[tot].a + 1) * (a[i].a - stack[tot].a) / 2 % mod * num) % mod;
                a[i].b -= num; stack[tot].b -= num;
                if (!stack[tot].b) tot--;
            }
        }
    printf("%d\n" , (ans + mod) % mod);
}

int main(){
    freopen("A.in" , "r" , stdin);
    freopen("A.out" , "w" , stdout);
    scanf("%d" , &t);
    fo (i , 1 , t){
        printf("Case #%d: " , i);
        Init();
        Work();
    }
    return 0;
}
