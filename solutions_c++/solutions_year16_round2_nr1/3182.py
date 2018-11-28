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
	string mess;
	int l, lett[12] = {0,0,0,0,0,0,0,0,0,0,0}, i, j;
	cin >> mess;
	l = mess.length();
	for (i = 0; i < l; i++) {
		if (mess[i] == 'Z') {
			lett[0]++;
			lett[1]--;
		}
		if (mess[i] == 'O') {
			lett[1]++;
		}
		if (mess[i] == 'W') {
			lett[2]++;
			lett[1]--;
		}
		if (mess[i] == 'H') {
			lett[3]++;
		}
		if (mess[i] == 'U') {
			lett[4]++;
			lett[5]--;
			lett[1]--;
			lett[9]++;
		}
		if (mess[i] == 'F') {
			lett[5]++;
			lett[9]--;
		}
		if (mess[i] == 'X') {
			lett[6]++;
			lett[9]--;
			lett[7]--;
		}
		if (mess[i] == 'S') {
			lett[7]++;
		}
		if (mess[i] == 'G') {
			lett[8]++;
			lett[9]--;
			lett[3]--;
		}
		if (mess[i] == 'I') {
			lett[9]++;
		}
	}
	
	for (i = 0; i < 10; i++) {
		if (lett[i] != 0) {
			for (j = 0; j < lett[i]; j++) {
				printf("%d", i);
			}
		}
	}
	
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