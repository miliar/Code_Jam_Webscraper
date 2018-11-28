/*
 ID: jonnyko1
 PROG: barn1
 LANG: C++11
*/

#include <algorithm>
#include <stack>
#include <unordered_map>
#include <limits.h>
#include <time.h>
#include <queue>
#include <set>
#include <time.h>
#include <iostream>
#include <vector>
#include <string>
#include <fstream>
#include <math.h>
#include <iomanip>
#include <numeric>
#include <array>
#include <utility>
#include <ctime>

using namespace std;

#define RELEASE 1

bool mySort(const pair<int, char> & a, const pair<int, char> & b){
    return a.first > b.first;
}

int main(){
#if RELEASE
    freopen("/Users/jonnykong/Downloads/A-large.in.txt", "r", stdin);
    freopen("/Users/jonnykong/Desktop/outPut.txt", "w", stdout);
#endif
    int t; cin >> t;
    for(int z = 0; z < t; ++z){
        int n; cin >> n;
        int total = 0;
        vector<pair<int, char>> nums(n);
        for(int i = 0; i < n; ++i){
            cin >> nums[i].first;
            total += nums[i].first;
            nums[i].second = i + 'A';
        }
        cout << "Case #" << z + 1 << ':' << ' ';
        for(int i = 0; i < total / 2 - 1; ++i){
            sort(nums.begin(), nums.end(), mySort);
            cout << nums[0].second << nums[1].second << ' ';
            --nums[0].first; --nums[1].first;
        }
        sort(nums.begin(), nums.end(), mySort);
        if(total % 2){
            cout << nums[0].second << ' ';
            --nums[0].first;
            sort(nums.begin(), nums.end(), mySort);
            cout << nums[0].second << nums[1].second;
        }
        else{
            cout << nums[0].second << nums[1].second;
        }
        cout << endl;
    }
}