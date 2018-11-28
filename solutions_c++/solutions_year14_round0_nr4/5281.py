#include <iostream>
#include <algorithm>

const int MAX_N = 1005;
double naomi[MAX_N];
double ken[MAX_N];

using std::sort;
using std::cin;
using std::cout;
using std::endl;

int main() {
    int T;
    cin >> T;
    for (int testcase = 1; testcase <= T; ++testcase) {
    	cout << "Case #" << testcase << ": ";
    	int N;
    	cin >> N;
    	for (int i = 0; i < N; ++i)
    		cin >> naomi[i];
    	for (int i = 0; i < N; ++i)
    		cin >> ken[i];
    	sort(naomi, naomi + N, std::greater<double>());
    	sort(ken, ken + N, std::greater<double>());
    	/*
    	for (int i = 0; i < N; ++i)
    		cout << naomi[i] << " ";
    	cout << endl;
    	for (int i = 0; i < N; ++i)
    		cout << ken[i] << " ";
    	cout << endl;
    	*/
    	int deceitful_ans = 0;
    	int pk = 0;
    	for (int i = 0; i < N; ++i) {
    		while ((ken[pk] > naomi[i]) && (pk < N)) {
    			++pk;
    		}
    		if (pk < N) {
    			++deceitful_ans;
    			++pk;
    		}
    	}
    	cout << deceitful_ans << " ";
    	int war_ans = N;
    	int pn = 0;
    	for (int i = 0; i < N; ++i) {
    		while ((naomi[pn] > ken[i]) && (pn < N)) {
    			++pn;
    		}
    		if (pn < N) {
    			--war_ans;
    			++pn;
    		}
    	}
    	cout << war_ans << endl;
    }	
    return 0;
}
