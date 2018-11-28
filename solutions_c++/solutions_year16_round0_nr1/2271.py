#include <iostream>
#include <cstring>
using namespace std;

typedef long long ll;

#include <fstream>
int main()
{
    //ifstream cin("in.txt");
    //ofstream cout("out.txt");

    int T;
    cin >> T;

    for (int i = 1; i <= T; i++)
    {
        ll N;
        cin >> N;
        cout << "Case #" << i<<": ";

        if ( N == 0) { cout << "INSOMNIA" << endl; continue;}


        bool c[11];
        memset(c, false, 11);
        
        ll m = 0;
        int s = 0;
        while (s < 10)
        {
            m += N;
            ll x = m;

            while (x) {c[x%10] = true; x /= 10;}

            s = 0;
            for (int j = 0; j < 10; j++) 
                if (c[j] == true) s++;
        }
        cout << m << endl;

    }
    return 0;
}