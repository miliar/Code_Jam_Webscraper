#include <iostream>
#include <algorithm>
#include <cstdio>
using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("outputL.out","w",stdout);

    int T,runn;
    cin >> T;

    int r,c,w;
    int ans;

    for(runn=1;runn<=T;runn++){
        cin >> r >> c >> w;

        ans=((r-1)*(c/w)) + ((c/w)-1) + w;
        if(c%w!=0) ans+=1;

        printf("Case #%d: %d\n",runn,ans);

    }
}
