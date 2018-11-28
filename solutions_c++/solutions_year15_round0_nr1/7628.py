#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    int cnt=1;
    scanf("%d",&t);
    int num[1010];
    while(t--){
        int n;
        scanf("%d",&n);
        for(int i=0;i<=n;i++){
            char c;
            cin>>c;
            num[i]=c-'0';
        }
        int ans=0;
        int level=num[0];
        for(int i=1;i<=n;i++){
            if(i>level){
                ans+=i-level;
                level=i;
            }
            level+=num[i];
        }
        printf("Case #%d: %d\n",cnt++,ans);
    }
    return 0;
}
