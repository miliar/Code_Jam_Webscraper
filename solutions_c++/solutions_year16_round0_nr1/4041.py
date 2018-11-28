#include <bits/stdc++.h>
using namespace std;

int main(){
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
    int t,n;
    scanf("%d",&t);
    for(int ca=1;ca<=t;ca++){
        scanf("%d",&n);
        printf("Case #%d: ",ca);
        set<int> s;
        if(n==0) puts("INSOMNIA");
        else{
            int nn=n;
            while(1){
                int x=n;
                while(x){
                    s.insert(x%10);
                    x/=10;
                }
                if(s.size()==10){
                    printf("%d\n",n);
                    break;
                }
                n+=nn;
            }
        }
    }
    return 0;
}
