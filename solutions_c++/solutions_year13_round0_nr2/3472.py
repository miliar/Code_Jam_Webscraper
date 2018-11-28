#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>

#include <boost/lexical_cast.hpp>
#include <boost/assign.hpp>

using namespace std;
using namespace boost;
using namespace boost::assign;

int main(int argc, char** argv)
{
    auto& in = cin;
    auto& out = cout;

    out << setprecision(7);

    string line;
    getline(in, line);
    int nLines = boost::lexical_cast<int>(line); 


    for (int caseNo=0; caseNo < nLines; ++caseNo)
    {
        out << "Case #" << caseNo+1 << ": ";
        
        int N, M;
        in >> N >> M;

        int values[N][M];
        for (int i=0; i<N; ++i)
        {
            for (int j=0; j<M; ++j)
            {
                in >> values[i][j];
            }
        }

        vector<int> maxOfRow(N, 1);
        vector<int> maxOfColumn(M, 1);

        for (int i=0; i<N; ++i)
        {
            for (int j=0; j<M; ++j)
            {
                if (values[i][j] > maxOfRow[i])
                {
                    maxOfRow[i] = values[i][j];
                }
                if (values[i][j] > maxOfColumn[j])
                {
                    maxOfColumn[j] = values[i][j];
                }
            }
        }
        bool foundFailure = false;
        for (int i=0; i<N && !foundFailure; ++i)
        {
            for (int j=0; j<M && !foundFailure; ++j)
            {
                if (values[i][j] != min(maxOfRow[i], maxOfColumn[j]))
                {
                    foundFailure = true;
                }
            }
        }
        
        if (foundFailure)
        {
            out << "NO";
        }
        else
        {
            out << "YES";
        }

        out << endl;
    }


    return 0;
}

