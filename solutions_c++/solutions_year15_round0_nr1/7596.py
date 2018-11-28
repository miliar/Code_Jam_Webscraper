#pragma once

#include <string>
#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

class StandingOvation
{
public:
    void solve(const string& file)
    {
        ifstream input(file);
        ofstream out("a.out");

        int Ntests;
        input >> Ntests;

        for (int i = 0; i < Ntests; ++i)
        {
            vector<int> s;
            int maxShyness;
            string shyness;
            input >> maxShyness >> shyness;

            for (int j = 0; j < maxShyness+1; ++j)
                s.push_back(stoi(shyness.substr(j, 1)));

            out << "Case #" << i+1 << ": " << calcAdditionalFriends(s) << endl;
        }
        out.close();
    }

    int calcAdditionalFriends(const vector<int>& shyness)
    {
        int sum = 0;
        int add = 0;
        for (int i = 0; i < shyness.size(); ++i)
        {
            if (sum < i)
            {
                add += i - sum;
                sum += i - sum;
            }
            sum += shyness[i];
        }

        return add;
    }
};

int main()
{
    StandingOvation problem;
    problem.solve("A-large.in");
    return 0;
}
