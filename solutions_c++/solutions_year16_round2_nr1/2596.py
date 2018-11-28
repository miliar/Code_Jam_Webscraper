#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
int main(){
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int t;
	in >> t;
	for (int i = 1; i <= t; ++i){
		string s, ans;
		in >> s;
		vector<string> z{ "ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE" };
		map<char, int> x;
		map<int, int> y;
		for (auto i : s)
			++x[i];
		for (auto i : x){
			if (i.first == 'U'){
				for (auto j : z[4]){
					for (auto k : x){
						if (j == k.first)
							x[k.first] -= i.second;
					}
				}
				y[4] += i.second;
			}
			if (i.first == 'G'){
				for (auto j : z[8]){
					for (auto k : x){
						if (j == k.first)
							x[k.first] -= i.second;
					}
				}
				y[8] += i.second;
			}
			if (i.first == 'Z'){
				for (auto j : z[0]){
					for (auto k : x){
						if (j == k.first)
							x[k.first] -= i.second;
					}
				}
				y[0] += i.second;
			}
			if (i.first == 'W'){
				for (auto j : z[2]){
					for (auto k : x){
						if (j == k.first)
							x[k.first] -= i.second;
					}
				}
				y[2] += i.second;
			}
			if (i.first == 'X'){
				for (auto j : z[6]){
					for (auto k : x){
						if (j == k.first)
							x[k.first] -= i.second;
					}
				}
				y[6] += i.second;
			}
		}
		for (auto i : x){
			if (i.first == 'H'){
				for (auto j : z[3]){
					for (auto k : x){
						if (j == k.first)
							x[k.first] -= i.second;
					}
				}
				y[3] += i.second;
			}
		}
		for (auto i : x){
			if (i.first == 'F'){
				for (auto j : z[5]){
					for (auto k : x){
						if (j == k.first)
							x[k.first] -= i.second;
					}
				}
				y[5] += i.second;
			}
		}
		for (auto i : x){
			if (i.first == 'V'){
				for (auto j : z[7]){
					for (auto k : x){
						if (j == k.first)
							x[k.first] -= i.second;
					}
				}
				y[7] += i.second;
			}
		}
		for (auto i : x){
			if (i.first == 'I'){
				for (auto j : z[9]){
					for (auto k : x){
						if (j == k.first)
							x[k.first] -= i.second;
					}
				}
				y[9] += i.second;
			}
		}
		for (auto i : x){
			if (i.first == 'O'){
				for (auto j : z[1]){
					for (auto k : x){
						if (j == k.first)
							x[k.first] -= i.second;
					}
				}
				y[1] += i.second;
			}
		}
		for (auto i : y){
			for (int j = 0; j != i.second; ++j){
				ans += to_string(i.first);
			}
		}
		out << "Case #"<<i<<": "<<ans << endl;
	}
}
