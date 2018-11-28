#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <sstream>
using namespace std;

int deceitful(vector<int> naomis, vector<int> kens) {
    int n = naomis.size();
    int ans = 0;
    for (int j = 0; j < kens.size(); ++j) {
        int i;
        for (i = 0; i < naomis.size(); ++i) {
            if (naomis[i] > kens[j]) break;
        }
        if (i == naomis.size()) break;

        ++ans;
        naomis.erase(naomis.begin() + i);
    }

    return ans;
}

int war(vector<int> naomis, vector<int> kens) {
    int ans = 0;
    for (int i = 0; i < naomis.size(); ++i) {
        int j;
        for (j = 0; j < kens.size(); ++j) {
            if (kens[j] > naomis[i]) break;
        }
        if (j == kens.size()) {
            ++ans;
            kens.erase(kens.begin());
        } else {
            kens.erase(kens.begin() + j);
        }
    }
    return ans;
}

string calc()
{
    int n;
    cin >> n;
    vector<int> naomis, kens;
    double f;
    for (int i = 0; i < n; ++i) {
        cin >> f;
        naomis.push_back((f*10000000 + 1)/100);
    }
    for (int i = 0; i < n; ++i) {
        cin >> f;
        kens.push_back((f*10000000 + 1)/100);
    }

    sort(naomis.begin(), naomis.end());
    sort(kens.begin(), kens.end());
    /*
    for (int i = 0; i < n; ++i) {
        cerr << naomis[i] << ' ';
    }
    cerr << endl;
    for (int i = 0; i < n; ++i) {
        cerr << kens[i] << ' ';
    }
    cerr << endl;
    */

    stringstream ss;
    ss << deceitful(naomis, kens) << ' ' << war(naomis, kens);
    return ss.str();
}

int main(void)
{
	int T;
	cin >> T;
	//getline(cin, line);
	for (int ca=1; ca<=T; ++ca) {
		//getline(cin, line);
		cout << "Case #" << ca << ": " << calc() << endl;
	}
	return 0;
}
