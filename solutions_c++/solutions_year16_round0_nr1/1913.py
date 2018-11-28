#include <bits/stdc++.h>

using namespace std;
#define pb push_back
#define PB pop_back
#define fs first
#define se second
#define eps (1e-8)
#define INF (0x3f3f3f3f)

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> P;

#define less asdfa
int cnt[15];
int n;
int T;
int cas=0;
int main(){
    freopen("/home/cwind/CppFiles/in","r",stdin);
    freopen("/home/cwind/CppFiles/out","w",stdout);
    cin>>T;
    while(T--){
        printf("Case #%d: ",++cas);
        scanf("%d",&n);
        memset(cnt,0,sizeof cnt);
        int less=10;
        if(n==0){
            puts("INSOMNIA");
            continue;
        }
        for(int i=1;;i++){
            ll x=(ll)i*n;
            if(x<10){
                cnt[x]++;
                if(cnt[x]==1) less--;
            }else{
                if(x%10==0){
                    cnt[0]++;
                    if(cnt[0]==1) less--;
                }
                for(;x>0;x/=10){
                    cnt[x%10]++;
                    if(cnt[x%10]==1) less--;
                }
            }
            if(less==0){
                printf("%d\n",i*n);
                break;
            }
        }
        less=0;

    }
    return 0;
}