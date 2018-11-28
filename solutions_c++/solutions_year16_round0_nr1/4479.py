#include <cstdio>

using namespace std;

int Count( int n ) {
    if ( n == 0 ) return -1;
    bool used[10]={false};
    int i, tmp, tmpn = n;
    do {
        tmp = tmpn;
        while ( tmp != 0 ) {
            used[tmp%10] = true;
            tmp /= 10;
        }

        for ( i = 0 ; i < 10 && used[i] == true ; i ++ );
        if ( i == 10 ) break;

        tmpn += n;
    }
    while(1);

    return tmpn;
}


int main() {
    freopen("A-Large.in","r",stdin);
    freopen("A-Large.out","w",stdout);
    int T, t, n, ans;
    scanf("%d",&T);
    for ( t = 1 ; t <= T ; ++t ) {
        scanf("%d",&n);
        ans = Count(n);
        if ( ans == -1 ) printf("Case #%d: INSOMNIA\n",t);
        else printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
