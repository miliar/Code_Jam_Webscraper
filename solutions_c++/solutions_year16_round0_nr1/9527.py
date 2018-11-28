#include<iostream>
#include<unordered_set>
using namespace std;

void insertTable(long long i, unordered_set<int>& table){
    if(table.size() >= 10){
        return;}
    if(i <= 0){
        return; 
    }
    int val = i % 10;
    table.insert(val);
    insertTable(i/10, table);
}

long foo(long i, unordered_set<int>& table, int curr){
    insertTable(i*curr, table);
    if(table.size() >= 10){
        return i;}
    ++curr;
    return foo(i, table, curr);
}

long driver(long i){
    unordered_set<int> table;
    int curr = 1;
    return foo(i, table, curr);
}

void m(){
    int gar;
    cin >> gar;
    long long val;
    int curr = 1;;
    while(cin >> val){
        if(val == 0){
            cout << "Case #" << curr << ": INSOMNIA\n";
        }  else {
            unordered_set<int> table;
            long long curVal;
            int counter = 1;
            while(table.size() != 10){
                curVal = val * counter; 
                insertTable(curVal, table); 
                ++counter;
            }
            cout << "Case #" << curr << ": " << curVal << endl;
        }
        ++curr;
    }
}

int main(){
    // unordered_set<int> table;
    // insertTable(123456789, table);
    m();
}
