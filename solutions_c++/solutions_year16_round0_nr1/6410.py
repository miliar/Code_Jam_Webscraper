#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int main()
{
    ifstream fe ("A-large.in");
    ofstream fs ("resp2.out");
    int t;
    long int n;
    fe>>t;
    for (int q = 1; q <= t; q++)
    {
        fe>>n;
        bool vec[10];
        memset (vec, false, sizeof(vec));
        int con = 0;
        long int i = 1;
        if (n!=0)
        {
            while (con < 10)
            {
                long long int igual = n * i;
                while (igual > 0)
                {
                    if (!vec[igual%10])
                    {
                        vec[igual%10] = true;
                        con ++;
                    }
                    igual /= 10;
                }
                i++;
            }
            fs << "Case #"<<q<<": "<<n*(i-1)<<endl;
        }
        else
        {
            fs << "Case #"<<q<<": INSOMNIA"<<endl;
        }
    }
    return 0;
}
