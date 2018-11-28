#include <iostream>
#include <map>
using namespace std;

int main(){
    unsigned long long T, N;
    cin >> T;


    for (int i = 0; i < T; i++){
        map<int, bool> seen;
        int currMultiple = 0;
        cin >> N;
        while(seen.size() < 10 && currMultiple < 100000){
            currMultiple++;
            unsigned long long curr = N * currMultiple;
            while (curr != 0){
                seen[curr % 10] = true;
                curr /= 10;
            }
        }
        cout << "Case #" << i + 1 << ": ";
        if (currMultiple == 100000){
            cout << "INSOMNIA" << endl;
        } else {
            cout << currMultiple * N << endl;
        }
    }
}
