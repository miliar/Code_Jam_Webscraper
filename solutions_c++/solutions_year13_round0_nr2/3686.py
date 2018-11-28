#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    ifstream input("B-large.in");
    int t;
    input >> t;
    int n, m;
    ofstream output("B-large.out");
    bool a, b, c;
    for (int i=0; i<t; i++)
    {
        input >> n >> m;
        int garden[n][m];
        for (int y=0; y<n; y++)
        {
            for (int z=0; z<m; z++)
            {
                input >> garden[y][z];
            }
        }
        c=false;
        for (int y=0; y<n; y++)
        {
            for (int z=0; z<m; z++)
            {
                a=false;
                b=false;
                for (int k=0; k<n; k++)
                {
                    if (garden[k][z]>garden[y][z])
                    {
                        a=true;
                    }
                }
                for (int k=0; k<m; k++)
                {
                    if (garden[y][k]>garden[y][z])
                    {
                        b=true;
                    }
                }
                if ((b == true) && (a == true))
                {
                    c=true;
                }
            }
        }
        if (c==true)
        {
            output << "Case #" << i+1 << ": NO" << endl;
        }
        else
        {
            output << "Case #" << i+1 << ": YES" << endl;
        }
    }
    input.close();
    output.close();
    return 0;
}
