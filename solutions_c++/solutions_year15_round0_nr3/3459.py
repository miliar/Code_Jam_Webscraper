#include <iostream>
#include <vector>
#include <algorithm>
#include <set>
#include <string>
#include <map>
#include <fstream>
using namespace std;
vector<vector<int> > ops = {{0, 0, 0, 0, 0}, {0, 1, 2, 3, 4}, {0, 2, -1, 4, -3}, {0, 3, -4, -1, 2}, {0, 4, 3, -2, -1}};
int mult(int l, int r)
{
    int sign = 1;
    if (l < 0)
    {
        sign *= -1;
        l = -l;
    }
    if (r < 0)
    {
        sign *= -1;
        r = -r;
    }
    return ops[l][r] * sign;
}
int my_pow(int num, int pow)
{
    if (pow == 1)
        return num;
    if (pow % 2 == 0)
    {
        int res = my_pow(num, pow / 2);
        return mult(res, res);
    }
    return mult(my_pow(num, pow - 1), num);
}
int main()
{
    ifstream cin ("/Programming/Sources/cf_c/cf_c/input.txt");
    ofstream cout ("/Programming/Sources/cf_c/cf_c/output.txt");
    
    int i, j, n, m, k, t;
    
   /* for(j = 1; j < 5; j++)
    {
        for (i = 1; i < 5; i++)
            cout << ops[j][i] << ' ';
        cout << endl;
    }*/
    cin >> t;
    for (int curtest = 1; curtest < t + 1; ++curtest)
    {
        int l, x;
        
        cin >> l >> x;
        string s;
        
        cin >> s;
        vector<int> f;
        for (j = 0; j < s.size(); j++)
        {
            if (s[j] == 'i')
            {
                f.push_back(2);
            }
            if (s[j] == 'j')
            {
                f.push_back(3);
            }
            if (s[j] == 'k')
            {
                f.push_back(4);
            }
        }
        for (j = 0; j < x - 1; j++)
        {
            for(i = 0; i < l; i++)
            {
                f.push_back(f[i]);
            }
        }
        if (l * x < 3)
        {
                cout << "Case #" << curtest<< ": NO"  << endl;
            continue;
        }
        int res = f[0];
        int good = 0;
        for (j = 1; j < f.size(); j++)
        {
            if (res == 2)
            {
                --j;
                good++;
                break;
            }
            res = mult(res, f[j]);
            if (res == 2)
            {
                good++;
                break;
            }
        }
      //  cout << ' ' << j << ' ';
        if (j + 1 < f.size())
        {
            res = f[j + 1];
            ++j;
            ++j;
        }
        for (; j < f.size(); j++)
        {
            if (res == 3)
            {
                --j;
                good++;
                break;
            }
            res = mult(res, f[j]);
            if (res == 3)
            {
                good++;
                break;
            }
        }
      //  cout << ' ' << j << ' ';
        if (j + 1 < f.size())
        {
            res = f[j + 1];
            ++j;
            ++j;
        }
        for (; j < f.size(); j++)
        {
            res = mult(res, f[j]);
            
        }
      //  cout << ' ' << j << ' ';
        if (res == 4)
            ++good;
        if (good == 3)
        {
            cout << "Case #" << curtest<< ": YES"  << endl;
        }
        else
        {
            cout << "Case #" << curtest<< ": NO"  << endl;
        }
        continue;
        int sign = 1;
        if (res < 0)
        {
            if (x % 2 != 0)
                sign = -1;
            res = -res;
        }
        res = my_pow(res, x);
        res *= sign;
        if (res == -1)
        {
            cout << "Case #" << curtest<< ": YES"  << endl;
        }
        else
        {
            cout << "Case #" << curtest<< ": NO"  << endl;
        }
        //cout << "Case #" << curtest<< ": " << ans << endl;
    }
}