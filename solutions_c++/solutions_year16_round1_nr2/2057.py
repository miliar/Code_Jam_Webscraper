#include <cstdio>
#include <algorithm>


using namespace std;

typedef struct H{
    int h[50];
    int n;
}H;

bool cmp(H a, H b)
{
    for(int i=0;i<a.n;i++){
        if(a.h[i]<b.h[i])
            return true;
    }

    return false;
}

int main(void)
{
    int cases,cas;
    int n;
    int hist[2550];
    int h[125][60];
    int ans[60];
    int cnt;

    for(int i=0;i<2550;i++)
        hist[i] = 0;

    scanf("%d",&cases);
    for(cas=1;cas<=cases;cas++){
        cnt = 0;
        scanf("%d",&n);
        for(int i=0;i<2550;i++)
            hist[i] = 0;

        for(int i=0;i<2*n-1;i++){
            for(int j=0;j<n;j++){
                scanf("%d",&h[i][j]);
                hist[h[i][j]]++;
            }
        }

        printf("Case #%d:",cas);
        for(int i=0;i<2550;i++){
            if(hist[i]!=0 && hist[i]%2==1){
              printf(" %d",i);
            }
        }
        printf("\n");

    }

    return 0;
}
