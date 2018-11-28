#include<iostream>
#include<unordered_map>
#include<string>
#include<vector>

using namespace std;

unordered_map<char, int> genMap(string s){
    unordered_map<char, int> ret; 
    for(int x = 0; x < s.length(); ++x){
        if(ret.find(s[x]) != ret.end()){
            ++(ret.find(s[x])->second);
        }
        pair<char,int> p(s[x], 1);
        ret.insert(p);
    }
    return ret;
}

bool checkFit(unordered_map<char,int> map, string s){
    for(int x = 0; x < s.length(); ++x){
        if(map.find(s[x]) == map.end() || map.find(s[x])->second <= 0){
            return false; 
        }
        --(map.find(s[x])->second);
    }
    return true;
}

void removeWord(unordered_map<char, int>& map, string s){
    for(int x = 0; x < s.length(); ++x){
        --(map.find(s[x])->second); 
    }
}

void printVec(vector<string> good){
    vector<int> vec;
    for(int x = 0; x < good.size(); ++x){
        if(good[x] == "ZERO"){
            vec.push_back(0);
        } 
        else if(good[x] == "ONE"){
            vec.push_back(1);
        } 
        else if(good[x] == "TWO"){
            vec.push_back(2);
        }
        else if(good[x] == "THREE"){
            vec.push_back(3);
        }
        else if(good[x] == "FOUR"){
            vec.push_back(4);
        } 
        else if(good[x] == "FIVE"){
            vec.push_back(5);
        }
        else if(good[x] == "SIX"){
            vec.push_back(6);
        }
        else if(good[x] == "SEVEN"){
            vec.push_back(7);
        }
        else if(good[x] == "EIGHT"){
            vec.push_back(8);
        } 
        else if(good[x] == "NINE"){
            vec.push_back(9);
        }
    }
    sort(vec.begin(), vec.end());
    for(int x = 0; x < vec.size(); ++x){
        cout << vec[x]; 
    }
}

void exec(){
     // vector<string> vec = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
    vector<string> vec = {"ZERO","FOUR","SIX","EIGHT","TWO","ONE","THREE","SEVEN","FIVE","NINE"};
    int junk;
    cin >> junk;
    string line;
    int caseNum = 1;
    while(cin >> line){
        if(caseNum > 1){
            cout << endl; 
        }
        vector<string> goodNums;
        unordered_map<char, int> map = genMap(line);
        for(int x = 0; x < vec.size(); ++x){
            while(checkFit(map, vec[x])){
                removeWord(map, vec[x]);
                goodNums.push_back(vec[x]);
            } 
        }
        cout << "Case #" << caseNum << ": ";
        printVec(goodNums);
        ++caseNum;
    }
}

int main(){
    exec();
}
