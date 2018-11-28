#include <iostream>
#include <cstdlib>
#include <vector>
#include <set>
#include <list>
#include <map>
#include <algorithm>
#include <cmath>
#include <string>
#include <sstream>
#include <fstream>

using namespace std;

template <class T> std::string toString( const T &t ) { ostringstream oss; oss << t; return std::string (oss.str()); }


class Input
{
    public:
        vector<vector<int> > lawn;
};

class Output
{
    public:
        bool possible;
};

std::ostream& operator<<(std::ostream& o, const Output & output)
{
    o << (output.possible ? "YES" : "NO");
    return o;
}

class Parser
{
    public:
        void parse(string filename, vector<Input> & input);
};

class Solver
{
    public:
        void solve(Input & input, Output & output);
};

void Parser::parse(string filename, vector<Input> & inputs)
{
    ifstream fs(filename);
    int nbCase;
    fs >> nbCase;
    inputs.resize(nbCase);

    for (int i = 0; i < nbCase; ++i)
    {
        Input & input = inputs[i];

        unsigned int row;
        unsigned int col;
        fs >> row;
        fs >> col;

        input.lawn.resize(row);
        for (unsigned int j = 0; j < row; ++j)
        {
            input.lawn[j].resize(col);
            for (unsigned int k = 0; k < col; ++k)
                fs >> input.lawn[j][k];
        }
    }
}

void Solver::solve(Input & input, Output & output)
{
    vector<int> maxRow;
    vector<int> maxCol;
    unsigned int row = input.lawn.size();
    unsigned int col = input.lawn[0].size();
    maxRow.resize(row);
    maxCol.resize(col);

    for (unsigned int j = 0; j < row; ++j)
        for (unsigned int k = 0; k < col; ++k)
            maxRow[j] = max(maxRow[j], input.lawn[j][k]);
    for (unsigned int j = 0; j < col; ++j)
        for (unsigned int k = 0; k < row; ++k)
            maxCol[j] = max(maxCol[j], input.lawn[k][j]);

    output.possible = true;
    for (unsigned int j = 0; j < row; ++j)
        for (unsigned int k = 0; k < col; ++k)
            if (input.lawn[j][k] < min(maxRow[j], maxCol[k]))
                output.possible = false;
}


int main(int argc, char * argv[])
{
    if (argc != 2)
    {
        std::cout << "no input!" << std::endl;
        return EXIT_FAILURE;
    }

    vector<Input> inputs;
    vector<Output> outputs;
    Parser p;
    Solver s;
    p.parse(argv[1], inputs);

    outputs.resize(inputs.size());
    for (unsigned int i = 0; i < inputs.size(); ++i)
        s.solve(inputs[i], outputs[i]);

    for (unsigned int c = 0; c < outputs.size(); ++c)
    {
        cout << "Case #" << c+1 << ": ";
        cout << outputs[c] << endl;
    }

    return EXIT_SUCCESS;
}
