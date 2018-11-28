#include <iostream>
#include <fstream>
#include <set>
#include <algorithm>
#include <iterator>

using namespace std;

const size_t size = 4;
set <int> grid1 [size];
set <int> grid2 [size];
ifstream fin ("D:\\DOWNLOADS\\A-small-attempt0.in");

void readGridData (int iter = 1)
{
    int temp;
    for (size_t j = 0; j < size; ++j)
    {
        for (size_t k = 0; k < size; ++k)
        {
            fin >> temp;
            ((1 == iter) ? grid1[j] : grid2[j]).insert(temp);
        }
    }
}

int main ()
{
    ofstream cout ("D:\\outASMALL.txt");

    int t;
    fin >> t;
    for (int i = 0; i < t; ++i)
    {
        int a, b;
        fin >> a;
        readGridData();
        fin >> b;
        readGridData(2);
        cout << "Case #" << i+1 << ": ";
        set <int> intersection;
        set_intersection(grid1[a-1].begin(), grid1[a-1].end(),
                grid2[b-1].begin(), grid2[b-1].end(), inserter(intersection, intersection.begin()));
        if (intersection.size() == 1)
            cout << *intersection.begin() << endl;
        else if (intersection.size() == 0)
            cout << "Volunteer cheated!" << endl;
        else
            cout << "Bad magician!" << endl;

        for (size_t j = 0; j < size; ++j)
        {
            grid1[j].clear();
            grid2[j].clear();
        }

    }
}
