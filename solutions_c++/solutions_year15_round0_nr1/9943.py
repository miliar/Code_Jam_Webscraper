#include <iostream>
#include <fstream>
#include <sstream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    ofstream fout("ans.txt");
    int all;
    scanf("%d",&all);
    
    for (int i = 0; i < all; i ++) {
        int line;
        char shys[1001], shy;
        scanf("%d",&line);
        int need = 0;
        int have = 0;
        scanf("%s",shys);
        for (int j = 0; j < line+1; j++) {
            shy = shys[j]-'0';
            if (j > 0)
            {
                if (shy > 0 && have < j)
                {
                    need += (j-have);
                    have = j;
                }
                have += shy;
            }
            else
                have += shy;
            
        }
        
        //       fout << num ;
        cout << "Case #" << i+1 <<": " << need << "\n";
        fout <<"Case #" << i+1 <<": " << need;
        fout << "\n";
    }
}
