// Author: Bony Roopchandani

#include <bits/stdc++.h>
using namespace std;

void clearGlobals(void) {}

void flip(string& Stack, int left, int right) {
    while(left <= right) {
        char L = Stack[left], R = Stack[right];
        Stack[left] = (R=='+'?'-':'+');
        Stack[right] = (L=='+'?'-':'+');
        left++; right--;
    }
}

void solve(void) {
    string Stack;
    cin>>Stack;
    long long res = 0;
    for(int i = Stack.length() - 1; i >= 0; i--) {
        if(Stack[i] == '-') {
            if(Stack[0] == '-') {
                flip(Stack, 0, i);
            }
            else {
                int index = 0;
                while(index < Stack.length() and Stack[index] == '+') {
                    Stack[index++] = '-';
                }
                res += 1;
                flip(Stack, 0, i);
            }
            res += 1;
        }
    }
    cout<<res<<'\n';
    clearGlobals();
}

int main(void) {
    ios_base::sync_with_stdio(false);
    int testCase;
    cin>>testCase;
    for(int tc=1; tc<=testCase; tc++) {
        cout<<"Case #"<<tc<<": "; solve();
    }
    return (EXIT_SUCCESS);
}
