#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;
#define inf 0x3f3f3f3f

int x,v[10];
int main(){
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T,cas=0;
    cin>>T;
    while (T--)
    {
        memset(v,0,sizeof v);
        cin>>x;
        printf("Case #%d: ",++cas);
        int cnt=0;
        for (int i=1;i<=1000;i++){
            int p=x*i;
            while (p){
                int digit=p%10;
                if (!v[digit]) {v[digit]=1;cnt++;}
                p/=10;
            }
            if (cnt==10){
                printf("%d\n", x*i);
                break;
            }
        }
        if (cnt<10) puts("INSOMNIA");
    }
}
