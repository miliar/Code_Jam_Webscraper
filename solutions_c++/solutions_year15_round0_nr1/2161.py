#include<iostream>
#include<cstdio>
#include<cstring>
using namespace std;
const int  N  = 1000+10;
char s[N];
int a[N];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int cas=0;
    while(t--){
        int n; cin>>n;
        int sum = 0,ans=0;
        scanf("%s",s);
        int len = strlen(s);
        for(int i=0;i<len;i++){
            int need = i;
            if(sum < need){
                ans += need-sum;
                sum = need;
                sum += s[i]-'0';
            }
            else sum+=s[i]-'0';
        }
        printf("Case #%d: ",++cas);
        cout<<ans<<endl;
    }
}
