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
    ll t,n,i,x,y,tc=0,maxdiff;
    sl(t);
    while(t--){
        sl(n);
        x=0; y=0;
        ll arr[n];
        sl(arr[0]);
        maxdiff = -1;
        for(i=1;i<n;i++){
        	sl(arr[i]);
        	if(arr[i]<arr[i-1])
        		x+=(arr[i-1]-arr[i]);
        	if(arr[i]<=arr[i-1])
        		maxdiff = max(maxdiff,arr[i-1]-arr[i]);
        }
        for(i=0;i<n-1;i++)
        	if(arr[i]>=maxdiff)
        		y+=maxdiff;
        	else
        		y+=arr[i];
        printf("Case #%lld: %lld %lld\n",++tc,x,y);
    }
    return 0;
}
