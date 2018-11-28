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
        int min;
        int max;
};

class Output
{
    public:
        int nb;
};

std::ostream& operator<<(std::ostream& o, const Output & output)
{
    o << output.nb;
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
        bool check(int nb)
        {
            int i = nb;
            int reverse = 0;
            while (i > 0)
            {
                reverse = 10 * reverse + i % 10;
                i /= 10;
            }
            return reverse == nb;
        }
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

        fs >> input.min;
        fs >> input.max;
    }
}

void Solver::solve(Input & input, Output & output)
{
    for (int i = sqrt(input.min); i <= sqrt(input.max); ++i)
    {
        if (check(i) && check(i*i) && i*i >= input.min)
            ++output.nb;
    }
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
