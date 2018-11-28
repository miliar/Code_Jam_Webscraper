#include <iostream>
#include <fstream>
#include <set>

using namespace std;

int main()
{
    ifstream in("input.txt");
    ofstream out("output.txt");

    set<int> numbers;

    int T;
    long N, tempN;

    in >> T;

    for(int i = 0; i < T; i++) {
        in >> N;

        if(N == 0) {
            out << "Case #" << i+1 << ": INSOMNIA\n";
            continue;
        }

        tempN = N;
        int k = 2;

        while(true) {
            while(tempN != 0) {
                numbers.insert(tempN % 10);
                tempN /= 10;
            }

            if(numbers.size() != 10) {
                tempN = k * N;
                k++;
            } else {
                tempN = (k-1) * N;
                break;
            }
        }

        numbers.clear();
        out << "Case #" << i+1 << ": " << tempN << "\n";
    }

    return 0;
}
