#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int getNumCases(){
    int a;
    cin >> a;
    return a;
}

bool isHappy(char c){
    return c=='+';
}

bool isBlank(char c){
    return c=='-';
}

int countHappyGroups(string s){
    int i=0, n=0;
    while(i<s.length()){
        if(isHappy(s.at(i))){
            ++n;
            ++i;
            while(i < s.length() && isHappy(s.at(i)))
                ++i;
        }
        else
            ++i;
    }
    return n;
}

int countBlankGroups(string s){
    int i=0, n=0;
    while(i<s.length()){
        if(isBlank(s.at(i))){
            ++n;
            ++i;
            while(i < s.length() && isBlank(s.at(i)))
                ++i;
        }
        else
            ++i;
    }
    return n;
}

int minManeuvers(string s){
    if(s.size()==0) return 0;

    unsigned long lb= s.find_last_of('-');
    if(lb == string::npos) return 0;

    s = s.substr(0, lb+1);
    int ch = countHappyGroups(s);
    int cb = countBlankGroups(s);
    if(ch >= cb)
        return 2*cb;
    else
        return 1+2*ch;
}

void enumerateCases(vector<string> v){
    for(unsigned long i=0; i<v.size(); ++i){
        string s = v.at(i);
        int t = minManeuvers(s);
        cout << "Case #" << i+1 << ": " << t << endl;
    }
}

vector<string> generateInputVector(){
    int n = getNumCases();
    vector<string> v;
    for(int i=0; i<n; ++i){
        string s;
        cin >> s;
        v.push_back(s);
    }
    return v;
}

void stdinPancakes(){
    enumerateCases(generateInputVector());
}

int main() {
    stdinPancakes();
    //enumerateCases(vector<string>{"+--+--+", "+--+--"});
    return 0;
}