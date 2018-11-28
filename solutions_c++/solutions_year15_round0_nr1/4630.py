#include <iostream>     // std::cout
#include <algorithm>    // std::lower_bound, std::upper_bound, std::sort
#include <vector>       // std::vector
#include <cstdio>
#include <cstring>
typedef long long LL;
using namespace std;

int n,m;
char str[1111];
int num[1111];
bool input(){
    scanf("%d",&n);
    scanf("%s",str);
    n++;
}

void solve(){
    for(int i=0; i<n; i++)num[i]=str[i]-'0';
    int ans=0;
    for(int i=0,pre=0; i<n; i++){
        //printf("%d %d\n",pre,i);
        if(pre<i){
            ans+= i-pre;
            pre=i;
        }
        pre+= num[i];

    }
    static int cas=1;
    printf("Case #%d: %d\n",cas++,ans);
}

int main () {
    int zz=1;
    scanf("%d",&zz);
    while(zz--){
        input();
        solve();
    }
    return 0;
}
/*
011
011

011
110

*/
