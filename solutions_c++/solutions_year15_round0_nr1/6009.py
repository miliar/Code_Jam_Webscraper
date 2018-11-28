#include<bits/stdc++.h>
using namespace std;
int main(){
   int t,r;
   freopen("ab.in","r",stdin);
	freopen("bc.out","w",stdout);
   cin>>t;
   r=t;
   while(t--){
   	int p,count=0;
   string a;
   cin>>p>>a;
   int dp[p+5],i,diff;
   dp[0] = a[0]-'0';
   if(a[0]=='0'){
   	count++;
   	a[0]=count;
   	dp[0]=a[0];
   }
   for(i=1;i< (a.length()+1);i++){
   	if(dp[i-1]>=i || a[i]=='0')
   	dp[i]=dp[i-1] + (a[i] - '0');
   	else{
   		diff=i-dp[i-1];
   		count =count + diff;
   		dp[i]= i + (a[i]-'0');
   	}
   }
   cout<<"Case #"<<r-t<<": "<<count<<endl;
   }
}

