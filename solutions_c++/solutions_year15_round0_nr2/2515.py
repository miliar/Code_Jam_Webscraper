#include <iostream>
#include <fstream>
#include <cassert>
#include <cctype>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> eat(vector<int> &diner)
{
    vector<int> rlt{};
    for(auto i=diner.begin();i!=diner.end();++i)
    {
        int temp = *i - 1;
        if(temp!=0) rlt.push_back(temp);
    }
    return rlt;
}

vector<int> split(vector<int> diner, int j)
{
    auto i = max_element(diner.begin(),diner.end());
    int temp = *i;
    *i = j;
    diner.push_back(temp-j);
    return diner;
}

int solve(vector<int> diner)
{
    if(diner.empty()) return 0;
    else{
        auto i = max_element(diner.begin(),diner.end());
        if(*i==1) return 1;
        vector<int> rlt{};
        int one = solve(eat(diner));
        rlt.push_back(one);

       for(auto j=2;j<=(*i)/2;++j)
            {
                rlt.push_back(solve(split(diner,j)));
            }
        return 1 + *min_element(rlt.begin(),rlt.end());
    }
}



int main()
{
    fstream in,out;
    in.open("small.in",fstream::in);
    out.open("small2.out",fstream::out|fstream::app);
    int num;
    in >> num;
    for(int i = 0;i != num; ++i)
    {
        int d = 0;
        in >> d;
        vector<int> diner{};
        for(int j = 0; j != d; ++j)
        {
            int temp;
            in >> temp;
            diner.push_back(temp);
        }
        out << "Case #" << i+1 << ": " << solve(diner) <<endl;

    }
    return 0;
}
