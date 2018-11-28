#include<iostream>
#include<bitset>

using namespace std;

int main(int argc, char **argv) {

    size_t TEST_CASES;
    cin >> TEST_CASES;

    uint64_t N;

    for (size_t i = 1; i <= TEST_CASES; ++i) {
        cin >> N;

        if(N == 0){
            cout << "Case #" << i << ": INSOMNIA\n";
            continue;
        }

        bitset<10> knownDigits;
        for(uint64_t mult = 1; ; ++mult){
            uint64_t currNumber = N * mult;

            do{
                knownDigits.set(currNumber % 10);
                currNumber /= 10;
            }while(currNumber > 0);

            if(knownDigits.all()){
                cout << "Case #" << i << ": " << (N*mult) << "\n";
                break;
            }
        }
    }
}