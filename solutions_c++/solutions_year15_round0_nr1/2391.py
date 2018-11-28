#include <cstdio>
using namespace std;

int main(){
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int test;
    int cases=0;
    for(scanf("%d",&test);test>0;--test){
        int n;
        char S[1010];
        scanf("%d%s",&n,S);
        int res=0;
        int cnt=0;
        for(int i=0;i<=n;++i){
            if(!(S[i]-'0')) continue;
            if(cnt>=i) cnt+=(S[i]-'0');
            else{ res+=i-cnt; cnt=i+(S[i]-'0');}
        }
        printf("Case #%d: %d\n",++cases,res);
    }
    return 0;
}
