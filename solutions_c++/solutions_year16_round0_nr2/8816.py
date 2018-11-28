#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;
typedef vector<bool> VB;

VB parse(const string& in)
{
    VB res(in.length(), false);
    for (int i = 0; i < in.length(); ++i)
        if (in[i] == '+')
            res[i] = true;
    return res;
}

void flip(VB& vb, int n)
{
    for (int i = 0; i <=n; ++i)
    {
        vb[i] = !vb[i];
    }
}

int run(VB& vb)
{
    int nswaps = 0;
    for (int i = vb.size() - 1; i >= 0; --i) {
        if (!vb[i]) {
            flip(vb, i);
            ++nswaps;
        }
    }
    return nswaps;
}

int main(int nargs, char** args)
{
    ifstream input("B-large.in");
    int nproblems = 0;
    input >> nproblems;

    ofstream output("pan-large.out");
    string buf;
    for (size_t i = 0; i < nproblems; ++i) {
        input >> buf;
        VB vb = parse(buf);
        int nswaps = run(vb);
        output << "Case #" << i+1 << ": " << nswaps << "\n";
    }

    return 0;
}
