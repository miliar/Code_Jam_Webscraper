#include <bitset>
#include <iostream>
#include <map>
#include <string>

using namespace std;

void solve(int testnum)
{
    bitset<1000> pancakes;

    string pancakes_init;
    int width;

    cin >> pancakes_init >> width;

    int num_pancakes = pancakes_init.length();

    for (int i = 0; i < num_pancakes; i++) {
        pancakes.set(i, pancakes_init[i] == '-');
    }

    int index = 0;
    int moves = 0;
    while (pancakes.any() && index <= num_pancakes - width) {
        if (pancakes[index]) {
            for (int i = 0; i < width; i++) {
                pancakes.flip(index + i);
            }
            ++moves;
        }
        ++index;
    }
    cout << "Case #" << testnum << ": ";
    if (pancakes.none()) {
        cout << moves;
    } else {
        cout << "IMPOSSIBLE";
    }
    cout << endl;
}

int main()
{
    int num_tests;

    cin >> num_tests;

    for (int i = 1; i <= num_tests; i++) {
        solve(i);
    }
}