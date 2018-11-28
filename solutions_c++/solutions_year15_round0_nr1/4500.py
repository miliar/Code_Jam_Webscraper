#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream f("A-small-attempt2.in");
    ofstream g("output.txt");
    int T;
    f >> T;
    for (int i=0;i<T;++i) {
        int Smax;
        f >> Smax;

        int friends = 0;
        int clapping = 0;
        char Si;
        for (int j=0;j<=Smax;++j) {
            // j db embernek kell tapsolnia, hogy a j. pakk is tapsoljon
            f >> Si;
            Si -= '0';
            if (Si != 0 && clapping < j) {
                friends += j-clapping;
                clapping += friends;
            }
            clapping += Si;
        }
        g << "Case #" << i+1 << ": " << friends << endl;
    }
    return 0;
}
