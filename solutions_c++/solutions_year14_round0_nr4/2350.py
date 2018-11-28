#include <algorithm>
#include <fstream>
using namespace std;


int main(int argc, char * argv[])
{
    ifstream fin;
    ofstream fout;
    int T, N, t, y, z, i, j, k;
    double naomi[1000], ken[1000];
    
    if (argc < 2)
        return 1;
    
    fin.open(argv[1]);
    fout.open("output.txt");
    
    fin >> T;
    
    for (t = 1; t <= T; t++) {
        fin >> N;
        y = z = 0;
        
        for (i = 0; i < N; i++)
            fin >> naomi[i];
        
        for (j = 0; j < N; j++)
            fin >> ken[j];
        
        sort(naomi, naomi + N);
        sort(ken, ken + N);
        
        
        i = 0;
        j = k = N-1;
        
        while (j >= i) {
            if (naomi[j] < ken[k]) {
                i++;
                k--;
            }
            else {
                j--;
                k--;
                y++;
            }
        }
        
        
        i = j = -1;
        
        while (j < N && i < N) {
            i++; j++;
            
            while (j < N && naomi[i] > ken[j])
                j++;
        }
        
        z = N - i;
        
        
        fout << "Case #" << t << ": " << y << ' ' << z << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}