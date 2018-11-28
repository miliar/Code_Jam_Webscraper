#include <iostream>
#include <string>
#include <iterator>
using namespace std;


void solve_case(int num_case)
{
    string cakes;
    cin >> cakes;

    int num_flips = 0;
    size_t i=cakes.length()-1;
    for(; i<cakes.length(); --i) {
        if(cakes[i] == '-') {
            ++num_flips;
            break;
        }
    }

    char last_char = '-';
    for(; i<cakes.length(); --i) {
        if(cakes[i] != last_char) {
            ++num_flips;
            last_char = cakes[i];
        }
    }

    cout << "Case #" << num_case+1 << ": " << num_flips << endl;
}

int main()
{
    int num_cases;
    cin >> num_cases;

    for(int i=0; i!=num_cases; ++i) {
        solve_case(i);
    }
    return 0;
}
