/* shakti11094 : Shakti Kheria */
#include<bits/stdc++.h>

#define ll long long
#define MP(a,b) make_pair(a,b)
#define PB(a) push_back(a)
#define fi first
#define se second
#define s(a) scanf("%d",&a);
#define sl(a) scanf("%lld",&a);
#define s64(a) scanf("%I64d",&a);
#define sf(a) scanf("%f",&a);
#define sd(a) scanf("%lf",&a);
#define sld(a) scanf("%llf",&a);
#define ss(a) scanf("%s",a);
#define fillin(a,b) memset(a,b,sizeof(a))
using namespace std;

int main(){
    ll t,tc=0,n,i,ans,total;
    sl(t);
    while(t--){
        sl(n);
        char s[1009];
        ss(s);
        total=s[0]-'0';
        ans=0;
        for(i=1;i<=n;i++){
        	//printf("curAns=%lld\n",ans);
        	if(s[i]=='0')
        		continue;
        	if(total<i){
        		ans+=(i-total);
        		total+=(i-total);
        	}
        	total+=(s[i]-'0');
        }
        printf("Case #%lld: %lld\n",++tc,ans);
    }
    return 0;
}
