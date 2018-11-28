#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main() {

  int T; 
  cin >> T;
  for (int Ti = 1; Ti <= T; ++Ti) {
	int N;
	cin >> N;

	vector<string> A(N);
	vector<int> B(N);
	for (int i=0; i<N; ++i) {
		cin >> A[i];
		B[i] = 0;
	}

	char ch;

	vector <char> str;
	vector <int> count;
	str.push_back(A[0][0]);
	int j=0;
	int xx=0;
	for( int i=0; i<A[0].length(); ++i) {
		if (A[0][i] != str[j]) {
			count.push_back(xx);
			xx=0;
			str.push_back(A[0][i]);
			++j;
		} else ++xx;
	}
	count.push_back(xx); //cout << count[0] << endl;
bool fail = false;
vector <int> mincount(count);
// vector <int> maxcount(str.size());


	for (int y=1; y<N; ++y) { 

	vector <char> str2;
	vector <int> count2;
	str2.push_back(A[y][0]);
	int j=0;
	int xx=0;
	 for( int i=0; i<A[y].length(); ++i) {
		if (A[y][i] != str2[j]) {
			count2.push_back(xx);
			xx=0;
			str2.push_back(A[y][i]);
			++j;
		} else ++xx;
	}
	count2.push_back(xx);
	for (int u =0 ; u<str.size(); ++u) {
	mincount[u] = min(mincount[u], count2[u]);
	count[u]+=count2[u];
	}
//cout << str[0] << ' ' << str2[0] << endl;
	if (str != str2) { cout << "Case #" << Ti << ": "<<"Fegla Won" << endl;
		fail = true;	
	}

	}

if (!fail) {
	int sum = 0;
	for (int y=0; y<N; ++y) { 

	vector <char> str2;
	vector <int> count2;
	str2.push_back(A[y][0]);
	int j=0;
	int xx=0;
	 for( int i=0; i<A[y].length(); ++i) {
		if (A[y][i] != str2[j]) {
			count2.push_back(xx);
			xx=0;
			str2.push_back(A[y][i]);
			++j;
		} else ++xx;
	}
	count2.push_back(xx);
	for (int u =0 ; u<str.size(); ++u) {
		//cout << count[u] << ' '<< count[u]/N << ' ' << count2[u] << '-';
		sum += abs(count[u]/N-count2[u]);
//	mincount[u] = min(mincount[u], count2[u]);
//	count[u]+=count2[u];
	}
//cout << str[0] << ' ' << str2[0] << endl;
//	if (str != str2) { cout << "Case #" << Ti << ": "<<"Fegla Won" << endl;
//		fail = true;	
//	}

	}



//	int sum = 0;
//	for (int u=0; u < str.size(); ++u) {
//		sum += count[u] - mincount[u]*N; 
//	}
	    cout << "Case #" << Ti << ": "<< sum << endl;
	  }

  }

  return 0;

}
