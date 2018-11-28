#include <fstream>
#include <set>
#include <iostream>
using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    int n, t;
    in >> t;
    for(int i = 1; i <= t; ++i){
        set<int> numbers_seen;
        in >> n;
        if (n == 0)
            out << "Case #" << i << ": INSOMNIA\n";
        else{
            int multiplier = 1, tmp = 0;
            while(numbers_seen.size() != 10){
                tmp = multiplier * n;
                ++multiplier;
                while(tmp != 0){
                    numbers_seen.insert(tmp % 10);
                    tmp /= 10;
                }
            }
            out << "Case #" << i << ": " << (multiplier - 1) * n << '\n';
        }
    }
}
