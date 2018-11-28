#include <iostream>
#include <fstream>
#include <cmath>
#include <vector>
#include <string>

using namespace std;

void readInput(const char *fileName, vector<string> &v) {
	ifstream in_file;
    int nCases, n, m, h;
    vector<vector<int> > lawn;


	in_file.open(fileName, ifstream::in);
	if (in_file.fail()) cout << "**Opening file error**" << endl;
	else {
		in_file >> nCases;
		for (int i = 0; i < nCases; i++) {
		    in_file >> n;
		    in_file >> m;
		    lawn.clear();
		    lawn.resize(n);
		    for (int j = 0; j < n; j++) {
                for (int k = 0; k < m; k++) {
                    in_file >> h;
                    lawn[j].push_back(h);
                }
		    }

            int j = 0, k;
            bool possible = true;
            while (j < n and possible) {
                k = 0;
                while (k < m and possible) {
                    int l = 0;
                    while (l < n and possible) {
                        possible = lawn[l][k] <= lawn[j][k];
                        l++;
                    }
                    if (not possible) {
                        l = 0;
                        possible = true;
                        while (l < m and possible) {
                            possible = lawn[j][l] <= lawn[j][k];
                            l++;
                        }
                    }
                    k++;
                }
                j++;
		    }
		    if (possible) v.push_back("YES");
		    else v.push_back("NO");
		}
		in_file.close();
	}
}

void writeOutput(const char *fileName, vector<string> &v) {
	ofstream out_file;

	out_file.open(fileName, ofstream::out);
	if (out_file.fail()) cout << "**Opening file error**" << endl;
	else {
        for (int i = 0; i < v.size(); i++) out_file << "Case #" << i+1 << ": " << v[i] << endl;
		out_file.close();
	}
}

int main()
{
    vector<string> results;

    readInput("B-large.in", results);
    writeOutput("B-large.out", results);
    return 0;
}
