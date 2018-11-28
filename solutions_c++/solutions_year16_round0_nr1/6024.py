#include <iostream>
#include <unordered_set>

using namespace std;

long long int countSleep(int num) {
    unordered_set<int> units( {0,1,2,3,4,5,6,7,8,9} );
    long long int result = 0, temp;
    int unit;
    while (!units.empty()) {
        result += num;
        temp = result;
        while (temp) {
            unit = temp % 10;
            if (units.find(unit) != units.end())
                units.erase(unit);
            temp /= 10;
        }
    }
    return result;
}

int main(){
    int T, num, id = 1;
    cin >> T;
    while (T--) {
        cout << "Case #" << id << ": ";
        cin >> num;
		id++;
        if (num == 0)
            cout << "INSOMNIA" << endl;
        else
            cout << countSleep(num) << endl;
    }
    
    return 0;
}