#include<bits/stdc++.h>
using namespace std;
#define NSIZ 100010
#define mxint (-1u/2)
#define mxll (-1ull/2)
#define F first
#define S second
typedef pair<int,int> pii;

int n, m, o, re=0;
pii a[NSIZ], b[NSIZ];
bool chk[NSIZ];
int main(){
    int i, j, k, l;
    int test;
    scanf("%d", &test);
    for(int zz=1; zz<=test; zz++){
        scanf("%d", &n);
        for(i=0; i<n; i++){
            scanf("%d", &a[i].F);
            a[i].S=i;
        }
        sort(a,a+n);
        printf("Case #%d: ", zz);
        if(a[n-1].F-a[n-2].F>0){
            for(i=0; i<a[n-1].F-a[n-2].F; i++){
                printf("%c", 'A'+a[n-1].S);
            }
            printf(" ");
        }
        for(i=0; i<n-2; i++){
            while(a[i].F>0){
                a[i].F--;
                printf("%c ", 'A'+a[i].S);
            }
        }
        while(a[n-2].F>0){
            a[n-2].F--;
            printf("%c%c ", a[n-1].S+'A', a[n-2].S+'A');
        }
        printf("\n");
    }
    return 0;
}
