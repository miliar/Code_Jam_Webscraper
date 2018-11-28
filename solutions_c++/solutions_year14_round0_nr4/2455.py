#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

string inPath = "D-large.in";
string outPath = "D-large.out";

//string inPath = "D-small-attempt0.in";
//string outPath = "D-small-attempt0.out";

//string inPath = "input.txt";
//string outPath = "output.txt";

int main(int argc, char** argv) {
    FILE * fin = fopen(inPath.c_str(), "r");
    FILE * fout = fopen(outPath.c_str(), "w");
    
    int tcases;
    fscanf(fin, "%d", &tcases);
    
    for(int tcase = 0; tcase < tcases; ++tcase) {
        printf("test %d...", tcase + 1);

        int n;
        fscanf(fin, "%d", &n);
        
        vector<double> p1(n), p2(n);
        for(int i = 0; i < n; ++i)
            fscanf(fin, "%lf", &p1[i]);
        for(int i = 0; i < n; ++i)
            fscanf(fin, "%lf", &p2[i]);
        
        sort(p1.begin(), p1.end());
        sort(p2.begin(), p2.end());
        
        int a1 = 0, l = 0, r = n-1;
        
        for(int i = n-1; i >= 0; --i) {
            if(p1[r] > p2[i]) {
                a1++;
                r--;
            }
            else
                l++;
        }
        
        int a2 = n;
        l = 0;
        
        for(int i = 0; i < n && l < n; ++i) {
            while(l < n && p2[l] < p1[i])
                l++;
            if(l < n)
                a2--;
            l++;
        }
        
        fprintf(fout, "Case #%d: %d %d\n", tcase+1, a1, a2);
        printf("OK\n");
    }
    
    return 0;
}

