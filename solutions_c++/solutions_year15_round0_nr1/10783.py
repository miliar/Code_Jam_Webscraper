#include <bits/stdc++.h>
#define pb push_back
#define mp make_pair

const double PI=2*asin(1);

using namespace std;

int main(){
	int n, t, caso=1;
	string s;
	
	cin >> t;
	while(t--){
		cin >> n >> s;
	
		for(int i=0; i<=n; i++) s[i]-='0';
	
		int cont=0, ans=0;
		for(int i=0; i<=n; i++){			
			if(cont<i){ 
				ans+= i-cont;
				cont= i;
			}
			cont+=s[i];
			//cout << ans << endl;
		} 
	
		cout << "Case #" << caso << ": " << ans << endl;
		caso++;
	}
}
