#include <iostream>
#include <fstream>
using namespace std;
int main(int argc, char *argv[])
{
    int t, a, b;
    int c[5] = {1, 4, 9, 121, 484};
    ifstream fin("C-small-attempt1.in", ios::in);
    ofstream fout("C.out", ios::out);
    fin >> t;
    for(int k=1; k<=t; k++)
    {
        fin >> a >> b;
        int count = 0;
        for(int i=0; i<5; i++)
        {
            if(c[i]>=a && c[i]<=b) ++ count;
        }
        fout << "Case #" << k << ": " << count << endl;
    }
    system("PAUSE");
    return 0;
}
