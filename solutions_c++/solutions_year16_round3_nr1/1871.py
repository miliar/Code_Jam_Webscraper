

#include <iostream>
#include <fstream>
using namespace std;

ifstream fin ("/Users/Andrew/Desktop/File.txt");
ofstream fout("/Users/Andrew/Desktop/output.txt");

int main(int argc, const char * argv[]) {

    int tests;
    fin >> tests;
    int a[27];
    int b;
    int testscnt = 1;
    while (tests--){
        fout << "Case #"   << testscnt++ << ": ";
        int n;
        fin >> n;
        for (int i = 1; i <= n; ++i){
            fin >> b;
            a[i] = b;
        }
        for (int k = 1; k <= 1000; ++k){
//            cout << k << endl;
            int mx = 0;
            int index = 0;
            int cnt = 0;
            int diff = 0;
            
            
            
            for (int j = 1; j <= n; ++j){
                
                if (a[j] > mx)
                {
                    mx = a[j];
                    index = j;
                }
                cnt += a[j];
                if (a[j])
                    diff++;
            }
            
            
            if (cnt == 0)
                break;
            
            if (diff == 2){
                for (int i = 1; i <= n; ++i){
                    if (a[i] != 0){
                        fout << char('A' - 1 + i);
                        a[i]--;
                    }
                }
                fout << ' ' ;
                continue;
            }
            
            if ((mx - 1) * 2 > cnt){
                a[index] -= 2;
                fout << char('A' - 1 + index) << char('A' - 1 + index) << endl;
                continue;
            }
            fout << char('A' - 1 + index) << ' ';
            a[index]--;

            
        }
        fout << endl;
        
        
    }

    return 0;
}
