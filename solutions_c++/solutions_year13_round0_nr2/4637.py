#include<cstdio>
#include<cstring>
using namespace std;

const int N = 105;

#define fo(i , st , en) for (int i = st; i <= en; i++)
#define mymax(x , y) ((x) > (y) ? (x) : (y))
#define Me(x , y) memset(x , y , sizeof(x))

struct _three{
    int a , b , c;
    inline void Input(int A , int B , int C){
        a = A; b = B; c = C;
    }
}qu[N * N];

int ch[N][N];
int l[N] , r[N];
int n , m , t;

int main(){
    freopen("b.in" , "r" , stdin);
    freopen("b.out" , "w" , stdout);
    scanf("%d" , &t);
    fo (p , 1 , t){
        printf("Case #%d: " , p);
        scanf("%d%d" , &n , &m);
        int x , tot = 0; Me(l , 0); Me(r , 0); 
        fo (i , 1 , n)
            fo (j , 1 , m){
                scanf("%d" , &x); ch[i][j] = x; l[i] = mymax(l[i] , x); r[j] = mymax(r[j] , x);
            }
        bool flag = 0;
        fo (i , 1 , n)
            fo (j , 1 , m)
                if (l[i] > ch[i][j] && r[j] > ch[i][j]) flag = 1;
        if (flag) puts("NO"); else puts("YES");
    }
    return 0;
}
