#include <cstdio>

using namespace std;

int n;
char a[1005];
int s[1005];

bool check(int x){
    int now= s[0]+x;
    for(int i=1;i<=n;i++){
        if(now<i) return false;
        now+= s[i];
    }
    return true;
}

int main(){
    freopen("Qua_A(large).in","r",stdin);
    freopen("Qua_A.out","w",stdout);
    int test, cnt= 0; scanf("%d", &test);
    while(test--){
        scanf("%d%s", &n, a+1);
        for(int i=0;i<=n;i++) s[i]= a[i+1]-'0';
        int l= 0, r= 1005, mid;
        while(l<r){
            mid= (l+r)/2;
            if(check(mid)) r= mid;
            else l= mid+1;
        }
        cnt++; printf("Case #%d: %d\n", cnt, l);
    }
    return 0;
}
