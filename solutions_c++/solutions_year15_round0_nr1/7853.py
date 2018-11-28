/*************************************************************************
    > File Name: Standing Ovation.cpp
    > Author: Archer Liu
    > Mail: maple.km2041@me.com 
    > Created Time: Sat Apr 11 16:07:21 2015
 ************************************************************************/

#include <fstream>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    int solve(string str) {
        int len = str.size();
        int ans = 0;
        int sum = 0;
        for(int i=0; i<len; ++i) {
            if(sum < i) {
                ans += i - sum;
                sum = i;
            } 
            sum += str[i] - '0'; 
        }

        return ans;
    }
};

int main(int argc, char** argv) {
    fstream in("/Users/Archer/Desktop/dat.txt");
    fstream out("/Users/Archer/Desktop/output.txt");
    cin.rdbuf(in.rdbuf());
    cout.rdbuf(out.rdbuf());

    int cases;
    cin >> cases;
    Solution sol;
    for(int i=1; i<cases+1; ++i) {
        int m;
        cin >> m;
        string s1;
        cin >> s1;
        int ans = sol.solve(s1);
        printf("Case #%d: %d\n", i, ans);
    }

    return 0;
}
