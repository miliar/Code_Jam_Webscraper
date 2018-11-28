// All the includes.
#include <deque>
#include <iostream>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>

// Commons.
using namespace std;
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
#define LEN(x) (int)(x.size())
#define SIZE(x) (int)(x.size())

// Loops.
#define F0(i, n) for(int i=0; i < n; ++i)
#define F1(i, n) for(int i=1; i <= n; ++i)

// String funtions.
typedef stringstream SST;
void search_replace(string& original, string search_for, string replace_string) {
	size_t pos = 0;
	while ((pos = original.find(search_for, pos)) != string::npos) {
		original.replace(pos, search_for.length(), replace_string);
		pos += replace_string.length();			
	}
}

void split(const std::string &s, char delim, std::vector<std::string> &elems) {	std::stringstream ss(s); std::string item; while (std::getline(ss, item, delim)) { elems.push_back(item); } }
std::vector<std::string> split(const std::string &s, char delim) {
  std::vector<std::string> elems;
  split(s, delim, elems);
  return elems;
}

// Unoredered_map functions.
#define hash unordered_map
template <typename K, typename V>
bool mfind(std::unordered_map<K, V>& map, typename std::unordered_map<K, V>::key_type value) {
	if (map.find(value) == map.end()) {
	  return false;
	}
	return true;
}

// Pair typedefs.
typedef pair<long, long> PII;
typedef pair<double, double> PDD;
typedef pair<string, string> PSS;

// Vector Functions.
typedef vector<long> VI;
typedef vector<double> VD;
typedef vector<pair<long, long>> VPII;
typedef vector<pair<double, double>> VPDD;
typedef vector<long long> VL;
typedef vector<string> VS;
#define sortv(v) sort(v.begin(), v.end())
#define rsortiv(v) sort(v.begin(), v.end(), std::greater<long>())
#define rsortdv(v) sort(v.begin(), v.end(), std::greater<double>())
#define rsortlv(v) sort(v.begin(), v.end(), std::greater<long long>())

// Set functions.
typedef set<string> SS;
typedef set<long> SI;
typedef set<long long> SL;
typedef set<double> SD;
template <typename T>
bool sfind(std::set<T>& s, typename set<T>::value_type value) {
	if (s.find(value) == s.end()) {
		return false;
	} 
	return true;
}

// Regular expression.
bool is_match(string pattern, string word) {
	regex rx(pattern);
	return regex_match(word, rx);
}

// Main Logic
string nos[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int sum(int arr[26]) {
	int sum = 0;
	F0(i, 26) {
		sum += arr[i];
	}
	return sum;
}

bool helper(vector<string>& strings, vector<int>& indices, int j, string org, int case_no) {
	if (j >= 10) {
		return false;
	}
	
	string new_str;
	for (auto str : strings) {
		new_str.append(str);
  }
	//cout << new_str << endl;

	sortv(new_str);
	sortv(org);
	if (new_str.compare(org) == 0) {
	 	cout << "Case #" << case_no << ": ";
		for (auto x: indices) {
			cout << x;
		}
		cout << endl;
		return true;
	} else if (new_str.size() > org.size()) {
		return false;
  }
	
	for(int k=j; k < 10; ++k) {
		strings.push_back(nos[k]);
		indices.push_back(k);
		if (helper(strings, indices, k, org, case_no)) {
		  return true;
		}
		strings.pop_back();
		indices.pop_back();
	}
	return false;
}

int main() {
	int n;
	cin >> n;
	F1(i, n) {
		string c_ph;
		cin >> c_ph;
		
		int arr[26];
		F0(j, 26) {
			arr[j] = 0;
		}	
		for(auto c : c_ph) {
			arr[c-65] += 1;
		}
	
		vector<string> strings;
		vector<int> indices;
		helper(strings, indices, 0, c_ph, i);
	}
}
