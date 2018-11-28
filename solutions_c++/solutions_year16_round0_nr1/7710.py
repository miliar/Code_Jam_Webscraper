#include <iostream>
#include <cstdio>
#include <algorithm>
#include <climits>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cmath>

using namespace std;

set<int> num_vis;

void add_digits(long long num) {
	long long n = num;
	while(n > 0) {
		int r = n%10;
		num_vis.insert(r);
		n = n/10;
	}
}

void print_case_op(int case_num, string op) {
	cout << "Case #" << case_num << ": " << op << endl;
}

int main()
{	int T, N;
	cin >> T;
	for(int t=1; t<=T; t++) {
		cin >> N;
		string op = "INSOMNIA";
		if(N==0) {
			cout << "Case #" << t << ": " << op << endl;
		}
		else {
			long long num = N;
			for(long long int iter=2; iter<=1000000; iter++) {
				add_digits(num);
				if(num_vis.size()==10) {
					break;
				}
				num = iter*N;
			}
			if(num_vis.size()==10) {
				cout << "Case #" << t << ": " << num << endl;
			}
			else {
				cout << "Case #" << t << ": " << op << endl;
			}
		}
		num_vis.clear();
	}
	return 0;
}