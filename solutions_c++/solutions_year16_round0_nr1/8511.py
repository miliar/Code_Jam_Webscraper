#include <bits/stdc++.h>

typedef long long int ll;
typedef unsigned long long int ull;
#define rep(i,n) for(int i=0;i<(n);i++)
 
using namespace std;

int main(){
	stringstream ss;
	ll times;
	cin >> times;

	rep(i, times){
		ll n, k;
		cin >> n;
		if(n == 0){
			cout << "Case #" << (i+1) << ": INSOMNIA" << endl;
			continue;
		}
		vector<bool> memo(10, false);

		k = n;
		while(true){
			string s;
			ss.clear();
			ss.str("");
			ss << k;
			s = ss.str();

			rep(i, s.length())	memo[s[i]-'0'] = true;


			int f = 0;
			for(;f < 10; f++){
				if(memo[f] == false)	break;
			}
			if(f == 10)	break;
			k += n;
		}
		cout << "Case #" << (i+1) << ": " << k << endl;

	}

	return 0;
}