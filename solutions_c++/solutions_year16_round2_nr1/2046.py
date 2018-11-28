#include <iostream>
#include <set>
#include <algorithm>

using namespace std;

string solve(string& s)
{
    multiset<char> counter;

    string result;

    int n6(0),n5(0),n8(0),n7(0),n9(0);

    for (char c : s)
    {
        counter.insert(c);
    }

    for (int i=0; i < counter.count('Z'); ++i)
    {
        result += '0';
    }

    for (int i=0; i < counter.count('W'); ++i)
    {
        result += '2';
    }


    for (int i=0; i < counter.count('X'); ++i)
    {
        result += '6';
        ++n6;
    }

    for (int i=0; i < counter.count('G'); ++i)
    {
        result += '8';
        ++n8;
    }

    for (int i=0; i < counter.count('S') - n6; ++i)
    {
        result += '7';
        ++n7;
    }

        for (int i=0; i < counter.count('V')-n7; ++i)
    {
        result += '5';
        ++n5;
    }


    for (int i=0; i < counter.count('F') - n5; ++i)
    {
        result += '4';
    }

    for (int i=0; i < counter.count('H') - n8; ++i)
    {
        result += '3';
    }

    for (int i=0; i < counter.count('I') - n8-n6-n5; ++i)
    {
        result += '9';
        ++n9;
    }

    for (int i=0; i < counter.count('N') - n7-2*n9; ++i)
    {
        result += '1';
    }

    sort(result.begin(), result.end());

    return result;
}

int main()
{
    int n_cases;
    cin >> n_cases;

    for (int cno=0; cno < n_cases; cno++)
    {
        string s;
        cin >> s;
        cout << "Case #" << cno+1 << ": " << solve(s) << "\n";
    }
}