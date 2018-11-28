#include<bits/stdc++.h>
using namespace std;

int main()
{
    freopen("B-large(1).in","r",stdin);
    freopen("B-smallHai.out","w",stdout);
    int t,i,j,l,pos,ans,co;
    char s[105],c;
    scanf("%d",&t);
    for(j=1;j<=t;j++){
        co = 0;
        scanf("%s",s);
        l = strlen(s);
        pos = l-1;
        if(l == 1){
            if(s[0] == '+')
                ans = 0;
            else
                ans = 1;
        }
        else{
            ans = 0;
            while(1){
                c = s[0];
                pos = l-1;
                co = 0;
                for(i=0;i<l;i++){
                    if(s[i] == '+')
                        co++;
                }
                if(co == l)
                    break;
                for(i=1;i<l;i++){
                    if(c!=s[i]){
                        pos = i-1;
                        break;
                    }
                }
                for(i=0;i<=pos;i++){
                    if(s[i] == '+'){
                        s[i] = '-';
                    }
                    else
                        s[i] = '+';
                }


                ans++;
            }
        }
        printf("Case #%d: %d\n",j,ans);
    }
    return 0;
}
