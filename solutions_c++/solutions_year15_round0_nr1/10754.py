#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

int t,n;
string s;

int main() {
	cin>>t;
	for(int j = 1; j <= t; ++j){
		cin>>n>>s;	
		
		int total = 0, ans = 0;
		
		for(int i = 0; i <= n; ++ i){
			int cur = (int)s[i] - 48;
			
			if(total < i){
				total ++;
				ans ++;
			}
				
			total += cur;
		}
		
		cout<<"Case #"<<j<<": "<<ans<<"\n";
	}
	
	return 0;
}
