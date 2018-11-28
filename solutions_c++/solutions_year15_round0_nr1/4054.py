#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
using namespace std;

int N;
int S;
string digits;
int invitations;

void solve() {
    int audienceSize = 0;
    for (int i = 0; i < digits.size(); i++) {
        int digit = digits[i] - '0';
        if (audienceSize < i) {
            int newInvitations = i - audienceSize;
            audienceSize += newInvitations;
            invitations += newInvitations;
        }
        audienceSize += digit;
    }
}

void clean() {
    invitations = 0;
}

void read() {
    cin >> S;
    cin >> digits;
}

void print() {
    cout << invitations;
}

int main() {
    int n;
    scanf("%d", &n);
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');

    for (int i = 1; i <= n; i++) {
        clean();
        read();
        solve();

        printf("Case #%d: ", i);
        print();
        printf("\n");
    }

    return 0;
}

