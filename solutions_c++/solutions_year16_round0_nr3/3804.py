#include <cstdio>
#include <cstdlib>
#include <cstring>

using namespace std;

typedef long long LL;

int N, J;
LL ans[505], anscnt, performans;
int ansarr[15];
LL pow[15][20];

bool notp[100005];
int p[100005], pcnt;
void preproce() {
    memset(notp,0,sizeof(notp));
    notp[0] = notp[1] = true;
    pcnt = 0;
    for ( int i = 2 ; i <= 100000 ; ++i ) {
        if ( notp[i] == false ) {
            p[pcnt++] = i;
            for ( int j = 2 ; i*j <= 100000 ; ++j ) {
                notp[i*j] = true;
            }
        }
    }

    for ( int i = 2 ; i <= 10 ; i ++ ) {
        LL tmp = 1;
        pow[i][0] = tmp;
        for ( int j = 1 ; j <= 20 ; j ++ ) {
            tmp *= i;
            pow[i][j] = tmp;
        }
    }
}

bool check( LL num ) {
    int i, j, deg;
    LL tmpn = num, tmp;
    for ( i = 2 ; i <= 10 ; ++i ) {
        deg = tmp = 0;
        tmpn = num;
        while ( tmpn != 0 ) {
            tmp += (tmpn%2)*(pow[i][deg++]);
        tmpn /= 2;
        }
        performans = tmp;
        for ( j = 0 ; j < pcnt; ++j ) {
            if ( tmp%p[j] == 0 ) {
                ansarr[i] = p[j];
                break;
            }
        }
        if ( j == pcnt || tmp == p[j] ) return false;
    }
    return true;
}


void tryit() {
    int i;
    LL siz = (1<<(N-2)); // random size;
    LL orig = (1<<(N-1))+1;
    LL num = orig+(rand()%siz)*2;
    if ( check(num) == true ) {
        for ( i = 0 ; i < anscnt ; ++i ) {
            if ( num == ans[i] ) break;
        }
        if ( i == anscnt ) {
            printf("%lld ",performans);
            for ( int j = 2 ; j <= 10 ; ++j ) {
                printf("%d ",ansarr[j]);
            }
            printf("\n");
            ans[anscnt++] = num;
        }
    }
}


int main() {
    freopen("C-small-attempt2.in","r",stdin);
    freopen("C-small-attempt2.out","w",stdout);
    preproce();
    int t, T;
    scanf("%d",&T);
    for ( t = 1 ; t <= T ; ++t ) {
        anscnt = 0;
        scanf("%d %d",&N,&J);
        printf("Case #%d:\n",t);
        while ( anscnt != J ) tryit();
    }
    return 0;
}
