#include <stdio.h>
#include<iostream>
#include<cmath>
#include<vector>
#include<set>
#include<algorithm>
#include <fstream>
#include <iomanip>
#include <limits>
using namespace std;

double C,X,F;

int main()
{
    ofstream cout ("B-large.out");
    ifstream cin ("B-large.in");
    int T;
    double ratio=2.0,s,sum,newS;
    cin >> T;
    for( int i = 1; i <= T; i++){
        cin >> C >> F >> X;
        sum = 0;
        ratio=2.0;
        s = X/ratio;
        while (true){
            sum += C/ratio;
            ratio+=F;
            newS = sum + X/ratio;
            if(newS>=s)
                break;
            else
                s = newS;
        }
        sum+= X/ratio;
        cout << "Case #"<< i <<": ";
        cout << fixed << setprecision(7) << s << "\n";
    }
    return 0;
}
