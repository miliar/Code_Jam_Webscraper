#include<cstdio>
#include<cstring>
#include<set>
using namespace std;

const int N = 10005;

#define fo(i , st , en) for (int i = st; i <= en; i++)
#define Me(x , y) memset(x , y , sizeof(x))

struct _two{
    int a , b;
};

bool operator < (const _two &x , const _two &y){
    if (x.a != y.a) return x.a < y.a;
    return x.b < y.b;
}

set<_two> b;
int a[N];
int n , t , x;

void Init(){
    scanf("%d%d" , &n , &x);
    fo (i , 1 , n) scanf("%d" , a + i);
    b.clear();
    fo (i , 1 , n) b.insert((_two){a[i] , i});
}

void Work(){
    int num = 0;
    fo (i , 1 , n)
        if (!b.empty()){
            set<_two>::iterator temp = b.begin();
            int tt = temp->a; b.erase(temp);
            if (!b.empty()){
                set<_two>::iterator t1 = b.upper_bound((_two){x - tt , n + 1});
                if (t1 != b.begin()){
                    t1--; b.erase(t1);
                }
            }
            num++;
        }
        else break;
    printf("%d\n" , num);
}

int main(){
    freopen("0.in" , "r" , stdin);
    freopen("0.out" , "w" , stdout);
    scanf("%d" , &t);
    fo (i , 1 , t){
        Init();
        printf("Case #%d: " , i);
        Work();
    }
    return 0;
}
