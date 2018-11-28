#include <fstream>
using namespace std;

int main(int argc, char * argv[])
{
    if (argc < 2)
        return 1;
    
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    
    int T, x, y, A, B, K, i, j;
    
    fin >> T;
    
    
    for (x = 1; x <= T; x++) {
        fin >> A >> B >> K;
        
        y = 0;
        
        for (i = 0; i < A; i++)
            for (j = 0; j < B; j++)
                if ((i & j) < K)
                    y++;
        
        fout << "Case #" << x << ": " << y << endl;
    }
    
    
    fin.close();
    fout.close();
    
    return 0;
}
