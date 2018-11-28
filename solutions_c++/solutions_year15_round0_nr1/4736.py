#include<bits/stdc++.h>
using namespace std;
#define mod 1000000007
typedef long long ll;

char a[1008];
int s[1008];

int main(){
	ll t,n,i,z;
	cin>>t;
	for(z=1;z<=t;z++){
		cin>>n;
		n++;
		cin>>a;
		
		int ans=0;
		s[0]=a[0]-'0';
		
		for(i=1;i<n;i++){
			if(i>s[i-1]){
				ans++;
				s[i]=s[i-1]+a[i]-'0'+1;
			}
			else
				s[i]=s[i-1]+a[i]-'0';
		}
		cout<<"Case #"<<z<<": "<<ans<<endl;
	}
	return 0;
}
