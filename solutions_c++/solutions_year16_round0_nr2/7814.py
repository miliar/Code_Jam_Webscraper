#include<bits/stdc++.h>
using namespace std;
typedef long long int LL;
const int N=105;
bool check(char str[],int x,int n)
{
    for(int i=x;i<n;i++) if(str[i]=='0') return false;
    return true;
}
int main()
{
    freopen("input.in","r",stdin);
   freopen("output.out","w",stdout);

    int t;
    scanf("%d",&t);
    for(int tt=1;tt<=t;tt++){

        
        printf("Case #%d: ",tt);
        char str[N];
        scanf("%s",str);
        int n=strlen(str);

        for(int i=0;i<n;i++) 
            if(str[i]=='-') str[i]='0';
            else str[i]='1';

        
        int ans=0,x=0;
        int cur=str[0]-'0';
        while(!check(str,x,n)){
            int i=x;
            for(;i<n;i++){
                if(str[i]-'0'!=cur) break;
            }
            ans++;
            x=i;
            cur^=1;
        }
        printf("%d\n",ans);
    }
}