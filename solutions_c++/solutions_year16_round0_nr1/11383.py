#include <bits/stdc++.h>
using namespace std;

#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define int long long

main() {
	freopen("A-small-attempt3.in","r",stdin);
    freopen("output.out","w",stdout);
	int t; cin>>t;
	int count = 1;
	while(t--) {
		cout<<"Case #"<<count<<": ";
		count++;
		vector<int> freq(10, 0);
		int n; cin>>n;
		//cout<<"n: "<<n<<"; ";
		if(n == 0) {
			cout<<"INSOMNIA";
		}
		else {
		    int ans, curr, end = 0, flag, mul = 1;
    		while(!end) {
    			curr = (mul * n);
    			ans = curr;
    			mul++;
    			if(curr < 10) {
    				freq[curr] = 1;
    			}
    			else {
    				while(curr) {
    					int dig = curr % 10;
    					//cout<<dig<<" ";
    					freq[dig] = 1;
    					curr /= 10;
    				}
    				//cout<<endl;
    			}
    			flag = 1;
    			for(int i = 0; i < 10; i++) {
    				if(freq[i] == 0) {
    					flag = 0;
    				}
    			}
    			if(flag) {
    				end = 1;
    			}
    		}
    		cout<<ans;   
		}
		if(t) {
			cout<<endl;
		}
	}
}
