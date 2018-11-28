#include <iostream>
#include <set>
#include <sstream>
#include <vector>

using namespace std;

int getNumCases(){
    int a;
    cin >> a;
    return a;
}

string intToString(long long t){
    ostringstream oss;
    oss << t;
    return oss.str();
}

long long getLastBeforeSleeping(long long t){
    if(t == 0){
        return -1;
    }
    set<int> intset{'0','1','2','3','4','5','6','7','8','9'};
    int i=0;
    while(!intset.empty()){
        ++i;
        for(char c: intToString(i*t)){
            intset.erase(c);
        }
    }
    return i*t;
}

void enumerateCases(vector<int> v){
    for(int i=0; i<v.size(); ++i){
        long long t = (long long)v.at(i);
        t = getLastBeforeSleeping(t);
        cout << "Case #" << i+1 << ": ";
        if(t == -1){
            cout << "INSOMNIA";
        }
        else {
            cout << t;
        }
        cout << endl;
    }
}

vector<int> generateInputVector(){
    int n = getNumCases();
    vector<int> v;
    for(int i=0; i<n; ++i){
        int t;
        cin >> t;
        v.push_back(t);
    }
    return v;
}

void stdinSheep(){
    enumerateCases(generateInputVector());
}

vector<int> generateLoopVector(int n){
    vector<int> v;
    for(int i=0; i<=n; ++i){
        v.push_back(i);
    }
    return v;
}

void loopSheep(int n){
    enumerateCases(generateLoopVector(n));
}

int main() {
    stdinSheep();
    //loopSheep(1000000);
    return 0;
}