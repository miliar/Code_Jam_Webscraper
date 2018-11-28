#include <fstream>
#include <vector>
using namespace std;

// Quaternion encoding:
// 1  = 0
// i  = 1
// j  = 2
// k  = 3
// -1 = -1
// -i = -2
// -j = -3
// -k = -4

int quat_mul(int a, int b)
{
    static int mul_table[4][4] = {
        {0, 1, 2, 3},
        {1, -1, 3, -3},
        {2, -4, -1, 1},
        {3, 2, -2, -1}
    };
    
    bool negate = ((a < 0 && b >= 0) || (a >= 0 && b < 0));
    if (a < 0)
        a = -1 * a - 1;
    if (b < 0)
        b = -1 * b - 1;
    int res = mul_table[a][b];
    return (negate) ? -1 * res - 1 : res;
}


int main(int argc, char * argv[])
{
    ifstream infile("dijkstra.in");
    ofstream outfile("dijkstra.out", ios_base::out | ios_base::trunc);
    
    unsigned int numCases, L, X, sample, letter, round;
    char c;
    int lookingFor, accu;
    vector<int> seq;
    vector<int>::const_iterator quat;
    infile >> numCases;
    for (sample = 1; sample <= numCases; sample++)
    {
        infile >> L >> X;
        seq.clear();
        seq.reserve(L);
        for (letter = 0; letter < L; infile.get(c))
            switch (c)
            {
                case 'i':
                    seq.push_back(1);
                    letter++;
                    break;
                case 'j':
                    seq.push_back(2);
                    letter++;
                    break;
                case 'k':
                    seq.push_back(3);
                    letter++;
                    break;
            }
        
        accu = 0;
        lookingFor = 1;
        for (round = 0; round < X; round++)
            for (quat = seq.begin(); quat != seq.end(); quat++)
            {
                accu = quat_mul(accu, *quat);
                if (accu == lookingFor)
                {
                    accu = 0;
                    lookingFor++;
                }
            }
        
        outfile << "Case #" << sample << ": ";
        if (lookingFor < 4 || accu != 0)
            outfile << "NO" << endl;
        else
            outfile << "YES" << endl;
    }
    
    return 0;
}