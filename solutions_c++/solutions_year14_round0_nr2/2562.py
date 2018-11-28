#include <cstdio>
#include <fstream>
using namespace std;


int main(int argc, char * argv[])
{
    ifstream fin;
    FILE* fout;
    double a;
    int T, t;
    double C, F, X, time, cps;
    
    if (argc < 2)
        return 1;
    
    fin.open(argv[1]);
    fout = fopen("output.txt", "w");
    
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        fin >> C >> F >> X;
        cps = 2.0;
        time = 0;
        
        while (X/cps > C/cps + X/(cps + F)) {
            time += C/cps;
            cps += F;
        }
        
        fprintf(fout, "Case #%d: %.7lf\n", t, time + X/cps);
    }
    
    fin.close();
    fclose(fout);
    
    return 0;
}