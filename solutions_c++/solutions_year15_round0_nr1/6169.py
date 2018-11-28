#include <bits/stdc++.h>
#define LL long long int
using namespace std;
int main(){
	ios_base::sync_with_stdio(false); 	
	cin.tie(NULL);
	LL i,j,m,n,t,x,ans,temp;
	string s;
	cin >> t;
	for(x=1;x<=t;x++){
		cin >> n;
		cin >> s;
		temp = 0;ans =0;
		for(i=0;i<n+1;i++){
			if(s[i]=='0')continue;
			if(temp>=i)
				temp+=s[i]-'0';
			else{
				ans+=(i-temp);
				temp += (i-temp)+s[i]-'0';
			}
		}
		cout << "Case #" << x << ": " << ans << endl;
	}
	return 0;
}


