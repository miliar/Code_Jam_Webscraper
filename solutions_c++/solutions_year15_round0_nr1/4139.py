#include<bits/stdc++.h>
#define pb push_back
#define mp make_pair
using namespace std;
char arr[1501]={NULL};
int main(){
    short t;
    scanf("%hd",&t);
    int tc=0;
    while(t--){
    	int n;
    	scanf("%d",&n);
        scanf("%s",arr);
        int ans=0;
        int cur=0;
        for(int i=0;i<=n;++i){
        	if(cur>=i){
        		cur+=arr[i]-'0';
        	}
        	else if(arr[i]!='0'){
        		ans+=i-cur;
                cur+=i-cur;
        		cur+=arr[i]-'0';
        	}
        }
        printf("Case #%d: %d\n",++tc,ans);
    }
}
