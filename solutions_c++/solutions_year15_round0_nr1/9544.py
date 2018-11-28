
#include <iostream>
#include <string.h>

using namespace std;

int main() {

    int t = 0;
    char str[1002];
    int n[1001], sum, up, hire, len;
    int smax;
    
    cin >> t;
    
    for (int i=0; i<t; i++) {
	smax = 0;
	cin >> smax;
	memset(str, 0, sizeof(str));
	cin >> str;
	len = strlen(str);
	for (int j=0; j<len; j++) {
	    n[j] = str[j] - '0';
	    sum += n[j];
	}
	hire = 0;
	up = n[0];
	for (int j=1; j<len; j++) {
		if (n[j] == 0) continue;
		if (up < j) {
		    hire += (j - up);
		    up += (j - up);
		}
		up += n[j];
		if (up >= smax) break;
	}
	
	cout << "Case #" << 1+i << ": " << hire << endl;
    }

    return 0;
}
