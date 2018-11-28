#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <cstring>

using namespace std;

int main(){
    freopen("A-large.in","r",stdin);
    freopen("outputA.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int co=1;co<=t;co++){
        int len;
        char peo[1005];
        scanf("%d %s",&len,peo);
        int ans = 0;
        int temp = peo[0]-'0';
        for(int g=1;g<=len;g++){
            if(temp<g){
                ans+=(g-temp);
                temp = g;
            }
            temp+=(peo[g]-'0');
        }
        printf("Case #%d: %d\n",co,ans);

    }
    return 0;


}
