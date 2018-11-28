#include <ctime>
#include <cstdlib>
#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <algorithm>
//Containers
#include <string>
#include <bitset>
#include <vector>
#include <deque>
#include <list>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <unordered_map>
#include <unordered_set>


using namespace std;


int countingSheep(int N) {
    unordered_set<int> digit;
    int i = 1;
    while(1) {
        int tmp = N * i;
        while(tmp > 0) {
            if(!digit.count(tmp % 10)) digit.insert(tmp % 10);
            tmp /= 10;
            if(10 == digit.size())
                return N * i;
        }
        ++i;
    }
    return 0;
}

int main (int argc, const char * argv[])
{
    //    Solution sol;
    ifstream in("");
    ofstream out("/Users/Xiangyu/Desktop/Gitfold/Test-Programming-Languages/CPP/CPP/output.txt");
    if (!in.is_open() || !out.is_open()) {
        cout << "Error opening file" << endl;
        exit (1);
    }
    int i = 0;
    int a;
    while(in >> a) {
        if(0 != i)
        {
            if(0 == a)
                out << "Case #" << i << ": INSOMNIA" << endl;
            else
                out << "Case #" << i << ": " << countingSheep(a) <<endl;
        }
        ++i;
    }
    in.close();
    out.close();
    return 0;
}