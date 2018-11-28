#include <cstdio>
#define INF 10000000
int T,n;
int a[1013];
int main(){
    scanf("%d",&T);
    for (int Case=1;Case<=T;Case++){
        scanf("%d",&n);
        for (int i=0;i<n;i++)scanf("%d",&a[i]);
        int tmpans=0,ans=INF;
        for (int i=1;i<=1000 && i<=ans;i++){
            tmpans=0;
            for (int j=0;j<n;j++){
                if (i<a[j]){
                   tmpans += (a[j]-1)/i;            
                }
            }
            tmpans+=i;
            if (tmpans<ans) ans = tmpans;    
        }    
        printf("Case #%d: %d\n",Case,ans);
    }
    return 0;    
}
