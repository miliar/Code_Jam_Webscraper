#include <stdio.h>
#include <stack>
#include <list>
#include <algorithm>
using namespace std;
int a[15];
int f[1005];
int main(){
    freopen("C-small-attempt0.in","r",stdin);
    freopen("Coutput.txt","w",stdout);
    int tc;
    scanf("%d",&tc);
    for(int t=1;t<=tc;t++){
        int n;
        scanf("%d",&n);
        for(int i=1;i<=n;i++){
            scanf("%d",&f[i]);
            a[i]=i;
        }
        int mx=1;
        do{
            for(int i=1;i<=n;i++){
                if(i==1){
                    if(f[a[i]]==a[i+1]){
                        mx=max(mx,i);
                    }
                    else{
                        break;
                    }
                }
                else if(i==n){
                    if(f[a[i]]==a[i-1]||f[a[i]]==a[1]){
                        mx=max(mx,i);
                    }
                    else{
                        break;
                    }
                }
                else{
                    if(f[a[i]]==a[i-1]||f[a[i]]==a[1]){
                            mx=max(mx,i);
                    }
                    if(f[a[i]]==a[i-1]||f[a[i]]==a[i+1]){

                    }
                    else{
                        break;
                    }
                }
            }
        }while(next_permutation(a+1,a+n+1));
        printf("Case #%d: %d\n",t,mx);
    }
}
