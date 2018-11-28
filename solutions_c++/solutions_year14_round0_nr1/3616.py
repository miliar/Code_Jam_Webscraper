#include<cstdio>
#define PI acos(-1.0)
using namespace std;
#define MAXN 100005
#define eps 1e-5
#define INF 0x7FFFFFFF

int a[5],b[5];
int main()
{
    freopen ("A-small-attempt6.in", "r", stdin);
    freopen ("A-small-attempt6.out", "w", stdout);
    int t,n,m,i,j;
    int kk=1;
    scanf("%d",&t);
    while(t--){
        scanf("%d",&n);
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                int temp;
                scanf("%d",&temp);
                if(i+1==n){
                    a[j] = temp;
                }
            }
        }
        scanf("%d",&m);
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                int temp;
                scanf("%d",&temp);
                if(i+1==m){
                    b[j] = temp;
                }
            }
        }
        int p;
        int flag = 0;
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(a[i]==b[j]){
                    flag++;
                    p = a[i];
                }
            }
        }
        printf("Case #%d: ",kk++);
        if(flag==0) printf("Volunteer cheated!\n");
        if(flag==1) printf("%d\n",p);
        if(flag>1)  printf("Bad magician!\n");
    }
    return 0;
}
