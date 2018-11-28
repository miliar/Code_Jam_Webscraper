#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <vector>
#include <sstream>


using namespace std;

bool string_less (string first, string second)
{
    if (first.size() < second.size())
        return true;
    if (first == second)
        return true;
    if (first.size() > second.size())
        return false;

    else
    {
        for (int i = 0; i < first.size(); i++)
        {
            if (first[i] < second[i])
                return true;
        }
    }
    return false;
}


void s_square(vector<int> & numv, vector<int> &res)
{
    vector<int> a = numv;
    vector<int> b = numv;
    b.reserve(b.size());
    a.reserve(a.size());


    int i, j, k;
    int tmp;

    for (i = 0; i < a.size(); i++)
    {
        k = i;
        for (j = 0; j < b.size(); j++)
        {
            res[k++] += a[i]*b[j];
        }
    }

    for (k  = res.size() -1; k >= 0; k--)
    {
        if (res[k] > 9 )
        {
            if (k != 0)
            {
                res[k-1] += res[k] /10;
                res[k] %= 10;
            }
            else
            {
                tmp = res[k]/10;
                res[k]%=10;
                res.insert(res.begin(), tmp);
            }
        }
    }
}



bool check_p(string input)
{
    for(int i = 0; i < input.size()/2; i++)
    {
        if (input[i] != input[input.size() -1 -i])
            return false;
    }
    return true;
}


int solve (string& low, string& high)
{
    long int i = 1;
    int count = 0;
    while (1)
    {
        stringstream ss;
        ss << i;
        string num = ss.str();
        if (!check_p(num))
        {
            i++;
            continue;
        }

        vector <int> numv (num.begin(), num.end());
        for (int j = 0; j < numv.size(); j++)
            numv[j] -= '0';

        vector <int> res (numv.size() *2 -1, 0);
        s_square (numv, res);
        string s_res ;
        for (int j = 0; j < res.size(); j++)
        {
            s_res += (res[j] +'0');
        }

        cout << num << " square is " << s_res << endl;

        int ilow, is, ih;
        istringstream ress (s_res);
        istringstream lows (low);
        lows >> ilow;
        istringstream higs (high);
        higs >> ih;
        ress >> is;
        if (is < ilow)
        {
            i ++;

            cout << is << "less than" << low <<endl;
            continue;
        }

        if (is <= ih)
        {
            cout << "less than high" << endl;
        }
        else
            return count;

        if (check_p(s_res))
            count ++;
        i ++;
    }
    return count;
}



int main()
{
    ifstream f1 ("input");
    ofstream f2 ("output");


    int cases;
    f1 >> cases;

    for (int i = 0; i < cases; i++)
    {
        string low, high;
        f1 >> low >> high;
        int s = solve (low, high);
        f2 << "Case #" << i + 1 << ": ";
        f2 << s << endl;
    }
}

