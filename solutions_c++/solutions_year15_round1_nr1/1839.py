#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;

int main()
{
    ifstream in("in.txt");
    ofstream out("out.txt");

    int t;
    in >> t;

    for(int test = 0; test < t; ++test)
    {
        int n;
        in >> n;

        vector<int> m;

        int y = 0;
        int z = 0;
        int last = 0;
        int minRate = 0;

        for(int j = 0; j < n; ++j)
        {
            int tmp;
            in >> tmp;
            m.push_back(tmp);

            if(last > tmp)
            {
                y += last - tmp;
                minRate = max(minRate, last - tmp);
            }

            last = tmp;
        }

        for(int i = 1; i < n; ++i)
        {
            z += min(m[i-1], minRate);
        }

        out << "Case #" << test + 1 << ": " << y << " " << z << endl;
    }

    return 0;
}

