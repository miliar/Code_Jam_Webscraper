#include <iostream>
using namespace std;

int calcNum(string order){
    int len = order.length();
    char cur ='+';
    int cnt = 0;
    for(int i = len-1; i >= 0; i--  ){
        if(order.at(i) != cur){
            cur = order.at(i);
            cnt++;
        }
        
    }
    return cnt;
        
    
}


int main() {
    int testCase;
    cin >> testCase;
    for(int i =0 ; i< testCase; i++){
        string pancake;
        cin >> pancake;
        int res = calcNum(pancake);
        printf("Case #%d: %d\n",i+1,res);
    }
}