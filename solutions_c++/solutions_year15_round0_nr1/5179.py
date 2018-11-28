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
    int smax, a, sum, req;
    int audience[1001];
    int i;
    
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        fin >> smax >> a;
        
        for (i = smax; i >= 0; i--) {
            audience[i] = a % 10;
            a /= 10;
        }
        
        sum = 0;
        req = 0;
        
        for (i = 0; i <= smax; i++) {
            sum += audience[i];
            
            if (sum < i + 1) {
                req += i + 1 - sum;
                sum += i + 1 - sum;
            }
        }
        
        fout << "Case #" << t << ": " << req << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
