#include <cstdio>
#include <iostream>
#include <ctime>
#include <iomanip>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>

using namespace std;


int main() {
	int times;
	cin>>times;
	for(int ii = 1;ii<=times; ++ii) {
		printf("Case #%d: ", ii);
		string inStr, outStr;
		cin>>inStr;
		outStr = inStr[0];
		for(int i = 1; i<inStr.size(); ++i) {
			if(string(1, inStr[i]) + outStr > outStr + inStr[i]) {
				outStr = string(1, inStr[i]) + outStr;
			} else {
				outStr += inStr[i];
			}
		}
		cout<<outStr<<endl;
	}
	return 0;
}
