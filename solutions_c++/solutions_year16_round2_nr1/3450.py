#include <iostream>
#include <unordered_map>
#include <limits>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

string numbers[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
vector<int> finalSol;
int getNum(string &s)
{
    if (s == "NINE")
        return 9;
    else if (s == "EIGHT")
        return 8;
    else if (s == "SEVEN")
        return 7;
    else if (s == "SIX")
        return 6;
    else if (s == "FIVE")
        return 5;
    else if (s == "FOUR")
        return 4;
    else if (s == "THREE")
        return 3;
    else if (s == "TWO")
        return 2;
    else if (s == "ONE")
        return 1;
    else
        return 0;
}

bool getSol(int index, unordered_map<char, int> h)
{
    vector<int> sol;
    int i;
    int minimum = numeric_limits<int>::max();
    int maximum = numeric_limits<int>::min();
    for (i = 0; i < numbers[index].size(); i++)
    {
        minimum = min(minimum, h[numbers[index][i]]);
        maximum = max(maximum, h[numbers[index][i]]);
    }
    if (numbers[index] == "SEVEN" || numbers[index] == "THREE")
    {
        if (minimum == 0 || maximum < 2)
            return false;
    }
    else
    {
        if (minimum < 1)
            return false;
    }

    for (i = 0; i < numbers[index].size(); i++)
        h[numbers[index][i]]--;
    sol.push_back(getNum(numbers[index]));

    bool done = false, found = true, noOp = true;
    while (!done)
    {
        noOp = true;
        for (index = 0; index < 10; index++)
        {
            minimum = numeric_limits<int>::max();
            maximum = numeric_limits<int>::min();
            for (i = 0; i < numbers[index].size(); i++)
            {
                minimum = min(minimum, h[numbers[index][i]]);
                maximum = max(maximum, h[numbers[index][i]]);
            }
            if (numbers[index] == "SEVEN" || numbers[index] == "THREE")
            {
                if (minimum == 0 || maximum < 2)
                    continue;
            }
            else
            {
                if (minimum < 1)
                    continue;
            }

            for (i = 0; i < numbers[index].size(); i++)
                h[numbers[index][i]]--;
            sol.push_back(getNum(numbers[index]));
            noOp = false;
        }
        found = true;
        for (auto it = h.begin(); it != h.end(); it++)
            if (it->second != 0)
                found = false;
        if (noOp)
            done = true;
        if (found)
        {
            for (i = 0; i < sol.size(); i++)
                finalSol.push_back(sol[i]);
            done = true;
        }
    }


    return found;
}

int main()
{
    string S;
    int T, minimum, k, j, i;
    ifstream f("input.in");
    ofstream g("output.out");
    f >> T;
    for (i = 0; i < T; i++)
    {
        f >> S;
        unordered_map<char, int> h;
        for (j = 0; j < S.size(); j++)
            h[S[j]]++;

        g << "Case #" << i + 1 << ": ";
        for (j = 0; j < 10; j++)
        {
            minimum = numeric_limits<int>::max();
            for (k = 0; k < numbers[j].size(); k++)
                minimum = min(minimum, h[numbers[j][k]]);
            if (minimum > 2)
            {
                for (k = 0; k < numbers[j].size(); k++)
                    h[numbers[j][k]] -= minimum - 2;
                for (k = 0; k < minimum - 2; k++)
                    finalSol.push_back(getNum(numbers[j]));
            }
        }

        for (j = 0; j < 10; j++)
            if (getSol(j, h))
                break;
        sort(finalSol.begin(), finalSol.end());
        for (j = 0; j < finalSol.size(); j++)
            g << finalSol[j];
        g << '\n';
        finalSol.clear();
    }
    f.close();
    g.close();
    return 0;
}
