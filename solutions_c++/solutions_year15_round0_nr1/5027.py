#include <bits/stdc++.h>
using namespace std;
int t,n,sum,ans,c=1;
string s;
int main(){
	 freopen("input.in","r",stdin);
	 freopen("output.txt","w",stdout);
    cin>>t;
    while(t--){ans=0;sum=0;
        cin>>n;
        cin>>s;
       for(int i=0;i<s.size();i++){
       	if(sum<i){
       	  	ans+=i-sum;
       	  	sum+=i-sum;
       	  }
       	  sum+=s[i]-'0';
       }
       cout<<"Case #"<<c<<": "<<ans<<'\n';
       c++;
    }

	return 0;
}
