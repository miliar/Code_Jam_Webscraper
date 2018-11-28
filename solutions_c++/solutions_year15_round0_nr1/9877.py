#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");
    string tempIn;
    size_t ans(0), count(0);
    vector<size_t> peopleList;
    vector<string> inputVector;

    while ( getline(in, tempIn) )
    {
        inputVector.push_back(tempIn);
    }

    for (size_t i = 1; i < inputVector.size(); ++i)
    {
        ans = count = 0;
        peopleList.clear();
        for (size_t j = 2; j < inputVector[i].size(); ++j)
            peopleList.push_back(inputVector[i][j]-'0');

        for (size_t j = 0; j < peopleList.size(); ++j)
        {
            if (j > count && peopleList[j] != 0)
            {
                ans += (j-count);
                count += ans;
            }
            count += peopleList[j];
        }
        out << "Case #" << i << ": " << ans << endl;
    }
    return 0;
}

