#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>

using namespace std;

ifstream f ("C-small-attempt0.in");
ofstream g ("C-small-attempt0.out");

long long getDiv(unsigned long long nr, int (&divs)[9]) {
    long long root = (long long) sqrt(nr);
    for (int div = 2; div <= root; div++) {
        if (nr % div == 0) {
            bool ok = true;
            for(int i = 0; i < 10; i++) {
                if(div == divs[i]) {
                    ok = false;
                }
            }

            if (ok) {
                return div;
            }
        }
    }
    return -1;
}

long long getDiv(unsigned long long nr) {
    long long root = (long long) sqrt(nr);
    for (int div = 2; div <= root; div++) {
        if (nr % div == 0) {
            return div;
        }
    }
    return -1;
}

long long convertToDecimal(vector<int> sequence, unsigned int base) {
    long long pow = 1;
    long long result = 0;
    for(long long i = sequence.size() - 1; i >= 0; i--) {
        result += sequence[i] * pow;
        pow *= base;
    }
    return result;
}

int n,x[100], jams, maxJams, t;

bool verifyJam() {
    vector<int> temp;

    temp.push_back(1);
    for (int i = 1; i <= n; i++ ) {
        temp.push_back(x[i]);
    }
    temp.push_back(1);

    bool ok = true;
    int divs[] = {0, 0, 0, 0, 0, 0, 0, 0, 0};

    for(int i = 2; i <= 10; i++) {
        long long curr = convertToDecimal(temp, i);
        int currDiv = getDiv(curr);

        if(currDiv == -1) {
            return false;
        } else {
            divs[i-2] = currDiv;
        }
    }

    for(int i = 0; i<temp.size(); i++) {
        g<<temp[i];
    }

    for(int i = 0; i<9; i++) {
        g<<" "<<divs[i];
    }

    g<<"\n";

    jams++;
}

int succ(int k)
{
    if(x[k]<1)
    {
        x[k]++;
        return 1;
    }
    return 0;
}

void bt(int k)
{
    x[k]=-1;
    while(succ(k) && jams < maxJams) {
        if(k==n) {
            verifyJam();
        } else {
            bt(k+1);
        }
    }

}

int main()
{
    f>>t>>n>>maxJams;
    n -= 2;

    g<<"Case #1:\n";

    bt(1);


    f.close();
    g.close();
    return 0;
}
