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

int T;
int cas=0;
char s[10000];
int a[100000];
void rf(int p){
    reverse(a,a+p);
    for(int i=0;i<p;i++) a[i]^=1;
}
int main(){
    freopen("/home/cwind/CppFiles/in","r",stdin);
    freopen("/home/cwind/CppFiles/out","w",stdout);
    cin>>T;
    while(T--){
        scanf("%s",s);
        int len=strlen(s);
        for(int i=0;i<len;i++){
            if(s[i]=='-') a[i]=0;
            else a[i]=1;
        }
        int cnt=0;
        for(int i=len-1;i>=0;i--){
            if(a[i]==0){
                if(i>0&&a[0]==1){
                    int p=0;
                    while(a[p]==1&&p<i) p++;
                    rf(p);
                    cnt++;
                }
                rf(i+1);
                cnt++;
            }
        }
        printf("Case #%d: %d\n",++cas,cnt);
    }
    return 0;
}