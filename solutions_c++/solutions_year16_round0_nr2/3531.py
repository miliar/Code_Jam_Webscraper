#include <bits/stdc++.h>
using namespace std;
typedef long long LL;



LL solve(string input){
	vector<LL> dp(input.size());	
	if (input[0] == '-')
		dp[0] = 1;
	else
		dp[0] = 0;
	

	for (int i = 1; i != input.size(); ++i){ 
		if(input[i] == '+')
			dp[i] = dp[i-1];
		else if(input[i-1] == '+')
			dp[i] = dp[i-1] + 2;
		else 
			dp[i] = dp[i-1];

	}
	return dp[input.size()-1];
	
}





int main() {
	int n; cin >> n;
	vector<LL> res(n);
	transform(res.begin(), res.end(), res.begin(), [](LL x) {
			string tmp;
			std::cin >> tmp;
			return solve(tmp);
		});
	int i = 1;
	for_each(res.begin(), res.end(), [&](int val) { std::cout << "Case #" << i++ << ": " << val << std::endl;});


}


