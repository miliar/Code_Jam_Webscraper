#include <iostream>
using namespace std;

int main() {
    int cases;
    cin >> cases;

    for (int x = 0; x < cases; ++x) {
        int shyness;
        cin >> shyness;

        int total_stand = 0, need_to_invite = 0;
        for (int i = 0; i <= shyness; ++i) {
            char people;
            cin >> people;

            int number_of_people = people - '0';
            if (total_stand < i) {
                need_to_invite += i - total_stand;
                total_stand = i;
            }
            total_stand += number_of_people;
        }
        cout << "Case #" << x + 1 << ": " << need_to_invite << endl;
    }
}