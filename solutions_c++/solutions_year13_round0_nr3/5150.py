#include <stdint.h>
#include <iostream>

using namespace std;

int main()
{
    size_t n;
    uint64_t num[] = {
                        1,
                        4,
                        9,
                        121,
                        484,
                        10201,
                        12321,
                        14641,
                        40804,
                        44944,
                        1002001,
                        1234321,
                        4008004,
                        100020001,
                        102030201,
                        104060401,
                        121242121,
                        123454321,
                        125686521,
                        400080004,
                        404090404,
                        10000200001,
                        10221412201,
                        12102420121,
                        12345654321,
                        40000800004,
                        1000002000001,
                        1002003002001,
                        1004006004001,
                        1020304030201,
                        1022325232201,
                        1024348434201,
                        1210024200121,
                        1212225222121,
                        1214428244121,
                        1232346432321,
                        1234567654321,
                        4000008000004,
                        4004009004004,
                    };

    freopen("C-large-1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    cin >> n;
    for(size_t i = 0; i < n; ++i) {
        uint64_t left;
        uint64_t right;
        int x = 0;
        int y = 0;
        int res = 0;
        cin >> left >> right;
        if(right < num[0] || left > num[38]) {
            cout << "Case #" << i+1 << ": 0" << std::endl;
            continue;
        }

        for(size_t j = 0; j < 39; ++j) {
            if(left <= num[j]) {
                if(left == num[j]) {
                    ++res;
                    x = j;
                }
                else
                    x = j - 1;
                break;
            }
        }
        for(size_t j = 38; j > 0; --j) {
            if(right >= num[j]) {
                y = j;
                break;
            }
        }

        cout << "Case #" << i+1 << ": ";
        cout << y-x+res << std::endl;
    }

    return 0;
}
