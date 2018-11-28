#include <iostream>  // includes cin to read from stdin and cout to write to stdout

using namespace std;  // since cin and cout are both in namespace std, this saves some text


int printresult(int r1, int r2)
{
	//printf("(%d-%d)", r1, r2);
	if (r1 != -1)
		printf("%c", r1 + 'A');
	if (r2 != -1)
		printf("%c", r2 + 'A');
	printf(" ");
	return 0;
}
void main() {
	int t, n, i, r1 = 0, r2 = 0, m1, m2, p[26], r[26];
	int last = 0;
	int c0 = 0, c1 = 0;
	int loop = 0;
	int ci = 0;

	cin >> t;  // read t. cin knows that t is an int, so it reads it as such.
			   //printf("max case = %d\n", t);
	for (ci = 1; ci <= t; ci++) {
		cin >> n;  // read n and then m.
		for (i = 0; i<n; i++) {
			r[i] = 0;
			cin >> p[i];
		}

		cout << "Case #" << ci << ": ";
		//for(i=0;i<n;i++)
		//		printf("p[%d]=%d;",i,p[i]);
		last = 0;
		while (last != 1) {
			// find the largest,2nd largest number-1t
			loop++;

			m1 = p[0];
			r1 = 0; r2 = -1;
			for (i = 1; i<n; i++) {
				if (p[i]>m1) {
					m1 = p[i];
					r1 = i;
				}
			}
			if (p[r1] == 0)
				r1 = -1;
			else
				p[r1]--;

			m2 = p[0];
			r2 = 0;
			for (i = 1; i<n; i++) {
				if (p[i]>m2) {
					m2 = p[i];
					r2 = i;
				}
			}
			if (p[r2] == 0)
				r2 = -1;
			else
				p[r2]--;
			// check if balance is 1+n
			c0 = 0; c1 = 0;
			for (i = 0; i<n; i++) {
				if (p[i] == 0)
					c0++;
				if (p[i] == 1)
					c1++;
			}
			if (c0 == n)
				last = 1;
			if (c1 == 1 && c0 == n - 1) {
				p[r2]++;
				r2 = -1;
			}
			printresult(r1, r2);


			// cout << "Case #" << i << ": " << res <<  endl;
		}
		cout << endl;
	}
}


// Usgae: MY_PROGRAM < input_file.txt > output_file.txt