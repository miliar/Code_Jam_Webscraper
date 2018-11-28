#include <iostream>
#include <fstream>

using namespace std;


void flip(string & S, int sl);


int main(int argc, char * argv[])
{
    if (argc != 2)
        return 0;
    
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    
    int T, t;
    string S;
    int sl, ff;
    int mc;
    
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        fin >> S;
        sl = S.length();
        
        mc = 0;
        
        for (;;) {
            while (sl > 0 && S[sl - 1] == '+')
                sl--;
            
            if (sl == 0)
                break;
            
            ff = 0;
            
            while (ff < sl && S[ff] == '+')
                ff++;
            
            if (ff > 0) {
                flip(S, ff);
                mc++;
            }
            
            if (ff < sl) {
                flip(S, sl);
                mc++;
            }
        }
        
        fout << "Case #" << t << ": " << mc << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}


void flip(string & S, int sl)
{
    string St = S;
    int i;
    
    for (i = 0; i < sl; i++)
        S[sl - i - 1] = (St[i] == '+' ? '-' : '+');
}
