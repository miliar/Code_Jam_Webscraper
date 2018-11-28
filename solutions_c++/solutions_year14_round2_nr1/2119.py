#include <fstream>
#include <iostream>
#include <string>
using namespace std;


inline int myabs(int n) { return (n > 0 ? n : n * -1); }


int main(int argc, char * argv[])
{
    if (argc < 2)
        return 1;
    
    ifstream fin(argv[1]);
    ofstream fout("output.txt");
    int T, x, y, count[100], i, j;
    string a, b, c, d;
    
    fin >> T;
    
    for (x = 1; x <= T; x++) {
        fin >> i; // dump
        fin >> a >> b;
        
        c = a[0];
        j = 0;
        
        for (i = 0; i < a.length(); i++)
            if (a[i] != c[j]) {
                c += a[i];
                j++;
            }
        
        d = b[0];
        j = 0;
        
        for (i = 0; i < b.length(); i++)
            if (b[i] != d[j]) {
                d += b[i];
                j++;
            }
        
        if (c != d) {
            fout << "Case #" << x << ": Fegla Won" << endl;
            continue;
        }
        
        for (i = 0; i < 100; i++)
            count[i] = 0;
        
        count[0] = 1;
        j = 0;
        
        for (i = 1; i < a.length(); i++) {
            if (a[i] != a[i-1])
                j++;
            
            count[j]++;
        }
        
        count[0]--;
        j = 0;
        
        for (i = 1; i < b.length(); i++) {
            if (b[i] != b[i-1])
                j++;
            
            count[j]--;
        }
        
        y = 0;
        
        for (i = 0; i < 100; i++)
            y += myabs(count[i]);
        
        fout << "Case #" << x << ": " << y << endl;
    }
    
    fin.close();
    fout.close();
    
    return 0;
}
