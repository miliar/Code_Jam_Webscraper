/**
 * file: sheep.cpp
 * @author: Yangmu Jiang
 * @mail: celsius.j@gmail.com
 * @created time: Apr 08 2016
 */

#include <iostream>
#include <algorithm>
using namespace std;

string count(int N) {
    if (N == 0)
        return "INSOMNIA";

    bool digits[10];
    int i = 1;
    string Nx;

    fill_n(digits, 10, false);
    while (true) {
        Nx = to_string(N * i);
        ++i;
        for (unsigned char c : Nx)
            digits[c - '0'] = true;
        if (find(begin(digits), end(digits), false) == end(digits))
            break;
    }
    return Nx;
}
    
int main(int argc, char **argv)
{
    int test = 0;
    int N;
    cin >> test;
    for (int i = 1; i <= test; ++i) {
        cin >> N;
        cout << "Case #" << i << ": " << count(N) << endl;
    }
    return 0;
}

