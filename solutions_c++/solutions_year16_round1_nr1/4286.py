#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <string>
#include <iostream>

//#define DBG_PRINT

#ifdef DBG_PRINT
#define DbgPrintf(...) printf(__VA_ARGS__)
#else
#define DbgPrintf(...)
#endif

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
#define INPUT_MAX_LENGTH 1000

using namespace std;


string S;
string LW;

int main(int argc, char *argv[]) {
	
	int T;
	int N;
	int i;
	unsigned j;
	//iterator it;

	//DbgPrintf("MAX: %lld \n", LLONG_MAX);

	scanf("%d", &T);
	DbgPrintf("T: %d \n", T);

	for( i = 1 ; i <= T ; i++ ) {
		S.clear();
		LW.clear();
		cin >> S;

		LW.push_back(S.at(0));

		for( j = 1 ; j < S.length() ; j++ ) {
			if( S.at(j) >= LW.at(0) ) {
				LW.insert(LW.begin(), S.at(j));
			}
			else {
				LW.push_back(S.at(j));
			}
		}
		
		cout << "Case #" << i << ": " << LW << "\n";
	}

	return 0;
}
