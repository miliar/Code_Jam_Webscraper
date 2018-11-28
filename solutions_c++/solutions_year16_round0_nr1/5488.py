#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <bitset>


using namespace std;

int main()
{
//    ifstream fin("input.in");
    //ifstream fin("A-small-attempt0.in");
    ifstream fin("A-large.in");
    ofstream fout("output.out");

    //-- check if the files were opened successfully
    if (!fin.is_open()) cout << "input.in was not opened successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int numCase;
    fin >> numCase;

    int N = 0;
    std::string audience;
    int ans = 0;

    for (int i = 0; i < numCase; i++)
    {
        fin >> N;
        int NN = N;
        bitset<10> bs;
        if (N ==0) fout << "Case #" << (i + 1) << ": " << "INSOMNIA" << endl;
        else {
            bool notFound = true;
            int ind = 1;
            while (notFound)
            {
                std::string str = std::to_string(NN*ind);
                for (auto c : str)
                {
                    bs.set(int(c)-48);
                }
                if (bs.all()) notFound = false;
                else {
                ind++;
                }
            }

            fout << "Case #" << (i + 1) << ": " << NN*ind << endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}
