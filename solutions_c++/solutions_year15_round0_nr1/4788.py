#include <iostream>
#include <fstream>

using namespace std;

int data[1005];

int sub(int poi, int parsum, int invnum){
    int tmp;
    tmp = poi - parsum - invnum;
    if (tmp > 0) return tmp;
    else return 0;
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("ouput-large.txt");
    int T, smax, parsum = 0, invnum = 0;
    char tmpchar;
    fin >> T;
    for (int i = 0; i < T; ++i){
        parsum = 0;
        invnum = 0;
        fin >> smax;
        fin >> tmpchar;
        data[0] = tmpchar - '0';
        for(int j = 1; j <= smax; ++j){
            fin >> tmpchar;
            data[j] = tmpchar - '0';
            parsum += data[j-1];
            invnum += sub(j, parsum, invnum);
        }
        fout << "Case #" << i+1 <<": " << invnum << endl;
    }
    fin.close();
    fout.close();
    return 0;
}
