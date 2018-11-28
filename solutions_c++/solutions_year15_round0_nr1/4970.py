#include <fstream>
#include <string>
#include <iostream>
#include <boost/lexical_cast.hpp>

int main()
{
using namespace std;

    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int N;
    fin >> N;
    for(int i=0; i<N; ++i)
    {
        int T;
        fin >> T;
        string str;
        fin >> str;
        int stood = 0;
        int friends = 0;
        for(int need=0; need<T+1; need++)
        {
            if(need>stood)
            {
                friends += need-stood;
                stood = need;
            }
            int to_stand = boost::lexical_cast<int>(str[need]);
//            cout << "To_stand: " << to_stand << endl;
            stood += to_stand;
        }
        fout << "Case " << "#" << i+1 << ": " << friends << endl;
    }
    fin.close();
    fout.close();
}
