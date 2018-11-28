#include <iostream>
#include <string>
#include <vector>
#include <math.h>
#include <limits.h>
using namespace std;

typedef long long mlong;
int main(int argc, char **argv) {
    int T;
    cin >> T;
    for (int i = 0; i < T; i ++) {
	int N;
	cin >> N;
	vector<vector<int> > square(2 * N - 1);
	for (int j = 0; j < 2 * N - 1; j ++) {
	    vector<int> line(N);
	    for (int k = 0; k < N; k ++) {
		cin >> line[k];
	    }
	    square[j] = line;
	}

	vector<int> missing(N);
	vector<bool> processed(2 * N - 1, false);
	// for each line, find the min element corresponding to this line
	for (int j = 0; j < N; j ++) {
	    int sum = 0;
	    int m = INT_MAX;
	    int r = -1, c = -1;
	    for (int k = 0; k < 2 * N - 1; k ++) {
		sum -= square[k][j];
		if (!processed[k]) {
		    if (square[k][j] < m) {
			m = square[k][j];
			r = k;
			c = -1;
		    }
		    else if (square[k][j] == m) {
		      c = k;
		    }
		}
	    }
	    
	    // if only one min element, this is the missing element. 
	    if (c == -1) {
	      missing[j] = m;
	      processed[r] = true;
	    }
	    
	    // otherwise, take the lines with this element and 
	    // add them up, minus the sum is the missing element. 
	    
	    else {
	      for (int k = 0; k < N; k ++) {
		sum += square[r][k];
		sum += square[c][k];
	      }
	      processed[r] = true;
	      processed[c] = true;
	      missing[j] = sum;
	    }
	}
	
	cout << "Case #" << i + 1 << ":";
	for (int j = 0; j < N; j ++) {
	    cout << " " << missing[j];
	}
	cout << endl;
    }
}
