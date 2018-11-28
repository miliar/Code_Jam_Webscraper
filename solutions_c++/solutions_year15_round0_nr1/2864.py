#include <cstdio>
int T,n;
char s[1013];
int main(){
    scanf("%d",&T);
    for (int Case=1;Case<=T;Case++){
        int ans=0;
        scanf("%d %s",&n,s);
        int x = (s[0]-'0');
        for (int i=1;i<=n;i++){
            if (x<i && s[i]!='0')ans+=(i-x), x+=(i-x);    
            x += (s[i]-'0');
        }   
        printf("Case #%d: %d\n",Case,ans); 
    }
    return 0;    
}
