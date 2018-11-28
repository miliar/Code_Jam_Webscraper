#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

#define PROB "B"

//string inPath = PROB "-large.in";
//string outPath = PROB "-large.out";

string inPath = PROB "-small-attempt1.in";
string outPath = PROB "-small-attempt1.out";
//
//string inPath = "input.txt";
//string outPath = "output.txt";

bool is_asc_desc(const vector<int> &p, const vector<int> &v) {
    int l = 0;
    while(l + 1 < p.size() && v[p[l]] < v[p[l+1]])
        l++;
    
    for(; l + 1 < p.size(); ++l)
        if(v[p[l]] < v[p[l+1]])
            return false;
    return true;
}

int count(const vector<int> &v) {
    int ans = 0;
    for(int i = 0; i < v.size(); ++i)
        for(int j = i + 1; j < v.size(); ++j)
            if(v[i] > v[j])
                ans++;
    return ans;
}

int f(int n) {
    int ans = 1;
    for(int i = 1; i <= n; ++i)
        ans *= i;
    return ans;
}

int main(int argc, char** argv) {
    FILE * fin = fopen(inPath.c_str(), "r");
    FILE * fout = fopen(outPath.c_str(), "w");
    
    int tcases;
    fscanf(fin, "%d", &tcases);
    
    for(int tcase = 0; tcase < tcases; ++tcase) {
        printf("test %d...\n", tcase + 1);
        
        int n;
        fscanf(fin, "%d", &n);
        vector<int> s(n), p(n);
        
        for(int i = 0; i < n; ++i) {
            fscanf(fin, "%d", &s[i]);
            p[i] = i;
        }
   
        int ans = 1e9;
        
        int mx = f(n);
        for(int i = 0; i < mx; ++i) {
            if(is_asc_desc(p, s)) {
                int turns = count(p);
                if(turns < ans)
                    ans = turns;
            }
            
            next_permutation(p.begin(), p.end());
        }

        fprintf(fout, "Case #%d: %d\n", tcase+1, ans);
        

        printf("OK\n");
    }
    
    return 0;
}

