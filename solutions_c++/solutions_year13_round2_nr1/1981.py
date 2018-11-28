#include<cstdio>
#include<algorithm>
using namespace std;
int a[110];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("textA.out","w",stdout);
    int T,ca=1;
    int n,i,j;
    int sum,d,k;
    int A;
    scanf("%d",&T);
    while(T--){
        scanf("%d%d",&A,&n);
        for(i=0;i<n;i++)
        scanf("%d",&a[i]);
        sort(a,a+n);
        if(A==1){printf("Case #%d: %d\n",ca++,n);continue;}
        j=0;
        sum=0;
        d=n;
        while(j<n){
            if(A>a[j]){A+=a[j];j++;}
            else {
                d=min(d,sum+n-j);
                A=2*A-1;
                sum++;
            }
        }
        printf("Case #%d: %d\n",ca++,min(d,sum));
    }
    return 0;
}
