/* 
 * File: main.cpp
 * Copyright © Jan Škoda
 */

#include <cstdlib>
#include <iostream>
#include <cassert>
#include <iomanip>
#include <cstdio>
#include <vector>

using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int N;
    cin >> N;
    for (int n = 1; n <= N; n++) {
        int SM;
        cin >> SM;
        int standing = 0;
        int friends = 0;
        for (int shy_level = 0; shy_level <= SM; shy_level++) {
            int count;
            scanf("%1d", &count);
//            cout << "Shyness " << shy_level << " people " << count << endl;
            int new_friends = max(0, shy_level - standing);
            friends += new_friends;
            standing += count + new_friends;
        }
        printf("Case #%d: %d\n", n, friends);
    }
    return 0;
}

