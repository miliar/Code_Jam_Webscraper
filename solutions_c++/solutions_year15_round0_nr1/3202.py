#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    if (!fin) {
        cout << "File not found" << endl;
        return 0;
    }
    int t;
    fin >> t;
    for (int tcase = 0; tcase < t; tcase++) {
        int smax;
        fin >> smax;
        string snums;
        fin >> snums;
        int tots = 0;
        int adds = 0;
        cout << "tcase " << (tcase + 1) << endl;
        for (int i = 0; i < smax; i++) {
            tots += snums[i] - '0';
            //cout << "found " << tots << " with slvl " << i << endl;
            if (tots < i + 1) {
                //cout << "adding " << i + 1 - tots << " for  slvl " << i << endl;
                adds += i + 1 - tots;
                tots = i + 1;
            }
        }
        fout << "Case #" << (tcase + 1) << ": " << adds << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
