#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for(int i=1;i<=t;++i) {
        int a,b,c;
        in >> a >> b >> c;
        int win = 0;
        for(int j=0;j<a;++j) {
            for(int k=0;k<b;++k) {
                if((j & k) < c) {
                    ++win;
                }
            }
        }
        out << "Case #" << i << ": " << win << endl;
    }
    in.close();
    out.close();
    return 0;
}
