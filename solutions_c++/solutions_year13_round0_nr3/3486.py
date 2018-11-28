#include <iostream>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

int A, B;
vector<int> palindrome_list;
vector<long long> fnsq_list;
int prev_start = 0;
int prev_end = 0;

void gen_palindrome_r(int length) {
	if (length == 1) {
		for (int i = 1; i <= 9; i++)
			palindrome_list.push_back(i);
		return;
	}

	prev_end = palindrome_list.size();

	//if (length%2 == 0) {
		for (int p = prev_start; p < prev_end; ++p) {
			int n;
			stringstream ss;
			ss << palindrome_list[p];
			string str = ss.str();
			str += '0';
			int len = str.size();
			for (int c = 0; c < len/2; c++) {
				str[len-c-1] = str[c];
			}
			if (length%2 == 0) {
				stringstream ss2(str); ss2 >> n;
				palindrome_list.push_back(n);
			} else {
				for (int i = 0; i <= 9; i++) {
					str[len/2] = '0'+i;
					stringstream ss2(str); ss2 >> n;
					palindrome_list.push_back(n);
				}
			}
		}
	//}

	prev_start = prev_end;
}

void gen_palindrome() {
	for (int l = 1; l <= 7; l++) {
		gen_palindrome_r(l);
	}
}

void gen_fair_and_square() {
	for (int i = 0; i < palindrome_list.size(); ++i) {
		long long sq = 
			(long long)palindrome_list[i] *
			(long long)palindrome_list[i];

		stringstream ss;
		ss << sq;
		string str = ss.str();
		int len = str.size();
		bool palindrome = true;
		for (int c = 0; c < len/2; c++) {
			if (str[c]!=str[len-c-1]) {
				palindrome = false;
				break;
			}
		}

		if (palindrome) { 
			fnsq_list.push_back(sq);
			//cout << sq << "\n";
		}
	}
}

long long count_fair_n_square() {
	long long count_var = 0;
	for (int i = 0; i < fnsq_list.size(); ++i) {
		if (fnsq_list[i] > B) break;
		if (fnsq_list[i] >= A) count_var+=1;
	}
	return count_var;
}


int main(int argc, char const *argv[])
{
	int t, T;

	gen_palindrome();
	gen_fair_and_square();

	cin >> T;

	for (t = 1; t <= T; ++t) {
		cin >> A >> B;
		cout << "Case #" << t << ": " << count_fair_n_square() << "\n";
	}
	
	return 0;
}
