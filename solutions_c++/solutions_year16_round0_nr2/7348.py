#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    char s[102];
    freopen("B-large.in","r",stdin);
    freopen("output2.txt","w",stdout);
    scanf("%d",&t);
    int p=1;
    while(t--){
        scanf("%s",s);
        bool h=0;
        int n = strlen(s);
        int o=0;
        for(int i=0;i<n;i++){
            if(s[i]=='+'&&h==0&&i){
                o+=1;
            }
            else if(s[i]=='-'&&h==1&&i){
                o+=1;
            }
            if(s[i]=='+'){
                h=1;
            }
            else if(s[i]=='-'){
                h=0;
            }
        }
        if(h==0){
            o+=1;
        }
        printf("Case #%d: %d\n",p,o);
        p++;
    }
}
