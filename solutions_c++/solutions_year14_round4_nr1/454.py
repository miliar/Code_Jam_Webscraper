#include<iostream>
#include<cstdio>
#include<cstring>
#include<queue>
#include<map>
#include<algorithm>
#include<string>
using namespace std;
int a[10010];
int main(){
    int T;
    int cas;
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    cin>>T;
    for(cas = 1; cas <= T; cas++){
        int n,ans = 0,x;
        cin>>n>>x;
        for(int i = 1; i <= n; i++){
            scanf("%d",&a[i]);
        }
        sort(a+1,a+n+1);
        int left = 1,right = n;
        while(left <= right){
            if(left == right) {ans++;break;}
            if(a[left] + a[right] <= x){
                left++;
                right--;
                ans++;
            }else{
                right--;
                ans++;
            }
        }

        printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
