#include<bits/stdc++.h>

using namespace std;

int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t,siz,i,n;
    char str[1010];
    scanf("%d",&t);
    long long ans=0,sum=0;
    for(int tt=1;tt<=t;tt++){
        ans=0;
        sum=0;
        scanf("%d",&n);
        scanf("%s",str);

        for(i=0;i<n+1;i++){
            if((str[i]-'0')<1)
                continue;
            if(sum<i){
                ans+= i-sum;
                sum+=ans;
            }
            sum+=(str[i]-'0');
        }
        cout << "Case #" << tt << ": " << ans << endl;
    }
    return 0;
}
