#include <iostream>
#include <stdio.h>
#include <string>
#include <math.h>
#include <vector>
#include <stdlib.h>

using namespace std;

int compare (const void * a, const void * b)
{
	return ( *(int*)a - *(int*)b );
}

void * solve(){
	void * ans;
	string word;
	char top;
	cin >> word;
	
	int i;
	for (i = 1; word[i] != '\0'; i++) {
		if (word[i] >= word[0]) {
			top = word[i];
			word = word.substr(i, 1) + word.substr(0, i) + word.substr(i + 1, 1000);
		}
	}
	cout << word;
	
	return ans;
}



int main (int argc, char * const argv[]) {
    int ncases, cases;
	scanf("%d\n", &ncases);
	for (cases = 0; cases < ncases; cases++) {
		cout << "Case #" << cases + 1 << ": ";
		solve();
		cout << endl;
	}
    return 0;
}
