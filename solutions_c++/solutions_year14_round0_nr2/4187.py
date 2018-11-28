#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    char buffer[128];
    int T;
    cin >> T;
    for(int k=1; k<=T; k++)
    {
        double C,F,X;
        cin >> C >> F >> X;
        double r = 2.0, t = 0.0;
        while(true)
        {
            double t1 = X/r;
            double t2 = C/r+X/(r+F);
            if(t1<=t2)
            {
                t += t1;
                break;
            }
            else
            {
                t += C/r;
                r += F;
            }
        }
        sprintf(buffer, "%.7f", t);
        cout << "Case #" << k << ": " << buffer << endl;
    }
    return 0;
}
