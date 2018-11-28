#include <iostream>
#include <set>

using namespace std;

void splitDigit(int i, set<int>& s){
    while (i){
        s.insert(i%10);
        i/=10;
    }
}

int main() {

    int nTest;

    cin >> nTest;

    for(size_t i = 0; i < nTest; ++i){
        set<int> set1;

        unsigned short us;
        cin >> us;
        int k = 0;
        while (true) {
            if(us == 0) {
                cout << "Case #" << i+1 << ": INSOMNIA" << endl;
                break;
            }
            splitDigit(++k * us, set1);
            if (set1.size() == 10) {
                cout << "Case #" << i+1 << ": " <<  k * us << endl;
                break;
            }
        }
    }

    return 0;
}

