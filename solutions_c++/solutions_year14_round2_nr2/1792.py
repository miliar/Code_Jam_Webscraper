#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
int a,b,k;
int T;
int main(){
    freopen("B-small-attempt0.in","r",stdin);
    freopen("out2.txt","w",stdout);
    cin>>T;
    for(int cas=1;cas<=T;++cas){
            scanf("%d %d %d",&a,&b,&k);
            int tot=0;
            for(int i=0;i<a;++i)
                    for(int j=0;j<b;++j)
                            if((i&j)<k)
                               tot++;
            printf("Case #%d: ",cas);
            printf("%d\n",tot);
    }
    return 0;
}
