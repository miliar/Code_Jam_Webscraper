
#include <string.h>
#include <string>
#include <stdio.h>
#include <iostream>
#include <unordered_set>
#include <stdint.h>
#include <stdlib.h>

using namespace std;

int main() {

    int T, total, counter[10];
    long N;
    cin >> T;
    cerr << T << " tests" << endl;
    for (int i = 0; i < T; i++) {

	cin >> N;
	memset(counter, 0, sizeof(counter));
	total = 0;
	
	char line[10];
	memset(line, 0, sizeof(line));
	long int ptr = 0;
	while (ptr < 1000000 && N != 0) {
	    ptr++;
	    if (ptr < 0)
		break;
	    sprintf(line, "%ld", ptr*N);
	    for (unsigned int j = 0; j < strlen(line); j++) {
		int digit = line[j] - '0';
		if (counter[digit] == 0) {
		    total++;
		    counter[digit]++;
		}
	    }
	    if (total >= 10) break;
	    cerr << "ptr: " << ptr << " N*ptr: " << ptr*N << " line: " << line << " total: " << total << endl;
	}
	
	if (ptr > 0 && ptr < 1000000 && N != 0) cout << "Case #" << 1+i << ": " << N*ptr << endl;
	else cout << "Case #" << 1+i << ": " << "INSOMNIA" << endl;
    
    }

    return 0;
}


