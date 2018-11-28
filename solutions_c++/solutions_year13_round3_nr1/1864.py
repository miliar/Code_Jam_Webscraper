#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <set>
#include <map>
#include <list>
#include <cmath>
#include <vector>
#include <algorithm>
#include <iterator>
using namespace std;

long long isNCons(string s, long long index, long long N)
{
    long long cons = 0;
    for (int i = index; i < s.size(); ++i) {
	if (s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u') {
	    cons = 0;
	    continue;
	}
	++cons;
	if (cons == N)
	    return i;
    }

    return -1;

}

int main() 
{
    fstream f("in", fstream::in);
    int T;
    f >> T;
    for (int caseNo = 1; caseNo <= T; ++caseNo) {
	string name;
	long long N;
	f >> name >> N;
	long long num = 0;
	for (long long i = 0; i < name.size(); ++i) {
	    for (long long j = i; j < name.size(); ++j) {
		long long k = isNCons(name, j, N);
		if (k != -1) {
		    num += (name.size() - k);
		    break;
		}
	    }
	}
	cout << setprecision(6) << "Case #" << caseNo << ": " << num << endl;
    }
    return 0;
}
