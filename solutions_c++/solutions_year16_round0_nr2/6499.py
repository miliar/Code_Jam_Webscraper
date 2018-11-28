#include <bits/stdc++.h>
#include <fstream>

using namespace std;

int main()
{
    ifstream fe ("B-large.in");
    ofstream fs ("resp2.out");
    int t;
    fe>>t;
    for (int q = 1; q <= t; q++)
    {
        string cad;
        fe>>cad;
        int con = 0;
        bool vec [cad.length()];
        for (int w = 0; w < cad.length(); w++)
        {
            if (cad[w] == '+')
            {
                vec[w] = true;
            }
            else
            {
                vec[w] = false;
            }
        }
        int pos = 0;
        bool aux = false;
        while (pos < cad.length())
        {
            aux = false;
            for (int w = pos; w < cad.length(); w++)
            {
                if (vec[w] != vec[0])
                {
                    pos = w;
                    w = cad.length();
                    aux = true;
                }
            }
            if (!aux)
            {
                pos = cad.length();
            }
            else
            {
                for (int w = 0; w < pos; w++)
                {
                    vec[w] = !vec[w];
                }
            }
            con++;
        }
        if (vec[0])
        {
            fs<<"Case #"<<q<<": "<<con-1<<endl;
        }
        else
        {
            fs<<"Case #"<<q<<": "<<con<<endl;
        }
    }
    return 0;
}
