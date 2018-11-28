#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <list>
#include <algorithm>
#include <stack>
#include <functional>
#include <fstream>
#include <deque>
#include <queue>

using namespace std;

int main() 
{
    fstream in("input.txt");
    fstream out("output.txt");
    int n;
    in >> n;
    for(int I = 1; I <= n; ++I)
    {
        int b[5][5];
        int a[5][5];
        int k, l;
        in >> k;
        for(int i = 1; i <= 4; ++i)
            for(int j = 1; j <= 4; ++j)
                in >> a[i][j];
        in >> l;
        for(int i = 1; i <= 4; ++i)
            for(int j = 1; j <= 4; ++j)
                in >> b[i][j];

        set<int>A;
        set<int>B;
        for(int i = 1; i <= 4; ++i)
            A.insert(a[k][i]);
        for(int i = 1; i <= 4; ++i)
            B.insert(b[l][i]);
        auto iter1 = A.begin();
        auto iter2 = B.begin();
        int counter = 0;
        int answer = 0;
        for(iter1 = A.begin(); iter1 != A.end(); ++iter1)
            if(B.find(*iter1) != B.end())
            {
                counter++;
                answer = *iter1;
            }
        out << "Case #" << I << ": ";
        if(counter == 0)
            out << "Volunteer cheated!";
        if(counter == 1)
            out << answer;
        if(counter > 1)
            out << "Bad magician!";
        out << endl;
    }



    return 0;
}




