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
	
	int i = 1, turn = 0;
	string tray;
	cin >> tray;
	while (tray[i] != '\0') {
		if (tray[i - 1] != tray[i]) {
			turn++;
		}
		i++;
	}
	if (tray[i - 1] == '-') {
		turn++;
	}
	cout << turn;
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
