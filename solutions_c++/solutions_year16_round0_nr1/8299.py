#include<bits/stdc++.h>
using namespace std;
#define ll long long
int main(){
	#ifndef ONLINE_JUDGE
    	freopen("inp.txt","r",stdin);
    	freopen("out.txt","w",stdout);
    #endif
	int t,s;
	cin>>t;
	s=t;
	while(t--){
		int n;
		int c[10]={0},cnt=0;
		cin>>n;
		ll ans;
		if(n==0)
		cout<<"Case #"<<s-t<<": INSOMNIA"<<endl;
		else{
			for(int i=1;;i++){
				ans=n*i;
				
				stringstream s1;
        		s1 << ans;
        		string str = s1.str();
        		
        		int l=str.length();
        		for(int j=0;j<l;j++){
        			c[str[j]-48]++;
				}
				for(int j=0;j<10;j++){
					if(c[j]!=0)
					cnt++;
				}
				if(cnt==10)
				break;
				cnt=0;
			}
			cout<<"Case #"<<s-t<<": "<<ans<<endl;
		}
	}
	
	return 0;
}

