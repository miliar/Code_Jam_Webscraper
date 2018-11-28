#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
using namespace std;
int main(){
    int tc;
    cin>>tc;
    for(int t=1;t<=tc;++t){
        int n;
        cin>>n;
        int arr[1001]={0};
        int mx = 0;
        int ans=1001;
        for(int i=1;i<=n;++i){
            scanf("%d",&arr[i]);
            mx = max(mx,arr[i]);
        }
        if(mx<=2){
            ans = mx;
        }
        else{
            for(int i = 1 ; i <= mx;++i){
            	int tm = 0;
            	for(int j=1;j<=n;++j){
            		tm += (arr[j]-1)/i;
            	}
            	tm+=i;
            	ans=min(ans,tm);
            }
        }
        printf("Case #%d: %d\n",t,ans);
    }   
}
