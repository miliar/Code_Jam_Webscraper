#include <iostream>
#include <fstream>
#include <list>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream f_in;
    ofstream f_out;
    f_in.open("input.txt");
    f_out.open("output.txt", ios_base::trunc );

    string temp;
    getline(f_in, temp);
    int T = stoi(temp);
    int N;
    string res = "";
    string S;
    vector<int> parties;

    for(int i=1; i<T+1; i++)
    {
        cout << "Case #" << i << ":";
        f_out << "Case #" << i << ":";

        getline(f_in, temp);
        N = stoi(temp);
        getline(f_in, S);

        std::size_t found = S.find_first_of(' ');
        int sum = 0;
        while (found != string::npos)
        {
            parties.push_back( stoi( S.substr(0, found) ) );
            sum += parties.back();
            S = S.substr(found+1, S.size() );
            found = S.find_first_of(' ', found);
        }
        parties.push_back( stoi( S ));
        sum += parties.back();

        for(int j=0; j<sum/2; j++)
        {
            int max = 0;
            int idmax = 0;
            for(int k=0; k<N; k++)
            {
                if( parties[k] > max )
                {
                    max = parties[k];
                    idmax = k;
                }
            }

            parties[idmax] = parties[idmax] -1;
            res.push_back( 'A'+idmax );

            max = 0;
            idmax = 0;
            if( j != ((sum/2)-1) || sum%2 == 0)
            {
                for(int k=0; k<N; k++)
                {
                    if( parties[k] > max )
                    {
                        max = parties[k];
                        idmax = k;
                    }
                }
                parties[idmax] = parties[idmax] -1;
                res.push_back( 'A'+idmax );
            }

            cout << " " << res;
            f_out << " " << res;
            res.clear();
        }

        if( sum%2 == 1 )
        {
            int max = 0;
            int idmax = 0;
            for(int k=0; k<N; k++)
            {
                if( parties[k] > max )
                {
                    max = parties[k];
                    idmax = k;
                }
            }

            parties[idmax] = parties[idmax] -1;
            res.push_back( 'A'+idmax );

            max = 0;
            idmax = 0;
            for(int k=0; k<N; k++)
            {
                if( parties[k] > max )
                {
                    max = parties[k];
                    idmax = k;
                }
            }

            parties[idmax] = parties[idmax] -1;
            res.push_back( 'A'+idmax );

            cout << " "<<res;
            f_out << " "<<res;
        }

        cout << endl;
        f_out << endl;
        parties.clear();
        res.clear();
    }

    f_in.close();
    f_out.close();
    return 0;
}
