#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output1.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int cs=1;cs<=t;cs++) {
        int n;
        char s[1009];
        scanf("%d%s",&n,s);
        int invite=0;
        int total=s[0]-'0';
        for(int i=1;i<=n;i++) {
            invite += max(0,i-total-invite);
            total+=s[i]-'0';
        }
        printf("Case #%d: %d\n",cs,invite);
    }
    return 0;
}
