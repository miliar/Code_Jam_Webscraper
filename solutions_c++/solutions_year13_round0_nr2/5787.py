#include <set>
#include <map>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
#include <list>
#include <cassert>
#include <climits>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <fstream>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <stdexcept>

using namespace std;

string countP(int N, int M, vector<vector<int> > &a) {
    for(int i = 0; i < a.size(); i++) {
        for(int j = 0; j < a[i].size(); j++) {
            if(a[i][j] == 1) {
                int c = 0, c1 = 0;
                for(int m = 0; m < a[i].size(); m++) {
                    if(a[i][m] == 1) {
                        c++;
                    }
                }
                for(int k = 0; k < a.size(); k++) {
                    if(a[k][j] == 1) {
                        c1++;
                    }
                }
                if(c != a[i].size() && c1 != a.size()) {
                    return "NO";
                }
            }
        }
    }

    return "YES";
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;

    for(int c = 1; c < T+1; c++) {
        int N, M;
        cin >> N >> M;
        vector<vector<int> > a(N, vector<int> (M,0));
        for(int i = 0; i < N; i++) {
            for(int j = 0; j < M; j++) {
                cin >> a[i][j];
            }
        }

        cout << "Case #" << c << ": " << countP(N,M,a) << endl;
    }


    return 0;
}


