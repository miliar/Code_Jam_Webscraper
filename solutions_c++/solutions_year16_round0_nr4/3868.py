
#include <iostream>
using namespace std;

int main() {
    int numTests;
    
    int k;
    int c;
    int s;
    
    cin >> numTests;
    cin.ignore(10000, '\n');
    
    for (int i = 1; i <= numTests; i++)
    {
        cin >> k >> c >> s;
        cout << "Case #" << i << ":";
        
        for (int i = 1; i <= k; i++)
            cout << " " << i;
        cout << endl;
    }
}

