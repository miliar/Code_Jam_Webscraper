#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

unordered_map<string, string> ConstructMap() {
	unordered_map<string, string> lookup;
	lookup.insert(pair<string, string>("ii", "-1"));
	lookup.insert(pair<string, string>("ij", "k"));
	lookup.insert(pair<string, string>("ik", "-j"));
	lookup.insert(pair<string, string>("ji", "-k"));
	lookup.insert(pair<string, string>("jj", "-1"));
	lookup.insert(pair<string, string>("jk", "i"));
	lookup.insert(pair<string, string>("ki", "j"));
	lookup.insert(pair<string, string>("kj", "-i"));
	lookup.insert(pair<string, string>("kk", "-1"));

	return lookup;
}

string multi(string first, char second, unordered_map<string, string> &lookup) {
	bool negtive = false;
	char first_char;
	string result = "";

	if (first[0] == '-') {
		negtive = true;
		first_char = first[1];
	} else {
		first_char = first[0];
	}

	if (first_char == '1') {
		
		if (negtive) {
			result.push_back('-');
		}
		result.push_back(second);
		return result;
	}
	if (second == '1') {
		return first;
	}

	string combine = "";
	combine.push_back(first_char);
	combine.push_back(second);
	result = lookup[combine];

	if (negtive) {
		if (result[0] == '-') {
			result.erase(0, 1);
		} else {
			result = "-" + result;
		}
	}
	return result;

}

bool IsIJK(int L, long long X, string elem, unordered_map<string, string> &lookup) {
	if (X * L < 3) {
		return false;
	}
	if (L == 1) {
		return false;
	}

	string result = "1";
	bool pos_i = false;
	bool pos_k = false;
	bool match = false;
	string elem_result = "";
	for (long long i = 0; i < X; ++i) {
		for (int j = 0; j < L; ++j) {
			result = multi(result, elem[j], lookup);
			if (result == "i") {
				pos_i = true;
			} else if (result == "k" && pos_i) {
				pos_k = true;
			}
		}
		if (i == 0) {
			elem_result = result;
		}
		
		if (elem_result == "-1" && (X % 2 != 0)) {
			match = true;
		} else if (elem_result != "1" && (X % 2 == 0) && (X % 4 != 0)) {
			match = true;
		}
		if (!match) {
			break;
		}

		if (pos_i && pos_k) {
			break;
		}
	}


	if (pos_i && pos_k && match) {
		return true;
	} else {
		return false;
	}
}


int main(int argc, char const *argv[])
{
	unordered_map<string, string> lookup = ConstructMap();
	int T;
	cin >> T;
	for (int i = 0; i < T; ++i) {
		int L;
		cin >> L;
		long long X;
		cin >> X;
		string elem;
		cin >> elem;


		cout << "Case #" << i + 1 << ": ";
		if (IsIJK(L, X, elem, lookup)) {
			cout << "YES" << endl;			
		} else {
			cout << "NO" << endl;
		}

		
	}
	return 0;
}