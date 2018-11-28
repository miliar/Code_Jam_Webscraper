#include<cstdio>
#include<iostream>
#include<cmath>
#include<algorithm>
#include<cstring>
#include<cstdlib>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include<string>

using namespace std;

int T;
int n;
char s[1007];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d",&T);
    for (int cas=1;cas<=T;cas++){
            scanf("%d",&n);
            scanf("%s",s);
            int now_stand=0;
            int ans=0;
            for (int i=0;i<=n;i++){
                    int x=s[i]-'0';
                    if (x==0) continue;
                    if (now_stand>=i)
                        now_stand+=x;
                    else{
                        ans+=i-now_stand;
                        now_stand=i+x;
                    }
            }
            printf("Case #%d: %d\n",cas,ans);
    }
    return 0;
}
