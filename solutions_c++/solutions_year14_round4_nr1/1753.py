#include<iostream>
#include<cstring>
#include<algorithm>
#include <cstdio>
using namespace std;
const int maxn = 10005;
int s[maxn];
int main(){
    int t,n,x,nc=0;
    cin >> t;
    while(t--){
        printf("Case #%d: ",++nc);
        scanf("%d%d",&n,&x);
        for(int i = 0; i < n; i++){
           scanf("%d",&s[i]);
        }
        sort(s,s+n);
        int a = 0,b = n-1,ans = 0;
        while(a<=b){
            if(s[a] + s[b] <= x){
                a++;
            }
            b--;
            ans++;
        }
        printf("%d\n",ans);
    }
    return 0;
}
