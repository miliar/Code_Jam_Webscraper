#include <iostream>
#include <map>
#include <vector>

using namespace std;

bool done(vector<bool> &numbers_seen) {
    bool d = true;

    for (int i = 0; i < 10; ++i) {
        d &= numbers_seen[i];
    }

    return d;
}

void count(vector<bool> &numbers_seen, int64_t number) {
    while (number > 0) {
        int rem = number % 10;

//        cout << "Saw number " << rem << endl;

        numbers_seen[rem] = true;

        number /= 10;
    }
}



int64_t doit() {
    int n;

    cin >> n;

//    cout << n << endl;

    if (n <= 0) {
        return -1;
    }

    vector<bool> numbers_seen(10, false);
    int64_t counter = n;

    do {
        count(numbers_seen, counter);

        counter += n;
    } while (!done(numbers_seen));


    return counter - n;
}

int main() {
    int test_cases;

    cin >> test_cases;

    for (int i = 0; i < test_cases; ++i) {
        int64_t res = doit();

        if (res < 0) {
            printf("Case #%d: INSOMNIA\n", i+1);
        } else {
            printf("Case #%d: %lld\n", i+1, res);
        }
    }

    return 0;
}