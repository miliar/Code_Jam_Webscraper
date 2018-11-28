#include <iostream>
#include <vector>
#include <algorithm>
#include <bitset>
#include <fstream>

using namespace std;

typedef long long ll;

string ans(int n, int r, int p, int s) {
    if (max(r, max(p, s)) - min(r, min(p, s)) != 1) {
        return "IMPOSSIBLE";
    }
  
    if (n == 1){
        if (r == 1 && p == 1 && s == 0) return "PR";
        if (r == 1 && p == 0 && s == 1) return "RS";
        if (r == 0 && p == 1 && s == 1) return "PS";
    }
    else if (n == 2) {
        if (r == 2 && p == 1 && s == 1) return "PRRS";
        if (r == 1 && p == 2 && s == 1) return "PRPS";
        if (r == 1 && p == 1 && s == 2) return "PSRS";
    
    }
    else if (n == 3) {
        if (r == 2 && p == 3 && s == 3) return "PRPSPSRS";
        if (r == 3 && p == 2 && s == 3) return "PRRSPSRS";
        if (r == 3 && p == 3 && s == 2) return "PRPSPRRS";
    }
  
    return "IMPOSSIBLE";
}

int main() {
    ofstream fout;
    fout.open ("ayylmao.txt");
    ifstream fin;
    fin.open ("A-small-attempt0.in");

    int t; fin >> t;
  
    for (int i = 1; i <= t; i++) {
        int n, r, p, s; fin >> n >> r >> p >> s;
        fout << "Case #" << i << ": " << ans(n,r,p,s) << endl;
    }
}