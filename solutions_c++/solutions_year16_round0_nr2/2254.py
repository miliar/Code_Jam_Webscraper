#include <iostream>
#include <algorithm>
#include <set>
#include <string>
using namespace std;

void use_file(const std::string& s = "")
{
    if (s != "std" && s != ""){
        freopen((s+".in").c_str(), "r", stdin);
        freopen((s+".out").c_str(), "w", stdout);
    }
}

int solve(const std::string& str)
{
	char cur = str[0];
	int ans = 0;
	for (int i = 0; i < str.size(); i++){
		if (cur != str[i]){
			cur = str[i];
			ans++;
		}
	}
	if (cur == '-') ans++;
	return ans;
}

int main(){
	int N;
	use_file("B2");
	cin >> N;
	for (int ca = 1; ca <= N; ca++){
		string s;
		cin >> s;
		cout << "Case #" << ca << ": " << solve(s) << endl;
	}
	return 0;
}
