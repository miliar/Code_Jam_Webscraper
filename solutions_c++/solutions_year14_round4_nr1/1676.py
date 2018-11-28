#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
int T;
int n, x, L;
int s[100000], v[100000];



int main(){
    int ans;
    scanf("%d", &T);
    for(int f=1;f<=T;f++){
        scanf("%d%d",&n,&x);
        for(int i=0;i<n;i++){
            scanf("%d",&s[i]);            
        }
        sort(s,s+n);
        ans = 0;
        L = 0;
        for(int i=n-1;i>=L;i--){
//            fprintf(stderr,"(%d,%d) (%d,%d)\n",i,s[i],L,s[L]);                    
            if(i==L){
                ans++;
            }else if(s[i] + s[L] <= x){
                ans++;
                L++;
            }else{
                ans++;                
            }
        }

        printf("Case #%d: %d\n", f, ans);
    }

    return 0;
}
