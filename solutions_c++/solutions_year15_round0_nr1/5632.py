// Copyright 2015 Thiago Barbato

#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>

using namespace std;

int main(int argc, char const *argv[]) {
    int n;
    cin >> n;
    cin.ignore();

    for (int i = 0; i < n; i++) {
        int maxShyness;
        int nFriends = 0;
        int count = 0;
        int peopleUp = 0;

        cin >> maxShyness;
        string buffer;
        cin >> buffer;

        for (char& c : buffer) {
            if (count == 0 && c == '0') {
                nFriends++;
                peopleUp++;
            }

            while (count > peopleUp) {
                nFriends++;
                peopleUp++;
            }

            peopleUp += (c - '0');
            count++;
        }

        cout << "Case #" << i + 1 << ": " << nFriends << endl;
    }
    return 0;
}
