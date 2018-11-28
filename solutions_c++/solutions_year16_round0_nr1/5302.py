#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

typedef long long ll;

ll counter;

void markNumbers(ll current, bool number[]) {
    string curr = to_string(current);
    int i = 0, len = curr.length();
    while(i < len) {
        int wtf = curr[i]-'0';
        if(number[wtf] == false) {
            number[wtf] = true;
            counter++;
        }
        i++;
    }
}

bool allNumbersDone(bool number[]) {
    return (counter == 10);
}

int main() {
    ll T, N, i, j, k, A[100000];

    cin >> T;
    ll t = 1;
    while(t <= T) {
        cin >> N;

        bool number[10];
        for(i=0;i<10;i++) {
            number[i] = false;
        }
        
        if(N == 0) {
            cout << "Case #" << t << ": " << "INSOMNIA" << endl;
            t++;
            continue;
        }

        counter = 0;
        j = 2;
        ll current = N;
        markNumbers(current, number);
        while(!allNumbersDone(number)) {
            current = N*j;
            markNumbers(current, number);
            j++;
        }
        cout << "Case #" << t << ": " << current << endl;
        t++;
    }

    return 0;
}