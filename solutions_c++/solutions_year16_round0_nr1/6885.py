#include <iostream>
#include <set>

using namespace std;

void insert(long n, set<int> &nums)
{
    while(n > 0) {
        nums.insert(n % 10);
        n /= 10;
    }
}

int main()
{
    int T;

    cin >> T;

    for(int t=1; t<=T; t++) {
        long n;
        set<int> nums;

        cin >> n;
        if (n == 0) {
            cout << "Case #" << t << ": INSOMNIA" << endl;
        } else {
            int i = 2;
            long newn = n;
            while(true) {
                insert(newn, nums);
                if (nums.size() >= 10) {
                    cout << "Case #" << t << ": " << newn << endl;
                    break;
                } else {
                    newn = n * i;
                    i++;
                }
            }
        }
    }

    return 0;
}
