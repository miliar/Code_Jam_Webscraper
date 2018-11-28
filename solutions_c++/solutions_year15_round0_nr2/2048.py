#include <iostream>
#include <cmath>

using namespace std;

int mem[1001][1001];

void setup() {
    for (int i = 0; i < 1001; i++)
	for (int j = 0; j < 1001; j++)
	    mem[i][j] = -1;
}

int solve(int index, int maxim, int *values, int length) {
    if (index >= length)
	return maxim;
    if (mem[index][maxim] != -1)
	return mem[index][maxim];
    int best = 1000000000;
    for (int i = 1; i <= values[index]; i++) {
	int cur_solution = i-1 + solve(index+1, max(maxim, (int)ceil((float)values[index]/i)), values, length);
	best = min(best, cur_solution);
    }
    mem[index][maxim] = best;
    return mem[index][maxim];
}

int main(void) {
    int n_cases;
    cin >> n_cases;
    for (int i = 0; i < n_cases; i++) {
	setup();
	int n_diners;
	cin >> n_diners;
	int values[n_diners];
	for (int i = 0; i < n_diners; i++)
	    cin >> values[i];
	int s = solve(0, 0, values, n_diners);
	cout << "Case #" << i+1 << ": " << s << endl;
    }
}
