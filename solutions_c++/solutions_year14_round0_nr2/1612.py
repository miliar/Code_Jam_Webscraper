#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

#define REP(i,N) for (int i = 0; i < N; ++i)

typedef unsigned long long int ulli;
typedef unsigned int ui;
typedef long long ll;

typedef vector<int> vi;

int main()
{
    cout.precision(7);
    cout.setf( std::ios::fixed, std:: ios::floatfield );

    int caseCount;
    cin >> caseCount;
    
    for (int csIx = 1; csIx <= caseCount; ++csIx)
    {
        double C,F,X,S;
        cin >> C >> F >> X;
        S = 2;
        double res = 0;
        
        while (X/S > C/S + X/(S+F))
        {
            res += C/S;
            S += F;
        }
        res += X/S;
        
        cout << "Case #" << csIx << ": " << res << endl;
    }
    
    return 0;
}
