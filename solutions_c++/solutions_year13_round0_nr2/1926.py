#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

bool lawnmower(int **lawn, int n, int m) {
    vector<int> col;
    for(int j = 0; j < m; ++j) col.push_back(100);

    for(int i = 0; i < n; ++i) {
        int highest = 0;
        for(int j = 0; j < m; ++j) {
            if(lawn[i][j] > highest) highest = lawn[i][j];
        }

        for(int j = 0; j < m; ++j) {
            if(lawn[i][j] < highest && lawn[i][j] < col[j]) {
                col[j] = lawn[i][j];
            }
        }
    }

	for(int j = 0; j < m; ++j) {
		if(col[j] == 100) continue;
		for(int i = 0; i < n; ++i) {
			if(lawn[i][j] > col[j]) return false;
		}
	}
    
    return true;
}
        
int main(int argc, char **argv) {
    ifstream input(argv[1], ios::in);
    ofstream output("output.txt", ios::out);

    int T;
    input>>T;
    
    for(int t = 1; t <= T; ++t) {
        int n, m;
        input>>n>>m;

        int **lawn = new int*[n];
        for(int i = 0; i < n; ++i) {
            lawn[i] = new int[m];
            for(int j = 0; j < m; ++j) {
                input>>lawn[i][j];
			}
        }

        output<<"Case #"<<t<<": ";
        if(lawnmower(lawn, n, m)) output<<"YES"<<endl;
        else output<<"NO"<<endl;

        for(int i = 0; i < n; ++i) delete[] lawn[i];
        delete[] lawn;
    }

    return 0;
}
