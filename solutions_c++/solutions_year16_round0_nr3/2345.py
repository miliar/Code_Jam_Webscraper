// All the includes.
#include <deque>
#include <iostream>
#include <regex>
#include <set>
#include <sstream>
#include <string>
#include <unordered_map>
#include <vector>
#include <math.h>

// Commons.
using namespace std;
#define pb push_back
#define pf push_front
#define popb pop_back
#define popf pop_front

// Loops.
#define fori(n) for(int i=0; i<n; ++i)
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

long convert_base(long no, int from, int to) {
	long ans10 = 0;
	int mod;
	int count = 0;
	if (from != 10) {
		while(no > 0) {
			mod = no % 10;
			no = no / 10;
			ans10 += mod * pow(from, count++);
		}
	} else {
	 	ans10 = no;
	}
	if (to == 10) { return ans10; }
	
	long ans = 0;
	count = 0;
	while (ans10 > 0) {
		mod = ans10 % to;
		ans10 = ans10 / to;
		ans += mod  * pow(10, count++);
	}
	return ans;
}

long getmin() {
	//return convert_base(100001, 2, 10);
	return convert_base(1000000000000001, 2, 10);
}
long getmax() {
	//return convert_base(111111, 2, 10);
	return convert_base(1111111111111111, 2, 10);
}

// Main Logic
long primish_fun(long no) {
	long sq = sqrt(no);
	if (no % 2 == 0) {return 2;}
	for(long i = 3; i <= sq; i+=2) {
		if (no % i == 0) {
			return i;
		}
	}
	return -1;
}

long interpret_base(long no, int base) {
	long ans = 0;
	int count = 0;
	int mod;
	while (no > 0) {
		mod = no % 10;
		no = no / 10;
		ans += mod * pow(base, count++);
	}
	return ans;
}

int main() {
	int t, n = 16, j = 50;
	long min = getmin();
	long max = getmax();
	//cout << min <<  " " << max << endl;
	int bases[] = {2, 3, 4, 5, 6, 7, 8, 9, 10};
	int j_count = 0;
	cout << "Case #1:" << endl;
	for(long no=min; no<=max; no+=2) {
		VL anss;
		bool gotone = true;
		
    long base_2_no = convert_base(no, 10, 2);
		//cout << "No checked " << no << endl;
		for	(int i=0; i < 9; ++i) {
			//cout << "base_2_no " << base_2_no << endl;
		  long number = interpret_base(base_2_no, bases[i]);
			//cout << "converted to base " << bases[i] << " being " << number << endl;
			long primish = primish_fun(number);
			//cout << "divisor is " << primish << endl;
			if (primish == -1) {
				//cout << "Said to primary in base " << bases[i] << " with no being " << convert_base(base_2_no, 10, bases[i])<< endl;
				gotone = false;
				break;
			}
			anss.push_back(primish);			
		}

		if (gotone) {
			cout << base_2_no << " "; 
			for(int div : anss) {
				cout << div << " ";
			}
			cout << endl;
			++j_count;
		} else {
			//++j_count;
		}
		if (j_count == j) {
			break;
		}
	}
}	
