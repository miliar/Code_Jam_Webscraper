#include <iostream>
#include <fstream>
#include <string>
#include <vector>

typedef long long int bignum;

using namespace std;

bool done(vector<bool> v){
	for (auto& it : v){
		if (it == false){
			return false;
		}
	}
	return true;
}

int main(){
	ifstream fin("A-large.in");
	ofstream fout("A-output.txt");

	int T;
	fin >> T;

	for (int t = 1; t <= T; t++){
		int n;
		fin >> n;

		std::string ans;
		if (n == 0){
			ans = "INSOMNIA";
		}
		else{
			vector<bool> digits(10, false);
			bignum c = n;
			bignum f;
			do{
				bignum v = c;
				while (v > 0){
					digits[v % 10] = true;
					v /= 10;
				}
				f = c;
				c += n;
			} while (!done(digits));
			ans = to_string(f);
		}
		fout << "Case #" << to_string(t) << ": " << ans << std::endl;
	}


	fout.close();
	return 0;
}