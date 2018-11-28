#include <iostream>
#include <stdio.h>
#include <string>

using namespace std;

int sortPancake(string pancake) {
    int rounds = 0;
    if (pancake.length()==1) {
        if (pancake.at(0) == '-'){
            rounds++;
        }
    } else {
        for (int i=1; i<pancake.length(); i++) {
            if (pancake.at(i-1) == pancake.at(i)) {
                if (i == pancake.length()-1 && pancake.at(i) == '-') {
                    rounds++;
                }
            } else {
                rounds++;
                if (i == pancake.length()-1 && pancake.at(i) == '-') {
                    rounds++;
                    for (int x=0; x<pancake.length(); x++) {
                    }
                }
            }
        }
    }

    return rounds;
}

int main() {
    freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);

    int testcase;
    scanf("%d", &testcase);
    int result [testcase];
    string pancakes [testcase];
    for (int i=0; i<testcase; i++) {
        cin >> pancakes[i];
        result[i] = sortPancake(pancakes[i]);
    }

    for (int j=0; j<testcase; j++) {
        cout << "Case #" << j+1 << ": ";
        cout << result[j] << endl;
    }

    return 0;
}
