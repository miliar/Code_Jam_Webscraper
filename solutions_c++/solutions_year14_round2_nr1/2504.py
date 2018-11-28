#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <map>
#include <vector>
#include <stack>
#include <queue>
#include <fstream>
#include <cstring>

using namespace std;

int T, N;
vector<string> w;
int c[101][101];
string fw;

void reset() {
    for (int i = 0; i < 100; i++) {
        for (int j = 0; j < 100; j++ ) {
            c[i][j] = 0;
        } 
    }
}

string getInfo(int ind) {
    fw = w[ind][0];
    
    for (int i = 1; i < w[ind].size(); i++) {
        if (w[ind][i] != w[ind][i-1]) {
            fw += w[ind][i];
        } else {
            c[ind][fw.size()-1]++;
        }
    }
    
    return fw;
}

bool isPossible() {
    bool isAllGood = true;

    string pw = getInfo(0);
    for (int i = 1; i < N && isAllGood; i++) {
        if (!(pw.compare(getInfo(i)) == 0)) isAllGood = false;
    }
    
    return isAllGood;
}

int solve() {
    int aux[N];
    int res = 0;
    
    for (int i = 0; i < fw.size(); i++) {
        for (int j = 0; j < N; j++) {
            aux[j] = c[j][i];
        }
        
        sort(aux, aux + N);
    
        int m = aux[N/2];
        
        for (int j = 0; j < N; j++)
            res += abs(m - aux[j]);
        
    }
    
    return res;
}

int main() {
    cin >> T;
    string line;
    int r;
    for (int i = 0; i < T; i++) {
        reset();
    
        cin >> N;
        for (int j = 0; j < N; j++) {
            cin >> line;
            w.push_back(line);
        }
        
        if (!isPossible()) printf("Case #%d: Fegla Won\n", i+1);
        else printf("Case #%d: %d\n", i+1, solve());
        
        w.clear();
    }
    return 0;
}
