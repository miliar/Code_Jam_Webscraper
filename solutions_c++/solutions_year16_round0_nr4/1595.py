#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, char * argv[])
{
    if (argc != 2)
        return 0;
    
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    
    int T, t;
    int K, C, S;
    int i;
    
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        fin >> K >> C >> S;
        
        fout << "Case #" << t << ":";
        
        for (i = 1; i <= K; i++)
            fout << " " << i;
        
        fout << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}

