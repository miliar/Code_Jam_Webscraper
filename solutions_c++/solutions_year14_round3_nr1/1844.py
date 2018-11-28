#include <iostream>
#include <algorithm>
#include <cctype>
#include <vector>
#include <stdlib.h>

using namespace std;

//unsigned long long

int solve(int P, int Q, int result);
void print(int result, int r);
int gcd_iterative(int a, int b);
bool isPower2(int x);

int main()
{
    int T, P, Q, pos, result, gcd;
    string s;
    
    cin >> T;

    for (int j = 1; j <= T; j++)
    {
        cin >> s;

        pos = s.find_first_of('/',0);

        P = atoi(s.substr(0,pos).c_str());
        Q = atoi(s.substr(pos+1).c_str());

        gcd = gcd_iterative(P,Q);
        P = P/gcd;
        Q = Q/gcd;

        if(!isPower2(Q)) result=0;
        else result = solve(P,Q,1);
        print(result, j);
    }

    return 0;
}

int solve(int P, int Q, int result)
{    
    if(P >= Q/2) return result;
    else solve(P,Q/2,result+1);
}

bool isPower2(int x)
{
    return ( (x > 0) && ((x & (x - 1)) == 0) );
}

int gcd_iterative(int a, int b) { if (b == 0) { return a; } else { return gcd_iterative(b, a % b); } }

void print(int result, int r)
{
    /*printf("Case #%d: %.7f\n", r, result);*/
    cout << "Case #" << r << ": ";
    if(result) cout << result << endl;
    else cout << "impossible\n";
}