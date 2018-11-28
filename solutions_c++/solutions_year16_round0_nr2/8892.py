#include <iostream>
#include <vector>

int main(){
	std::ios_base::sync_with_stdio(false);
	std::cin.tie(nullptr);
	std::cout.tie(nullptr);
	unsigned t;
	std::cin >> t;
	for(unsigned i = 0; i < t; ++i){
		std::string input{};
		std::cin >> input;
		std::vector<std::pair<unsigned, unsigned>> dp(input.length());
		if(input[0] == '+'){
			dp[0].first = 0;
			dp[0].second = 1;
		}
		else{
			dp[0].first = 1;
			dp[0].second = 0;
		}
		for(unsigned j = 1; j < input.length(); ++j){
			if(input[j] == '+'){
				dp[j].first = std::min(dp[j - 1].first, dp[j - 1].second + 1);
				dp[j].second = std::min(dp[j - 1].first + 1, dp[j - 1].second + 2);
			}
			else{
				dp[j].first = std::min(dp[j - 1].first + 2, dp[j - 1].second + 1);
                dp[j].second = std::min(dp[j - 1].first + 1, dp[j - 1].second);
			}
		}
		std::cout << "Case #" << i + 1 << ": " << dp[input.length() - 1].first << "\n";
	}

	return 0;
}
