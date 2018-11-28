#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

#define PROB "A"

string inPath = PROB "-large.in";
string outPath = PROB "-large.out";

//string inPath = PROB "-small-attempt0.in";
//string outPath = PROB "-small-attempt0.out";

//string inPath = "input.txt";
//string outPath = "output.txt";

int main(int argc, char** argv) {
    FILE * fin = fopen(inPath.c_str(), "r");
    FILE * fout = fopen(outPath.c_str(), "w");
    
    int tcases;
    fscanf(fin, "%d", &tcases);
    
    for(int tcase = 0; tcase < tcases; ++tcase) {
        printf("test %d...\n", tcase + 1);
        
        int n, x;
        fscanf(fin, "%d %d", &n, &x);
        vector<int> s(n);
        
        for(int i = 0; i < n; ++i)
            fscanf(fin, "%d", &s[i]);
        
        sort(s.begin(), s.end());
        
        int l = 0, r = n - 1, ans = 0;
        
        for(; l <= r; ++l) {
            while(r > l && s[l] + s[r] > x)
                r--, ans++;
            r--;
            ans++;
        }

        fprintf(fout, "Case #%d: %d\n", tcase+1, ans);
        

        printf("OK\n");
    }
    
    return 0;
}

