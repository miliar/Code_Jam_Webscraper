#include<iostream>
#include<string>
#include<vector>
using namespace std;
vector<string> strs;

int main(){
	int T, len, sum = 0, need = 0, t = 0;
	cin >> T;
	for(t = 0; t < T; ++t){
		string s;
		cin >> len; cin >> s;
		strs.push_back(s);
	}
	for(t = 0; t < T; ++t){
		sum = (strs[t][0] - '0');
		need = 0;
		for(int i = 1; i < strs[t].length(); ++i){
			if((strs[t][i] - '0') > 0){
				need += max(0, i - sum);
				sum = max(sum, i);
				sum += (strs[t][i]- '0');
			}
		}
		cout << "Case #" << t+1 << ": " << need << endl;
	}
}
