#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, const char *argv[])
{
    std::fstream fin( argv[1] );

    int cases;
    fin >> cases;
    for( int i = 1; i <= cases; i++ ){
        std::cout << "Case #" << i << ": ";
        unsigned int a, b, k;
        fin >> a >> b >> k;

        unsigned int combi = a * b;

        unsigned int ans = 0;
        for (int x = 0; x < a; x++) {
            for (int y = 0; y < b; y++) {
                if ( (x & y) < k )
                    ans++;
            }
        }
        cout << ans;
        
        cout << endl;
    }

    return 0;
}
