#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <set>
#include <utility>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <fstream>
#include <iomanip>

using namespace std;

int main()
{
    ifstream cin("entrada.in");
    ofstream cout("salida.txt");
    int T, n;
    double C,X, t=0, F;

    cin >> T;

    for(int i=1; i<=T; i++){
        cin >> C >> F >> X;
        t = 0;
        n=(F*X-2*C-F*C)/(F*C) +1;
        for(int j=0; j<n; j++){
            t += C/(2 + j*F);
        }
        t += X/(2 + n*F);

        double caso0 = X/2;
        if(caso0 < t) t = caso0;

        cout << "Case #" << i << ": ";
        cout << fixed;
        cout << setprecision(7) << t << endl;
    }
    return 0;
}
