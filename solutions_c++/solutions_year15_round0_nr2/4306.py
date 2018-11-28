#include <iostream>
#include <fstream>
using namespace std;


int main(int argc, char * argv[])
{
    if (argc != 3) {
        cout << "Usage: " << argv[0] << " <filein> <fileout>" << endl;
        return 0;
    }
    
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    
    int T, t;
    int D;
    int P[10];
    int max1, max2;
    int i, j;
    int time, norm;
    
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        fin >> D;
        time = 0;
        
        for (i = 1; i <= 9; i++)
            P[i] = 0;
        
        for (i = 0; i < D; i++) {
            fin >> j;
            P[j]++;
        }
        
        
        i = 9;
        
        
        
        if (P[i] == 1) {
            norm = 9;
            j = 8;
            
            while (P[j] == 0)
                j--;
            
            if (j <= 3 || j == 6) {
                time++;
                P[9] = 0;
                P[6]++;
                P[3]++;
            }
        }
        else {
            while (P[i] == 0)
                i--;
            
            norm = i;
        }
        
        for (;;) {
            while (P[i] == 0 && i > 0)
                i--;
            
            if (i == 0)
                break;
            
            j = i-1;
            
            while (P[j] == 0 && j > 0)
                j--;
            
            if (i <= P[i]) {
                time += i;
                break;
            }
            
            if (i/2 + i%2 + P[i] < i) {
                P[i/2 + i%2] += P[i];
                P[i/2] += P[i];
                time += P[i];
                P[i] = 0;
            }
            else {
                time += i;
                break;
            }
        }
        
        
        fout << "Case #" << t << ": " << min(time, norm) << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
