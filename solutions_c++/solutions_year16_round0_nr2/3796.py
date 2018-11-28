/*
	Alexandre Borgo - Google Code Jam - 2016 - B. Revenge of the Pancakes
*/

#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <windows.h>

using namespace std;

string flip(string pancakes, int from, int to) {
    string new_pancakes = pancakes;

    for(int i = from ; i <= int(to/2) ; i++) {
        char tmp = new_pancakes[i];
        new_pancakes[i] = new_pancakes[to-i];
        new_pancakes[to-i] = tmp;
    }

    for(int i = from ; i <= to ; i++) {
        if(new_pancakes[i] == '+') new_pancakes[i] = '-';
        else new_pancakes[i] = '+';
    }
    return new_pancakes;
}

bool areAllPancakesHappy(string pancakes) {
    for(int i = 0 ; i < pancakes.size() ; i++) {
        if(pancakes[i] == '-') return false;
    }
    return true;
}

bool areAllPancakeBlanc(string pancakes) {
    for(int i = 0 ; i < pancakes.size() ; i++) {
        if(pancakes[i] == '+') return false;
    }
    return true;
}

int main()
{
    int T;

    cin >> T;

    for(int i = 1 ; i <= T ; i++) {

        string pancakes;
        cin >> pancakes;

        int countman = 0;
        char last = pancakes[0];

        for(int pan = 1 ; ; pan++) {

            if(last != pancakes[pan] && pancakes.size()>1) {
                pancakes = flip(pancakes,0,pan-1);
                countman++;
            }

            last = pancakes[pan];

            if(areAllPancakeBlanc(pancakes)) {
                pancakes = flip(pancakes,0,pancakes.size());
                countman++;
            }

            if(areAllPancakesHappy(pancakes)) {
                break;
            }
        }

        cout << "Case #" << i << ": " << countman << endl;
    }

    return 0;
}
