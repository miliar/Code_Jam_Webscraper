#include "abstract_solver.h"
using namespace std;

class CaseSolver : public AbstractCaseSolver
{
public:
    virtual void ReadInput() override final
    {
        cin >> s;
    }

    virtual void Solve() override final
    {
        vector<int> sol(10, 0);
        vector<int> qtt(26);
        for (char c = 'A'; c <= 'Z'; ++c)
            qtt[c - 'A'] = Count(c);
        sol[0] = qtt['Z' - 'A'];
        sol[8] = qtt['G' - 'A'];
        sol[6] = qtt['X' - 'A'];
        sol[2] = qtt['W' - 'A'];
        sol[3] = qtt['H' - 'A'] - sol[8];
        sol[4] = qtt['U' - 'A'];
        sol[5] = qtt['F' - 'A'] - sol[4];
        sol[7] = qtt['V' - 'A'] - sol[5];
        sol[9] = qtt['I' - 'A'] - sol[5] - sol[6] - sol[8];
        sol[1] = qtt['N' - 'A'] - sol[7] - 2*sol[9];

        for (int i = 0; i < 10; ++i)
            out << string(sol[i], '0' + i);
        out << endl;
    }

    int Count(char c) const
    {
        int res = 0;
        for (char t : s)
            if (t == c)
                ++res;
        return res;
    }

private:
    string s;
};

int main()
{
    int cases;
    cin >> cases;
    ProblemSolver<CaseSolver> solver(cases);
}
