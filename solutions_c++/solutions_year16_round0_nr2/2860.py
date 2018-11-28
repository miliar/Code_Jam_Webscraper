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

// Loops.
#define fori(n) for(int i=1; i<=n; ++i)
#define forj(n) for(int j=0; j<n; ++j)
#define fork(n) for(int k=0; k<n; ++k)

// String funtions.
typedef stringstream SST;
void search_replace(string& original, string search_for, string replace_string) {
	size_t pos = 0;
	while ((pos = original.find(search_for, pos)) != string::npos) {
		original.replace(pos, search_for.length(), replace_string);
		pos += replace_string.length();			
	}
}

void split(const std::string &s, char delim, std::vector<std::string> &elems) {
	std::stringstream ss(s);
  std::string item;
  while (std::getline(ss, item, delim)) {
    elems.push_back(item);
  }
}

std::vector<std::string> split(const std::string &s, char delim) {
  std::vector<std::string> elems;
  split(s, delim, elems);
  return elems;
}

// Unoredered_map functions.
#define hash unordered_map
typedef std::unordered_map<int, long> iimap;
typedef std::unordered_map<string, long> simap;
typedef std::unordered_map<long, string> ismap;
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
typedef set<char> SC;
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
int main() {
	int t;
	cin >> t;
	fori(t) {
		string cakes;
		cin >> cakes;
		int ans = 0;
		char last = 'X';
		char c;
		for (c : cakes) {
			if (last == 'X') { last = c; continue; }
			if (c != last) {
				++ans;
				last = c;
			}
		}
		if (cakes[cakes.length() - 1] == '-') ++ans;	
		cout << "Case #" << i << ": " << ans << endl;
	}
}
