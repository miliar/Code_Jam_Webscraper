#include <iostream>
#include <cstdlib>
#include <cmath>
#include <string>
#include <algorithm>

char s[100][101];
int count[100];

void solve(int id) {
	// local variables
    int n = 0;
    std::cin>>n;
    
	// read data
    for (int i = 0; i < n; i++) {
        std::cin>>s[i];
    }
	// process
    int *index = new int[n];
    memset(index, 0, n * sizeof(int));
    int count = 0;
    int *move = new int[n];
    memset(move, 1, n * sizeof(int));
    bool flag = true;
    while (flag) {
        flag = false;
        char base = s[0][index[0]];
        while (s[0][index[0]] != '\0' && s[0][index[0]] == s[0][index[0]+1]) {
            index[0]++;
            move[0]++;
        }
        for (int i = 1; i < n; i++) {
            if (s[i][index[i]] != base) {
                printf("Case #%d: Fegla Won\n", id);
                return;
            }
            while (s[i][index[i]] == s[i][index[i]+1]) {
                index[i]++;
                move[i]++;
            }
            index[i]++;
            if (s[i][index[i]] != '\0') {
                flag = true;
            }
        }
        int sum = 0; 
        for (int i = 0; i < n; i++)
            sum += move[i];
        sum /= n;
        for (int i = 0; i < n; i++) {
            count += abs(move[i] - sum);
        }
        if (s[0][index[0]] != '\0') {
            index[0]++;
        }
        if (s[0][index[0]] != '\0') {
            flag = true;
        }
        memset(move, 1, n * sizeof(int));
    }
	// output
	printf("Case #%d: %d\n", id, count);
    delete [] move;
    delete [] index;
}

int main(int argc, char *argv[]) {
	int t = 0;
	std::cin>>t;
	for (int i = 1; i <= t; i++) {
		solve(i);
	}
}
