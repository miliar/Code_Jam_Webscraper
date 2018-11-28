#include<cstdio>
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int main(){
    //freopen("input.in","r",stdin);
    //freopen("output.out","w",stdout);
    int T,tc=1; scanf("%d",&T);
    while(T--){
        int s_max,standing,ans=0;
        scanf("%d",&s_max);
        string s; cin >> s;
        standing = s[0]-48;
        for(int i=1; i<=s_max; i++){
            if(standing < i) {
                ans += (i-standing);
                standing += (i-standing);
            }
            standing += s[i]-48;
        }
        printf("Case #%d: %d\n",tc++,ans);
    }
    return 0;
}
