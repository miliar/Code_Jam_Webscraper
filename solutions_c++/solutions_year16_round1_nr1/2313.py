#include <iostream>
#include <unordered_map>
#include <fstream>
#include <string>
#include <utility>
#include <vector>
#include <sstream>
#include <cmath>
#include <climits>
#include <algorithm>
#include <queue>

using namespace std;

#pragma loop(hint_parallel(8))

class Solution
{
public:
    static void getinput(string filename, int& n, vector<string>& ss)
    {
        string line;
        ifstream inFile(filename);

        if(inFile.is_open())
        {
            //first line is # of test cases
            getline(inFile, line);
            n = stoi(line);

            for(int i=0; i< n; i++)
            {
                getline(inFile, line);
                ss.push_back(line);
            }
        }
    }

    static void lastword(string s, string& out)
    {
        if(s.empty()) return;

        auto vec = vector<string>();
        auto res = "";
        auto q = queue<string>();
        for(auto& c : s)
        {
            auto ch = string(1,c);
            if(q.empty()){
                q.push(ch);
                continue;
            }
            else
                helper(ch, q);
        }
        auto size = q.size();
        for(auto i=0; i < size; i++)
        {
            auto str = q.front();
            vec.push_back(str);
            q.pop();
            //cout << str << endl;
        }

        sort(vec.begin(), vec.end());
        out = vec[size-1];

    }

    static void helper(string ch, queue<string>& res)
    {
        if(res.empty()) return;

        auto len = res.size();
        for (int i = 0; i < len; ++i)
        {
            auto tmp = res.front();
            res.push( tmp +  ch);
            res.push( ch + tmp);
            res.pop();
        }

    }
};

int main(int argc, char const *argv[])
{
    int numofcases = 0;
    auto ss = vector<string>();
    Solution::getinput("A-small-attempt0.in", numofcases, ss);
    int counter = 1;
    for(auto& s : ss)
    {
        string temp = "";
        Solution::lastword(s, temp);
        cout << "Case #" << counter<< ": "<< temp << endl;
        counter++;
    }
    return 0;
}