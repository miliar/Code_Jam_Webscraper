#include <stdio.h>
#include <string.h>

#define N 105
#define get_num(x) ((x)=='-'?0:1)

char a[N];
int n;

void process()
{
    scanf(" %s",&a[1]);
    n = strlen(&a[1]);

    int togle = 0;

    int ans = 0 ;
    for(int i=n; i>=1; i--) {
        if(!(togle^get_num(a[i]))) {
           ans++;
           togle ^= 1;
        }
    }

    printf("%d\n",ans);

}

int main()
{
    freopen("B-large.in","rt",stdin);
    freopen("output.txt","wt",stdout);

    int t;
    scanf("%d",&t);
    for(int i=1 ;i<=t; i++){
        printf("Case #%d: ",i);
        process();
    }
    return 0;
}
