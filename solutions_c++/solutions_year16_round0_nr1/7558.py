#include <iostream>
using namespace std;

bool Checkflag(bool f[]) {
    for(int i=0;i<10;++i)
        if(f[i]==false)
            return false;
    return true;
}
void Makeflag(bool f[], int N) {
    while(N) {
        f[N%10] = true;
        N = N/10;
    }
}

int main()
{
    int T,N;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&T);
    for(int i=1;i<=T;++i) {
        bool flag[10] = {false};
        printf("Case #%d: ",i);
        scanf("%d",&N);
        if(N == 0) {
            printf("INSOMNIA\n");
            continue;
        }
        for(int j=1;j<100;++j) {
            Makeflag(flag, j*N);
            if(Checkflag(flag)) {
                printf("%d\n",j*N);
                break;
            }
        }
    }
    return 0;
}
