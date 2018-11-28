#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <sstream>
#include <cstdio>
using namespace std;

string calc()
{
    double C, F, X;
    cin >> C >> F >> X;
    
    double A = 0;
    double ans = X/2;
    for (int i = 1; i <= 1000000; ++i) {
        A += C / ((i-1)*F + 2);
        double t = A + X / (i*F+2);
        if (t < ans) {
            ans = t;
        }
    }
    char buf[1024];
    sprintf(buf, "%.8f", ans);
    return buf;
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
