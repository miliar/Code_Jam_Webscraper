#include <bits/stdc++.h>
using namespace std;
typedef long long int ll;
const int INF = 1000000000;
#define REP(i,s,n) for(int i=(int)(s);i<(int)(n);i++)
#define rep(i,n) REP(i, 0, n)
int main(){
    ifstream ifs("A-large.in");
    ofstream ofs("op_a.txt");
    int test; ifs >> test;
    string zero = "ZERO", one = "ONE", two = "TWO", three = "THREE", four = "FOUR", five = "FIVE", six = "SIX", seven = "SEVEN", eight = "EIGHT", nine = "NINE";
    string pre = "GVSXFEZRONTWHUI";
    rep(casenum, test){
        string s; ifs >> s;
        map<char, int> nums;
        for(char a : pre) nums[a] = 0;
        for(char a : s) nums[a]++;
        vector<int> ans;
        while(nums['G']){
            for(char a : eight) nums[a]--;
            ans.push_back(8);
        }
        while(nums['X']){
            for(char a : six) nums[a]--;
            ans.push_back(6);
        }
        while(nums['S']){
            for(char a : seven) nums[a]--;
            ans.push_back(7);
        }
        while(nums['V']){
            for(char a : five) nums[a]--;
            ans.push_back(5);
        }
        while(nums['F']){
            for(char a : four) nums[a]--;
            ans.push_back(4);
        }
        while(nums['Z']){
            for(char a : zero) nums[a]--;
            ans.push_back(0);
        }
        while(nums['R']){
            for(char a : three) nums[a]--;
            ans.push_back(3);
        }
        while(nums['W']){
            for(char a : two) nums[a]--;
            ans.push_back(2);
        }
        while(nums['O']){
            for(char a : one) nums[a]--;
            ans.push_back(1);
        }
        while(nums['I']){
            for(char a : nine) nums[a]--;
            ans.push_back(9);
        }
        sort(ans.begin(), ans.end());
        ofs << "Case #" << casenum + 1
            << ": " ;
        for(int k : ans) ofs << k;
        ofs << endl;
    }
    return 0;
}