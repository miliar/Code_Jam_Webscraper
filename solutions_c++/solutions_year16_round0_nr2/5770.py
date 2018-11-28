#include<bits/stdc++.h>
using namespace std;
char s[100+10];
int l;
bool check(){
    for(int i=0;i<l;i++)
        if(s[i]=='-')return 1;
    return 0;
}
int main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,Case=0;
    scanf("%d",&T);
    while(T--){
        scanf("%s",s);
        l=strlen(s);
        int ans=0;
        for(int i=l-1;i>=0;i--){
            if(s[i]=='+')l--;
            else break;
        }
        while(l){
            if(s[0]=='+'){
                ans++;
                for(int i=0;i<l;i++){
                    if(s[i]=='+'){
                        s[i]='-';
                    }
                    else break;
                }
            }
            ans++;
            for(int i=0,j=l-1;i<j;i++,j--)swap(s[i],s[j]);
            for(int i=0;i<l;i++){
                if(s[i]=='+')s[i]='-';
                else s[i]='+';
            }
            for(int i=l-1;i>=0;i--)
                if(s[i]=='+')l--;
                else break;
        }
        printf("Case #%d: %d\n",++Case,ans);
    }
    return 0;
}
