#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

bool checkRow(const vector<int> &x, int val)
{
    bool flag = true;
    for(vector<int>::const_iterator i = x.begin(); i != x.end(); ++i)
    {
        flag &= *i == val;
    }

    return flag;
}

bool checkColumn(const vector<vector<int> > &x, int i, int val)
{
    size_t n = x.size();
    size_t m = x[0].size();
    bool flag = true;
    for(size_t j = 0; j < n; ++j)
    {
        flag &= x[j][i] == val;
    }

    return flag;
}

int mymin(const vector<vector<int> > &x)
{
    int mymin = 9999999;
    for(vector<vector<int> >::const_iterator i = x.begin();
        i != x.end(); ++i)
    {
        mymin = min(mymin, *min_element(i->begin(), i->end()));
    }
    return mymin;
}

int mymax(const vector<vector<int> > &x)
{
    int mymax = -9999999;
    for(vector<vector<int> >::const_iterator i = x.begin();
        i != x.end(); ++i)
    {
        mymax = max(mymax, *max_element(i->begin(), i->end()));
    }
    return mymax;
}

string CheckPattern(vector<vector<int> > x)
{
    size_t n = x.size();
    size_t m = x[0].size();
    int _min = mymin(x);
    int old_min = _min - 1;
    int _max = mymax(x);
    for (; _min != _max && old_min < _min ;)
    {
        vector<vector<int> > copyx = x;
        //check rows
        for(size_t i = 0; i < n; ++i)
        {
            if (checkRow(x[i], _min))
            {
                copyx[i].assign(m, _min + 1);
            }
        }
        //check columns
        for(size_t i = 0; i < m; ++i)
        {
            if (checkColumn(x, i, _min))
            {
                for (int j = 0; j < n; ++j)
                {
                    copyx[j][i] = _min + 1;
                }
            }
        }


        old_min = _min;
        x = copyx;
        _min = mymin(x);
        _max = mymax(x);
    }
    return (_min == _max) ? "YES" : "NO";
}

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt", ios_base::out | ios_base::trunc);
    size_t T;
    in >> T;
    for (size_t i = 0; i < T; ++i)
    {
        size_t n, m;
        in >> n;
        in >> m;
        vector<vector<int> > x(n);
        for (int k = 0; k < n; ++k)
        {
            x[k].resize(m);
            for (int l = 0; l < m; ++l)
            {
                in >> x[k][l];
            }
        }
        out << "Case #" << i + 1 << ": " << CheckPattern(x) << "\n";
    }

    return 0;
}

