#include <iostream>
#include <list>
void war(int);
using namespace std;

int main ()
{
    int testcases;
    cin >> testcases;
    int i;
    for (i = 1; i <= testcases; i++){
        war(i);
    }
    return 0;
}

void war(int i)
{
    std::list<long double> Naomi;
    std::list<long double> Ken;
    long double weightN;
    long double weightK;
    int noOfBlocks;
    cin >> noOfBlocks;
    for (int j = 1;j <= noOfBlocks; j++) {
        cin >> weightN;
        Naomi.push_front (weightN);
    }
    for (int j = 1;j <= noOfBlocks; j++) {
        cin >> weightK;
        Ken.push_front (weightK);
    }
    Naomi.sort();
    Ken.sort();
    Naomi.reverse();
    Ken.reverse();
    int fair_count = 0;
    int deceitful_count = 0;
    // fair play
    std::list<long double>::iterator itN=Naomi.begin();
    std::list<long double>::iterator itK=Ken.begin();
    while (itN != Naomi.end()) {
        if (*itN > *itK) {
            itN++;
            fair_count++;
        } else {
            break;
        }
    }
    while (itN != Naomi.end() && itK != Ken.end()) {
        if (*itN < *itK) {
            itK++;
            itN++;
        } else if (*itN > *itK) {
            fair_count++;
            itN++;
        }
    }
    // deceitful play
    itN=Naomi.begin();
    itK=Ken.begin();
    while (itN != Naomi.end() && itK != Ken.end()) {
        if (*itN > *itK) {
            itN++;
            itK++;
            deceitful_count++;
        } else if (*itN < *itK) {
            itK++;
        }
    }
    cout << "Case #" << i << ": " << deceitful_count << " " << fair_count << endl;
}
