#include<stdio.h>
#include<stdlib.h>
#include<algorithm>
#include<string.h>
using namespace std;
double a[1010];
double b[1010];
bool used[1010];
void solve(){
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;++i)scanf("%lf",&a[i]);
    for(int i=0;i<n;++i)scanf("%lf",&b[i]);
    sort(a,a+n);
    sort(b,b+n);
    int dread=0;
    int war=0;
    memset(used,0,sizeof(used));
    for(int i = 0 ; i < n ; ++ i ){
        bool win=true;
        for(int j=0;j<n;++j){
            if(!used[j]&& b[j]>a[i]&& win){
                win=false;
                used[j]=true;
                break;
            }
        }
        if(win){
            for(int j = 0 ; j < n ; ++ j )
                if(!used[j]){
                    war++;
                    used[j]=true;
                    break;
                }
        }
    }
    int sa=0,ea=n-1,sb=0,eb=n-1;
    for(int i = 0 ; i < n ; ++ i ){
        if(a[sa]<b[sb]){
            sa++;
            eb--;
        }
        else{
            sa++;
            sb++;
            dread++;
        }
    }
    printf("%d %d\n",dread,war);

}
int main(){
    freopen("D-large.in","r",stdin);
    freopen("D.out","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i = 1 ; i <= t ; ++ i ){
        printf("Case #%d: ",i);
        solve();
    }
}
