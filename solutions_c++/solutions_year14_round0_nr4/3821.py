#include <stdio.h>
#include <algorithm>
using namespace std;
int main(){
    int n;
    int a;
    //freopen("D-large.in","r",stdin);
    
    //freopen("D-large.out","w",stdout);
    float kao[1000],ken[1000],kao2[1000],ken2[1000];
    scanf("%d",&n);
    for(int i = 0; i < n;i++){
        scanf("%d",&a);
        for(int j = 0; j < a;j++){
            scanf("%f",&kao[j]);
            kao2[j] = kao[j];
        }
        for(int j = 0; j < a;j++){
            scanf("%f",&ken[j]);
            ken2[j] = ken[j]; 
        }    
        sort(kao,kao+a);
        sort(ken,ken+a);
        sort(kao2,kao2+a);
        sort(ken2,ken2+a);
        int ans,ans2;
        ans = ans2 = 0;
        
        for(int j = 0; j < a;j++){
            for(int k = 0; k < a;k++){
                if(kao[j] > ken[k]){
                    ken[k] = 99999;
                    ans++;
                    break;
                }
            }
        }
        for(int j = 0; j < a;j++){
            for(int k = 0; k < a;k++){
                if(kao2[j] < ken2[k]){
                    ken2[k] = 0;
                    ans2++;
                    break;
                }
            }
        }
        
        printf("Case #%d: %d %d\n",i+1,ans,a-ans2);
        
    }
    return 0;
}
