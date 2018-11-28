#include <iostream>
#include <climits>
using namespace std;

int f[1000001];

int reverse(int x) {
    int tmp = 0;
    while(x) {
        tmp = tmp*10 + x%10;
        x /= 10;
    }
    return tmp;
}

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    int T,N;
    cin >> T;
    for(int i=1;i<=T;++i) {
        cin >> N;
        for(int j=0;j<=1000000;++j)
            f[j] = j;
        for(int j=1;j<=N;++j)
            f[j] = min(f[j-1]+1,j%10?f[reverse(j)]+1:INT_MAX);
        printf("Case #%d: %d\n",i,f[N]);
    }
    return 0;
} 
