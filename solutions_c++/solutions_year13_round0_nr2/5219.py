#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>
#include <fstream>
#include <map>
#include <algorithm>
#include <utility>

using namespace std;

int main(int argc, char** argv) {

    ifstream in("input.in");
    ofstream out("output.in");

    int M, N, C, v;
    string str;

    in >> C;
    getline(in, str);

    for (int cs = 0; cs < C; cs++) {
        in >> N >> M;
        vector< vector<int> > l(N);
        vector< vector<int> > l_c(M);

        getline(in, str);

        for (int r = 0; r < N; r++) {
            for (int a = 0; a < M; a++) {
                in >> v;
                l[r].push_back(v);
            }
            getline(in, str);
        }
        
        for (int c = 0; c < M; c++) {
            for (int r = 0; r < N; r++) {
                l_c[c].push_back(l[r][c]);
            }
        }
        
        int total = N*M;        
        map< pair<int, int>, int> mp;

        for (int r = 0; r < N; r++) {
            int t = *max_element(l[r].begin(),l[r].end());
            for (int c = 0; c < M; c++) {
                if (t == l[r][c]) {
                    mp[make_pair(r, c)] = 1;
                }
            }
        } 
        
        for (int c = 0; c < M; c++) {
            int t= *max_element(l_c[c].begin(),l_c[c].end());
            for (int r = 0; r < N; r++) {
                if (t == l_c[c][r]) {
                    mp[make_pair(r, c)] = 1;
                }
            }
        }
        
        if(total == mp.size())
            out << "Case #" << cs+1 << ": YES" << endl;
        else
            out << "Case #" << cs+1 << ": NO" << endl;

    }

    return 0;
}

