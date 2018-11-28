#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

int main(int argc, char *args[]) {
	if (argc == 2 && strcmp(args[1], "small") == 0) {
		freopen("small.in", "r", stdin);
		freopen("small.out", "w", stdout);
	}
	else if (argc == 2 && strcmp(args[1], "large") == 0) {
		freopen("large.in", "r", stdin);
		freopen("large.out", "w", stdout);
	}
	else {
		cout << "\nPlease enter \"small\" or \"large\" test file.";
		return 0;
	}

	int N;
	cin >> N;
	for (int i=0; i<N; i++) {
		string S = "";
		cin >> S;
		string A = "";
		A.insert(0, 1, S[0]);
		for (int j=1; j<S.length(); j++) {
			if (S[j] >= A[0])
				A.insert(0, 1, S[j]);
			else
				A.insert(A.length(), 1, S[j]);
			
		}
		
		printf("Case #%d: %s\n", i+1, A.c_str());
	}

	fclose(stdin);
	fclose(stdout);
	return 0;	
}	
