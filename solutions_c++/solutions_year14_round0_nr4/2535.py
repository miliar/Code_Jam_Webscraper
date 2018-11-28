#include <cstdio>
#include <algorithm>
using namespace std;
#define REP(n,i) for(int i=0;i<n;i++)
const int N=1010;
double a[N];
double b[N];
int cc[N];
int QQ[N];

int main(){
    int T,c=0;
    freopen("d.in","r",stdin);
    freopen("d.out","w",stdout);
    scanf("%d",&T);
    while(c++<T){
        
        int x,y;
        int n;
        scanf("%d",&n);
        REP(n,i)scanf("%lf",&a[i]);
        REP(n,i)scanf("%lf",&b[i]);
        sort(a,a+n);
        sort(b,b+n);
        int ans=n;
        int index=0;
        REP(n,i){
            while(index!=n&&b[index]<a[i]){
                index++;
            }
            ans=min(n-1-i+index,ans);
        }
        int ans1=n;
        index=0;
        REP(n,i){
            while(index!=n&&a[index]<b[i]){
                index++;
            }
            ans1=min(n-1-i+index,ans1);
        }
        //printf("%d\n",ans1);
        
        
        printf("Case #%d: %d %d\n",c,ans,n-ans1);
        
    }
}
