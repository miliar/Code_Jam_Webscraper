#include <iostream>
#include <fstream>

#include <vector>
#include <map>
#include <set>

using namespace std;

int main(int argc, char const *argv[])
{
    ifstream ifs(argv[1]);
    ofstream ofs("result");
    int ncases;
    ifs >> ncases;

    for (int casenum = 1; casenum < ncases+1; ++casenum)
    {
        int height;
        int width;
        ifs >> height;
        ifs >> width;
        cout << width << endl;
        cout << height << endl;
        vector<vector<int> > mawn = vector<vector<int> >(height, vector<int>(width));
        for (int y = 0; y < height; y++)
        {
            for (int x = 0; x < width; x++)
            {
                ifs >> mawn.at(y).at(x);
            }
        }

//        for (int i = 0; i < mawn.size(); i++)
//        {
//            for (int j = 0; j < mawn[i].size(); j++)
//            {
//                cout << mawn[i][j];
//            }
//            cout << endl;
//        }

        bool possible = true;
        for (int y = 0; y < height && possible; y++)
        {
            for (int x = 0; x < width && possible; x++)
            {
                // check if this position can be generated
                bool a1 = false;
                bool a2 = false;
                for (int y1= 0; y1 < height; y1++)
                {
                    if (mawn[y1][x] > mawn[y][x]) a1 = true;
                }

                for (int x1= 0; x1 < width; x1++)
                {
                    if (mawn[y][x1] > mawn[y][x]) a2 = true;
                }
                if (a2 && a1) possible = false;
            }
        }

        ofs << "Case #" << casenum << ": ";
        if (possible)
        {
            ofs << "YES" << endl;
        } else {
            ofs << "NO" << endl;
        }
    }

    return 0;
}
