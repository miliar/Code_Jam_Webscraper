#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
#include <sstream>
#include <fstream>
#include <cctype>

using namespace std;

bool valid(vector<vector<int> >& lawn, int N, int M) {
    if (N == 0 || M == 0) 
        return 1;
        
    int counter = 0;
    for (int n = 0; n != N; ++n) {
        for(int m = 0; m != M; ++m) {
            int temp = lawn[n][m];
            bool n_possible = 0, m_possible = 0;
            int counter_n = 0;
            for(int i = 0; i != N; ++i) {
                if(temp >= lawn[i][m])
                    ++counter_n;
            }
            if (counter_n == N) {
                n_possible = 1;
                ++counter;
                continue;
            }
            int counter_m = 0;
            for(int i = 0; i != M; ++i) {
                if(temp >= lawn[n][i])
                    ++counter_m;
            }
            if (counter_m == M) {
                m_possible = 1;
                ++counter;
            }
        }
    }
    if (counter == N*M)
        return 1;
    return 0;
}

int main()
{
    ifstream infile("B-large.in");
    ofstream outfile("out.txt");
    int cases;
    string line;
    getline(infile, line);
    istringstream str(line);
    str >> cases;
    //cout << cases << endl;
    for (int j = 0; j != cases; ++j) {
        getline(infile, line);
        istringstream first(line);
        int N, M;
        first >> N >> M;
        vector<vector<int> > lawn;
        for (int n = 0; n != N; ++n) {
            getline(infile, line);
            istringstream lawnl(line);
            int temp;
            vector<int> lawnline;
            while (lawnl >> temp)
                lawnline.push_back(temp);
            lawn.push_back(lawnline);
        }
        string out = (valid(lawn, N, M) ? "YES": "NO");
        outfile << "Case #" << j+1 << ": " << out << endl;
    } 
    return 0;
}