#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

unordered_map<char,string> map1,map2;
unordered_map<char,int> counts;
unordered_map<string,int> nums;


int initMap(){
    map1['Z'] = "ZERO";
    map1['W'] = "TWO";
    map1['U'] = "FOUR";
    map1['X'] = "SIX";
    map1['G'] = "EIGHT";

    map2['O'] = "ONE";
    map2['T'] = "THREE";
    map2['F'] = "FIVE";
    map2['S'] = "SEVEN";

    nums["ZERO"] = 0;
    nums["ONE"] = 1;
    nums["TWO"] = 2;
    nums["THREE"] = 3;
    nums["FOUR"] = 4;
    nums["FIVE"] = 5;
    nums["SIX"] = 6;
    nums["SEVEN"] = 7;
    nums["EIGHT"] = 8;
    nums["NINE"] = 9;
}

void clearMap(){
    counts.clear();
}

int solve(string& instr,vector<int>& result){
    clearMap();
    initMap();
    for(auto c:instr){
        counts[c] ++;
    }

    for(auto c:instr){
        if(map1.count(c)){
            string &s = map1[c];
            for(auto cc:s){
                counts[cc] --;
            }
            result.push_back(nums[s]);
        }
    }
    for(auto c:instr){
        if(map2.count(c) && counts[c] > 0){
            string &s = map2[c];
            for(auto cc:s){
                counts[cc] --;
            }
            result.push_back(nums[s]);
        }
    }
    for(auto c:instr){
        if(counts[c] > 0){
            string s = "NINE";
            for(auto cc:s){
                counts[cc] --;
            }
            result.push_back(nums[s]);
        }
    }
    sort(result.begin(),result.end());
}

int main()
{
    int t;
    cin>>t;
    int line = 1;
    while(t--){
        string s;
        cin>>s;
        cout<<"Case #"<<line<<": ";
        vector<int> result;
        solve(s,result);
        for(auto ele:result)
            cout<<ele;
        cout<<endl;
        line ++;
    }
    return 0;
}
