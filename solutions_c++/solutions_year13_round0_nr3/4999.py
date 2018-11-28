#include <iostream>
#include <string>
#include <set>
#include <cmath>

using namespace std;


set<string> numbers;

int upperLimit = 1000;
int practicalLimit = sqrt(upperLimit);

void fillNumbers(string &s, int x) {
    //testNumber(s);

    if (s[x] != '9') {
        string s2 = s;
        s2[x]+=1;

        fillNumbers(s2, x);
    }

    if (x > 0) {
        fillNumbers(s, x-1);
    }
}

int main()
{
    int n;
    cin >> n;




    /* First, calc everything */
    int squares [5] = {1,4,9,121,484};

    for (int Case = 0; Case < n; Case++) {
        int min, max;

        cin >> min >> max;

        int total = 0;

        for (int i = 0; i < 5; i++) {
            if (squares[i] >= min && squares[i] <= max) {
                total += 1;
            }
        }

        cout << "Case #" << (Case+1) << ": " << total << endl;
    }

    return 0;
}

