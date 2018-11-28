#include<iostream>
#include<vector>
#include<algorithm>
#include<stdlib.h>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;

class Case{
    int n; string s;
public:
    Case(int nn, string ss = string()) :
        n(nn), s(ss)
    {
    }

    friend ostream& operator<<(ostream& out, Case& c)
    {
        return out << "Case #" << c.n << ": " << c.s ;
    }
};

int main()
{
    ifstream cin("B-large.in");
    ofstream cout("a.out");

    int n; 
    double c, f, x;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        cin >> c >> f >> x;
        double max = x/2.0, sum  = max;
        int z = 0;
        while (1){
            sum += (c-x) / (2.0 + z*f);
            z++;
            sum += x / (2.0 + z*f);
            if (sum < max)
            {
                max = sum;
            }
            else
            {
                cout << Case(i, "") << fixed << setprecision(7) << max << endl;
                break;
            }
        }



    }
    

   // system("PAUSE");

}