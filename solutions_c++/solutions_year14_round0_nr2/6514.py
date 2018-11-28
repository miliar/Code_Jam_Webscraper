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

#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    fstream in("input.txt");
    fstream out("output.txt");
    int n;
    in >> n;
    for (int i= 0; i < n; ++i)
    {
        double C,F,X;
        in >> C >> F >> X;
        double prev = 0;
        double mn = X*1./2;
        for (int j = 1; j < 200001; ++j)
        {
            prev=prev + C*1./ (F * (j - 1) + 2);
            mn = min(mn, prev + X * 1./(F * j + 2));
        }
        out.precision(9);
        out<< fixed << "Case #" << i+1 <<": "<< mn << endl;
    }
}




