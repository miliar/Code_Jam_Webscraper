#include <fstream>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
#include <vector>

using namespace std;

int main(int argc, char** argv)
{
    ifstream is(argv[1]);
    size_t nbCases;
    is >> nbCases;

    for (size_t c(1); c != nbCases+1; ++c)
    {
        int answer1, answer2;
        int field1[4][4], field2[4][4];

        is >> answer1;
        for (size_t r(0); r != 4; ++r) {
            is >> field1[r][0] >> field1[r][1] >> field1[r][2] >> field1[r][3];
        }

        is >> answer2;
        for (size_t r(0); r != 4; ++r) {
            is >> field2[r][0] >> field2[r][1] >> field2[r][2] >> field2[r][3];
        }

        set<int> set1{field1[answer1-1][0],field1[answer1-1][1],field1[answer1-1][2],field1[answer1-1][3]};
        set<int> set2{field2[answer2-1][0],field2[answer2-1][1],field2[answer2-1][2],field2[answer2-1][3]};

        set<int> result;
        set_intersection(set1.begin(),set1.end(),set2.begin(),set2.end(),std::inserter(result,result.begin()));

        if (result.size() == 1) cout << "Case #" << c << ": " << *result.begin() << endl;
        else if (result.size() > 1) cout << "Case #" << c << ": Bad magician!" << endl;
        else cout << "Case #" << c << ": Volunteer cheated!" << endl;
    }
}

