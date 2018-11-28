#include<iostream>
#include<list>
#include<stdio.h>

using namespace std;

string A;
list<char> li;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output1-large.out", "w", stdout);
    int t;
    cin >> t;
    for (int i = 1;i<=t;i++) {
        cin >> A;
        int len = A.length();
        //while (li.empty() != 1) li.pop_back();
        li.push_back(A[0]);
        for (int j=1;j<len;j++) {
            if (li.front()>A[j]) li.push_back(A[j]);
            else li.push_front(A[j]);
        }
        cout << "Case #" << i << ": ";
        while (li.empty() != 1) {
            cout << li.front();
            li.pop_front();
        }
        cout << endl;
    }
    return 0;
}
