#include <string>
#include <sstream>
#include <algorithm>
#include <functional>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <cmath>
using namespace std;

int main() {
    string s;
    ios::sync_with_stdio(false);
    
    cin >> s;
    int n = atoi(s.c_str());
    for (int i = 0; i < n; i++) {
        cin >> s;
	cin.ignore();
	int len = atoi(s.c_str());
        getline(cin, s);
	
	istringstream ss(s);
	string stmp;
	vector<int> v;
	v.reserve(len);
	while (getline(ss, stmp, ' ')) {
            v.push_back(atoi(stmp.c_str()));
	}

	int nsp = 0;
	if ((v.size() == 1) && (v[0] > 1)) {
	    if (v[0] == 9) {
		    v.push_back((v[0] + 2) / 3);
		    v.push_back((v[0] + 1) / 3);
		    v.push_back(v[0] / 3);
		    v.erase(v.begin());
		    nsp += 2;
	    }
	    else {
		int tmp = v[0];
		v.clear();
		v.push_back((tmp + 1) / 2);
		v.push_back(tmp / 2);
		nsp++;
	    }
	}
	
	do {
	    sort(v.begin(), v.end(), greater<int>());
	    int j;
	    for (j = 1; j < v.size(); j++) {   
		if (v[0] >= v[j] + j) {
		    break;
		}
	    }
	    if ((v[0] + 1) / 2 <= j) {
		break;
	    }
	    if (v[0] == 9 && ((v[1] <= 3) || (v[1] == 6 && (v.size() == 2) || v[2] <= 3))) {
		    v.push_back((v[0] + 2) / 3);
		    v.push_back((v[0] + 1) / 3);
		    v.push_back(v[0] / 3);
		    v.erase(v.begin());
		    nsp += 2;
	    }
	    else {
		for (int k = 0 ; k < j; k++) {
		    v.push_back((v[0] + 1) / 2);
		    v.push_back(v[0] / 2);
		    v.erase(v.begin());
		    nsp++;
		}
	    }
	} while (1);
      
	sort(v.begin(), v.end(), greater<int>());
        cout << "Case #" << i+1 << ": " << nsp + v[0] << endl;
    }
    return 0;
}