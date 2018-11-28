#include<cstdio>
#include<cstring>
using namespace std;
bool a[10] = {false};
bool judge(int n,int &cnt){
    while(n){
        if (a[n%10] == false){
            a[n%10] = true;
            cnt--;
        }
        n/=10;
    }
    if(cnt == 0) return true;
    return false;
}
int main(){
    freopen("A.in","r",stdin);
    freopen("A.txt","w",stdout);
    int T,n;
    scanf("%d",&T);
    int kase = 0;
    while(T--){
        memset(a,false,sizeof(a));
        scanf("%d",&n);
        int cnt = 10,cnt2=0;
        int tmp = n;
        while(judge(tmp,cnt)==false){
            cnt2++;
            tmp += n;
            if(cnt2 == 10000) break;
        }
        if (cnt2 == 10000) printf("Case #%d: INSOMNIA\n",++kase);
        else printf("Case #%d: %d\n",++kase,tmp);
    }
    return 0;
}
