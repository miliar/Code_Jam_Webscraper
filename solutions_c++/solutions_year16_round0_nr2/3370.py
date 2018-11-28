#include<bits/stdc++.h>
#define mod 1000000007
#include<bits/stdc++.h>
#define mod 1000000007
#define pp pair<ll,ll>
#define mp make_pair
#define ll long long
#define ff first
#define ss second
#define big 100000000000000000
using namespace std;

ll n,tc,i,j,k,t;
char ar[110];
string str;

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ios::sync_with_stdio(0);
	
	cin>>tc;
	for(t=1;t<=tc;t++){
		cin>>str;
		n = str.length();
		ar[0] = str[0];
		k = 1;
		for(i=1;i<n;i++){
			if(str[i] != str[i-1])
				ar[k++] = str[i];
		}
		ll ans = 0;
		bool flag = 1;
		for(i=k-1;i>=0;i--){
			if(flag){
				if(ar[i] == '-'){
					ans++;
					flag = !flag;
				}
			}
			else{
				if(ar[i] == '+'){
					ans++;
					flag = !flag;
				}
			}
		}
		cout<<"Case #"<<t<<": "<<ans<<"\n";
	}
	
	return 0;
}

