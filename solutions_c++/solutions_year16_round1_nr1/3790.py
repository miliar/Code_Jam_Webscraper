#include <iostream>
#include <list>

using namespace std;

int main() {
    int nCases;
    cin >> nCases;
    while(getchar() != '\n');
    for(int i = 1; i <= nCases; i++) {
        char c = getchar();
        list<char> list1;
        list1.push_back(c);
        while((c = getchar()) != '\n') {
            if(c <= *list1.rbegin()) {
                if(c > *list1.begin() && abs(c - *list1.begin() > abs(c - *list1.rbegin())))
                    list1.insert(list1.begin(), c);
                else
                    list1.push_back(c);
            }
            else if(c >= *list1.begin()) {
                list1.insert(list1.begin(), c);
            }
            else
                list1.push_back(c);

        }
        cout << "Case #" << i << ": ";
        for(auto it = list1.begin(); it != list1.end(); it++)
            cout << *it;
        cout << endl;
    }

    return 0;
}