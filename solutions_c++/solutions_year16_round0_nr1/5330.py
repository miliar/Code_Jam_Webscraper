#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
    //freopen("data.in", "rt", stdin);
    //freopen("data.out", "wt", stdout);
    unsigned long long N;
    int T;
    scanf("%d", &T);

    for(int i = 1; i <= T; ++i) {
        scanf("%lld", &N);
        if(N == 0)
            cout<< "Case #"<< i << ": " << "INSOMNIA\n" ;
        else {
            bool solved = false;
            unsigned long long cpy = N;
            int multiply = 1;
            vector<bool> found;
            found.assign(11, 0);
            int nrFound = 0;
            while(!solved && nrFound < 10) {
                cpy = N * multiply;
                while(cpy && nrFound < 10) {
                    if(found[cpy % 10] == false)
                        nrFound++;
                    found[cpy % 10] = true;
                    cpy = cpy / 10;
                }
                multiply++;
            }
            cout<< "Case #"<< i << ": " << N * (multiply - 1) << '\n';
        }
    }
    return 0;
}
