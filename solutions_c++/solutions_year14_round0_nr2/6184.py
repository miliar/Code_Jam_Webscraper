

// C = cookies need for a farm
// F = rate farm produces cookies
// X = total need

// if buy n farms
// y = kn * (x - Tn)
// kn = 2 + nF
// Tn = C ( 1/k0 + 1/k1 + .. + 1/k(n-1) )

// when line n-1 and line n meets, the y is:
// y/kn + Tn = y/k(n-1) + T(n-1), so,
// C * (1/k(n-1) - 1/kn) * y  = 1/k(n-1)
// y = kn/(C * F) = (2/F + n) * C

// so if X/C > 2/F + n, we should buy n farms
// that is the number of farms should be bought is floor(X/C - 2/F)
// time needed is X/kn + Tn


#include <fstream>
#include <cmath>
#include <iomanip>
using namespace std;


int main()
{
    ifstream infile("file.in");
    ofstream outfile("file.out");
    
    int T = 0;
    infile >> T;
    
    for (int c = 1; c <= T; ++c) {
        double C, F, X;
        infile >> C >> F >> X;
        
        int n = std::max(0, (int)std::floor(X/C - 2./F));
        double kn = 2 + F * n;
        double Tn = 0;
        for (int i = 0; i < n; ++i) {
            Tn += C / (2 + F * i);
        }
        double t = X/kn + Tn;
        
        outfile << "Case #" << c << ": " 
                << std::fixed << std::setprecision(7) << t << endl;
    }
}

