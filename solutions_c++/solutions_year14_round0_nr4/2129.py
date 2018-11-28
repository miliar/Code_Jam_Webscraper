#include <algorithm>
#include <fstream>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <list>
#include <queue>
#include <stack>
#include <string>
#include <vector>

using namespace std;

ifstream fin("data.txt");
ofstream fout("output.txt");

double a[1001], b[1001];

void run_once()
{
    int n;
    fin >> n;

    for (int i = 0; i < n; ++i)
        fin >> a[i];

    for (int i = 0; i < n; ++i)
        fin >> b[i];

    sort(a, a+n);
    sort(b, b+n);

    int dw = 0;

    for (int i = 0, j = 0; i < n && j < n; )
    {
        if (a[i] > b[j])
        {
            ++i, ++j, ++dw;
        }
        else
        {
            ++i;
        }
    }

    int w = n;
    for (int i = n-1, j = n-1; i >= 0 && j >= 0;)
    {
        if  (a[i] < b[j])
        {
            --i, --j;
            --w;
        }
        else
        {
            --i;
        }
    }

    fout << dw << " " << w << endl;
}

int main()
{
    int case_count;
    fin >> case_count;

    for (int case_id = 1; case_id <= case_count; ++case_id)
    {
        fout << "Case #" << case_id << ": ";
        run_once();
    }

    return 0;
}