
#include <string.h>
#include <string>
#include <stdio.h>
#include <iostream>
#include <unordered_set>
#include <stdint.h>
#include <stdlib.h>

using namespace std;

int main() {

    int T, S;
    cin >> T;
    for (int i = 0; i < T; i++) {
	int ans = 0;
	char line[110];
	cin >> line;
	S = strlen(line);
	
	char prob[110];
	memset(prob, 0, sizeof(prob));
	int ptr = 0;
	for (int i = 0; i < S; i++) {
	    if (i == 0 || line[i-1] != line[i])
		prob[ptr++] = line[i];
	}
	if (strlen(prob) == 1) ans = (prob[0] == '-') ? 1 : 0;
	else if (prob[0] == prob[ptr - 1]) {
	    ans = (prob[0] == '-') ? ptr : ptr - 1;
	} else {
	    ans = (prob[0] == '-') ? ptr - 1 : ptr;
	}
	cout << "Case #" << 1+i << ": " << ans << endl;
    
    }

    return 0;
}


