#include <iostream>

using namespace std;

void count_num(int n)
{
    if (n == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }

    // for n is not zero
    bool seen[10] = {false};
    int curr_n = n;
    for (;;) {
        // record current digits
        for (int tmp = curr_n; tmp > 0; tmp /= 10) {
            int digit = tmp % 10;
            seen[digit] = true;
        }

        // check whether all seen
        int flag = false;
        for (int i = 0; i < 10; ++i) {
            if (!seen[i]) {
                flag = true;
            }
        }
        if (flag) {
            // adjust n and enter next loop
            curr_n += n;
            continue;
        }

        // all seen!!!
        cout << curr_n << endl;
        return;
    }
}

int main(void)
{
    int times;
    cin >> times;

    int seq = 1;
    while (times-- > 0) {
        int n;
        cin >> n;
        cout << "Case #" << seq << ": ";
        count_num(n);

        seq++;
    }
    return 0;
}
