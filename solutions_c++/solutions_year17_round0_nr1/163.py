#include <bits/stdc++.h>
#define N 1009
using namespace std;

char a[N];
bool check(){
    for(int i=0;a[i];i++){
        if(a[i]=='-') return false;
    }
    return true;
}

void flip(int i){
    a[i] = (a[i]=='+'?'-':'+');
}

void solve(int tc){
    printf("Case #%d: ",tc);
    int k; scanf("%s%d",a,&k);
    int ans=0, n=strlen(a);
    for(int i=0;i+k<=n;i++){
        if(a[i]=='+') continue;
        ans++;
        for(int j=i;j<i+k;j++){
            flip(j);
        }
    }
    if(check()) printf("%d\n",ans);
    else printf("IMPOSSIBLE\n");
}

int main()
{
    freopen("A-large.in","r",stdin); freopen("out.txt","w",stdout);
    int T; scanf("%d",&T);
    for(int tc=1;tc<=T;tc++){
        solve(tc);
    }
    return 0;
}
