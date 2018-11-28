#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream myfile ("j.in");
    int t; myfile >> t;

    ofstream out;

    out.open ("ans.txt");
    for(int c = 0; c < t; c++){
        int a, b, k; myfile >> a >> b >> k;
        int r = 0;
        for(int i = 0; i < a; i++){
            for(int u = 0; u < b; u++){
                if((i & u) < k)
                    r++;
                else{
                    int v = i & u;
                    //cout << v << ">" << k << endl;
                }


            }
        }
        out <<"Case #"<< c+1 << ": " << r << endl;
    }

    return 0;
}
