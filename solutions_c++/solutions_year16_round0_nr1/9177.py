#include <iostream>
#include <string>
#include <cstdint>
using namespace std;

void solve_case(int num_case)
{
    cout << "Case #" << num_case+1 << ": ";
    uint64_t n;
    cin >> n;

    if(n == 0) {
        cout << "INSOMNIA" << endl;
        return;
    }

    bool digit_seen[10] = {false};
    int num_digit_seen = 0;
    uint64_t mul = 0;
    while(num_digit_seen != 10) {
        ++mul;
        auto n_str = to_string(mul*n);
        for(char c : n_str) {
            if(!digit_seen[c-'0']) {
                digit_seen[c-'0'] = true;
                ++num_digit_seen;
            }
        }
    }
    cout << n*mul << endl;
}

int main()
{
    int num_case;
    cin >> num_case;

    for(int i=0;i!=num_case;++i) {
        solve_case(i);
    }
    return 0;
}
