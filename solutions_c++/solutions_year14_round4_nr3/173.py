#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;

const int N = 1005 , inf = (int)1e9;

#define fo(i , st , en) for (int i = st; i <= en; i++)
#define Me(x , y) memset(x , y , sizeof(x))

struct _two{
    int x1 , y1 , x2 , y2;
}a[N];

int dis[N][N] , d[N];
bool flag[N];
int n , t , w , h;

void Init(){
    scanf("%d%d%d" , &w , &h , &n);
    fo (i , 1 , n)
        scanf("%d%d%d%d" , &a[i].x1 , &a[i].y1 , &a[i].x2 , &a[i].y2);
    Me(dis , 0);
    fo (i , 1 , n)
        fo (j , 1 , n)
            if (i != j){
                int temp1 = 0;
                if (a[i].x1 > a[j].x2) temp1 = a[i].x1 - a[j].x2 - 1;
                if (a[j].x1 > a[i].x2) temp1 = a[j].x1 - a[i].x2 - 1;
                int temp2 = 0;
                if (a[i].y1 > a[j].y2) temp2 = a[i].y1 - a[j].y2 - 1;
                if (a[j].y1 > a[i].y2) temp2 = a[j].y1 - a[i].y2 - 1;
                dis[i][j] = max(temp1 , temp2);
            }
    fo (i , 1 , n) dis[i][n + 1] = dis[n + 1][i] = a[i].x1;
    fo (i , 1 , n) dis[i][n + 2] = dis[n + 2][i] = w - a[i].x2 - 1;
    dis[n + 1][n + 2] = dis[n + 2][n + 1] = inf;
    
}

void Work(){
    Me(d , 127); d[n + 1] = 0; d[n + 2] = w; Me(flag , 0);
    fo (i , 1 , n + 2){
        int pos = 0;
        fo (j , 1 , n + 2)
            if (!flag[j] && d[j] < d[pos]) pos = j;
        if (!pos) break; flag[pos] = 1;
        fo (j , 1 , n + 2)
            if (!flag[j] && d[pos] + dis[pos][j] < d[j]) d[j] = d[pos] + dis[pos][j];
    }
    printf("%d\n" , d[n + 2]);
}

int main(){
    freopen("2.in" , "r" , stdin);
    freopen("2.out" , "w" , stdout);
    scanf("%d" , &t);
    fo (i , 1 , t){
        Init();
        printf("Case #%d: " , i);
        Work();
    }
    return 0;
}
