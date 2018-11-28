#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int N = 1005;

#define fo(i , st , en) for (int i = st; i <= en; i++)
#define Me(x , y) memset(x , y , sizeof(x))
#define lowbite(x) ((x) & -(x))

struct _two{
    int a , b;
}a[N];

bool operator < (const _two &x , const _two &y){
    return x.a > y.a;
}

int t , n;
int h[N];

void Init(){
    scanf("%d" , &n); int x;
    fo (i , 1 , n){
        scanf("%d" , &x); a[i] = (_two){x , i};
    }
    sort(a + 1 , a + n + 1);
}

void Ins(int x){
    for (; x <= n; x += lowbite(x)) h[x]++;
}

int Find(int x){
    int ret = 0;
    for (; x; x -= lowbite(x)) ret += h[x];
    return ret;
}

void Work(){
    int ans = 0; Me(h , 0);
    fo (i , 1 , n){
        int temp = Find(a[i].b);
        ans += min(temp , i - 1 - temp);
        Ins(a[i].b);
    }
    printf("%d\n" , ans);
}

int main(){
    freopen("1.in" , "r" , stdin);
    freopen("1.out" , "w" , stdout);
    scanf("%d" , &t);
    fo (i , 1 , t){
        Init();
        printf("Case #%d: " , i);
        Work();
    }
    return 0;
}
