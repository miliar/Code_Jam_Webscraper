#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;


typedef long double ld;


bool ispal(string str)
{
    for (int i = 0, j = str.length()-1; i < j; i++,j--)
        if (str[i] != str[j])
            return false;
    return true;
}


bool ispal(ld val)
{
    ostringstream o;
    o << val;
    string str = o.str();
    return ispal(str);
}


string increment(string num)
{
    ld val;
    istringstream i(num);
    i >> val;
    val += 1.0;
    ostringstream o;
    o << val;
    return o.str();
}


bool nextpal(ld& curr, ld maxv, bool doincrement)
{
    ostringstream o;
    o << curr;
    string str = o.str();

    if (doincrement)
    {
        // Increment the middle digit.
        if (str.length() % 2)   // if length is odd
        {
            string half1 = str.substr(0, str.length()/2+1);
            string half2 = str.substr(0, str.length()/2);
            half1 = increment(half1);
            half2 = string(half2.rbegin(), half2.rend());    // reverses half2
            str = half1 + half2;
        }
        else
        {
            string half1 = str.substr(0, str.length()/2);
            string half2 = str.substr(0, str.length()/2);
            half1 = increment(half1);
            half2 = string(half2.rbegin(), half2.rend());    // reverses half2
            str = half1 + half2;
        }
    }

    // Make a palindrome.
    if (str.length() % 2)   // if length is odd
    {
        string half1 = str.substr(0, str.length()/2+1);
        string half2 = str.substr(0, str.length()/2);
        half2 = string(half2.rbegin(), half2.rend());
        str = half1 + half2;
    }
    else
    {
        string half1 = str.substr(0, str.length()/2);
        string half2 = str.substr(0, str.length()/2);
        half2 = string(half2.rbegin(), half2.rend());
        str = half1 + half2;
    }

    //cout << curr << endl;

    istringstream i(str);
    i >> curr;

    //cout << curr << endl << endl;

    return curr <= maxv;
}


bool issqrpal(ld curr)
{
    curr = curr * curr;
    ostringstream o;
    o << curr;
    return ispal(o.str());
}


void solve()
{
    ld ll, rr;
    cin >> ll >> rr;

    //cout << endl << ll << "  " << rr << endl;

    ld l = ceil(sqrt(ll));
    ld r = floor(sqrt(rr));

    ld curr = l;
    int count = 0;
    if (nextpal(curr, r, false) && issqrpal(curr))
    {
        if (curr >= l && curr <= r)
        {
            //cout << curr << endl;
            count++;
            assert(curr * curr >= ll);
            assert(curr * curr <= rr);
            assert(ispal(curr));
        }
    }
    while (nextpal(curr, r, true))
    {
        if (issqrpal(curr))
        {
            if (curr >= l && curr <= r)
            {
                //cout << curr << endl;
                count++;
                assert(curr * curr >= ll);
                assert(curr * curr <= rr);
                assert(ispal(curr));
            }
        }
    }

    cout << count << endl;
    //cout << endl;
}


int main()
{
    int T;
    cin >> T;

    for (int caseNum = 1; caseNum <= T; caseNum++)
    {
        cout << "Case #" << caseNum << ": ";
        solve();
    }

    return 0;
}
