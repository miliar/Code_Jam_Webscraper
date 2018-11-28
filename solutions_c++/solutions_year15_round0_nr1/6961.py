/* Dan Mitton

*/
#define _CRT_SECURE_NO_WARNINGS
#include <vector>
#include <valarray>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <algorithm>
#include <sstream>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <cstring>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <complex>



using namespace std;
typedef long long ll;
typedef long double ld;



int t = 1;
int maxShyness;
//length = 7;

int main()
{

	char filename[32];
	char infile[32], outfile[32];
	scanf("%s", filename);
	strcpy(infile, filename); strcpy(outfile, filename);
	strcat(infile, ".in"); strcat(outfile, ".out");
	FILE *fp = fopen(infile, "r"), *ofp = fopen(outfile, "w");


	fscanf(fp, "%d", &t);
	
	for (int i = 0; i < t; i++) {
		cout << i;

		//get the max shyness
		fscanf(fp, "%d", &maxShyness);
		cout << maxShyness << " ";

		int levels[1001];											//CHANGE THISSSSSSSSSSSSSS FOR LARGE
		int length = maxShyness + 1;
		int numFriends = 0;
		int numClappers = 0;

		//extra plus 1 for space
		for (int j = 0; j < length+1; j++) {
			
			
			char a = fgetc(fp);
			if (j == 0) {
				continue;
			}
			
			int b = a - '0';
			levels[j - 1] = b;			
		}
		
		for (int k = 0; k < maxShyness + 1; k++) {
			//update clappers:
			
			if (numClappers < k) {
				numFriends += (k - numClappers);
				numClappers += (k - numClappers);
			}
			numClappers += levels[k];
			
		}

		
		fprintf(ofp, "Case #%d: %d\n", i + 1, numFriends);
		cout << "\n";

	}
	return 0;
}