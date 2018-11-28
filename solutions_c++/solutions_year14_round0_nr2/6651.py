#include<iostream>
#include<iomanip>
#include<algorithm>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<set>
using namespace std;
int main()
{
    int T;
    cin >> T;
    double X, F,C, FT, R,minT;
    for(int t = 1; t <= T; t++)
    {
        cin >> C >> F >> X;
        R =2;
        FT = 0;
        minT = X/R;
        while(true)
        {
            FT += C/R;
            R += F;
            if(minT > FT +  X/R)
                minT = FT + X/R;
            else
                break;
        }
        cout << "Case #" << t << ": " << fixed << setprecision(8) << minT << endl;
    }
    return 0;
}
