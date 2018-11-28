#include <cstdio>
#include <cstdlib>
#include <memory.h>
#include <algorithm>
#include <string>
#include <map>
#include <unordered_map>
#include <unordered_set>
#include <set>
#include <vector>
#include <cmath>
#include <climits>
#include <queue>
#include <cassert>
#include <iostream>
#include <sstream>
#include <utility>
#include <bitset>
using namespace std;
#define PI 3.14159265358979323846264338327950288
vector<string> Tokenize(string s, string ch) {
	vector<string> ret;
	for (int p = 0, p2; p < s.size(); p = p2 + 1) {
		p2 = s.find_first_of(ch, p);
		if (p2 == -1)
			p2 = s.size();
		if (p2 - p > 0)
			ret.push_back(s.substr(p, p2 - p));
	}
	return ret;
}
int my_abs(int a) {
	int i = a >> 31;
	return ((a ^ i) - i);
}

vector<int> TokenizeInt(string s, string ch) {
	vector<int> ret;
	vector<string> p = Tokenize(s, ch);
	for (int i = 0; i < p.size(); i++)
		ret.push_back(atoi(p[i].c_str()));
	return ret;
}

double process(float C, float F, float X) {
	double res = 0.1;
	int n = 0;
	vector<double> resV;
	double t;
	while (1) {
		t = 0.00000000000;
		for (int i = 0; i < n; i++) {
			if (n >= 1)
				t += C / (i * F + 2);
		}
		t += X / (n * F + 2);
		if ((!resV.empty()) && (t > *prev(end(resV)))) {
//			cout<<n<<endl;
			break;
//			return t;
		}
		resV.push_back(t);
		n++;
	}
	return *prev(end(resV));
}
int main() {
float a=1999.19990;
//cout<<"a"<<a<<endl;
	int Case = 1;
	int T;
	char tmp[10000];
	int p[100];
	double res;
	vector<string> names;
	scanf("%d", &T);
//	getchar();
	while (T--) {
		float C, F, X;
		scanf("%f%f%f", &C, &F, &X);
//		printf("%lf %lf %lf\n",C,F,X);
//		cout<<C<<" "<<F<<" "<<X<<" "<<endl;
		res = process(C, F, X);
		printf("Case #%d: %.7lf\n", Case++, res);
	}
	return 0;
}
