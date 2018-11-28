#include<fstream>
#define N 2000
#define MAX(x,y) ((x)>(y)?(x):(y))
#define MIN(x,y) ((x)<(y)?(x):(y))
using namespace std;
int T,sol,t[N],n,tt[N],a[N];
void processing();
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int i;
    scanf("%d",&T);
    for(i=1;i<=T;i++){
        processing();
        printf("Case #%d: %d\n",i,sol);
    }
    return 0;
}

void processing()
{
    int i,j,p,k;
    scanf("%d",&n);
    p=0;
    for(i=0;i<n;i++){
        scanf("%d",&a[i]);
        p=MAX(p,a[i]);
    }
    sol=p*n;
    for(i=1;i<=p;i++){
        k=0;
        for(j=0;j<n;j++){
            if(a[j]>i){
                k+=(a[j]/i);
                if(a[j]%i==0) k--;
            }
        }
        k+=i;
        sol=MIN(k,sol);
    }
}
