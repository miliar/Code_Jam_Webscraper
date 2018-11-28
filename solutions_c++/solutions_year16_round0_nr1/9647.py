#include <iostream>
#include <string>
#include <set>
#include <boost/multiprecision/cpp_int.hpp>

using namespace std;
using namespace boost::multiprecision;

int main() {

    int cases;
    cin >> cases;

    
    for (int casei = 0; casei < cases; casei++) {

        int counted = 0;
        set<int> seen;

        string snumber;
        cin >> snumber;
        cpp_int original_number(snumber);

            
        if (snumber == "0") {
            cout << "Case #" << casei+1 << ": " << "INSOMNIA" << endl;
        } else {
            
            for(int i = 1; seen.size() != 10; i++) {
                cpp_int current_number = original_number * cpp_int(i);
                snumber = current_number.str();
                for (int i = 0; i < snumber.size(); i++) {
                    seen.insert(snumber[i]);
                }

            }
            cout << "Case #" << casei+1 << ": " << snumber << endl;
        }

    }

}
