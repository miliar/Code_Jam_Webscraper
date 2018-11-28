#include <cstdio>
#include <cstdlib>
#include <string>
#include <fstream>

using namespace std;

string inPath = "B-large.in";
string outPath = "B-large.out";

//string inPath = "B-small-attempt0.in";
//string outPath = "B-small-attempt0.out";

//string inPath = "input.txt";
//string outPath = "output.txt";

int main(int argc, char** argv) {
    FILE * fin = fopen(inPath.c_str(), "r");
    FILE * fout = fopen(outPath.c_str(), "w");
    
    int tcases;
    fscanf(fin, "%d", &tcases);
    
    for(int tcase = 0; tcase < tcases; ++tcase) {
        printf("test %d...", tcase + 1);
        double c, f, x, v=2;
        fscanf(fin, "%lf %lf %lf", &c, &f, &x);
        
        double ans = 0;
        
        while(x > 0) {
            if(x < c) {
                ans += x / v;
                break;
            }
            else {
                if(x / v > c / v + x / (v + f)) {
                    ans += c / v;
                    v += f;
                }
                else {
                    ans += x / v;
                    break;
                }
            }
        }
        
         
        fprintf(fout, "Case #%d: %.9lf\n", tcase+1, ans);
        printf("OK\n");
    }
    
    return 0;
}

