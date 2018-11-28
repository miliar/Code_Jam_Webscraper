#include <iostream>
#include <string>

using namespace std;

void SolveCase(int case_n)
{
    int s_max;
    string levels;

    int total_people = 0;
    int extra_people = 0;

    cin >> s_max >> levels;
    for (int i = 0; i < s_max + 1; ++i) {
        int shy_i = levels[i] - '0';

        if (total_people >= i) { // no more people necessary
            total_people += shy_i;
        } else { // need more people
            int extra = i - total_people;
            extra_people += extra;
            total_people += (extra + shy_i);
        }
    }

    cout << "Case #" << case_n << ": " << extra_people << std::endl;
}

int main()
{
    int t;
    cin >> t;

    for (int c = 0; c < t; ++c) {
        SolveCase(c + 1);
    }

    return 0;
}