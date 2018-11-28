/* 
 * File:   main.cpp
 * Author: Shiva Prasad Goud Bandari <bshivagoud@gmaill.com>
 *
 * Created on 12 April, 2014, 2:54 PM
 */

#include <iostream>

using namespace std;

int main(int argc, char** argv) {

    unsigned int T, ans, r1[4], card, contains = 0, guessed_card;

    cin >> T;
    for(int t=1;t<=T;t++) {
        cin >> ans;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> card;
                if (ans == i + 1)
                    r1[j] = card;
            }
        }
        cin >> ans;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> card;
                if (ans == i + 1) {
                    if (card == r1[0] || card == r1[1] || card == r1[2] || card == r1[3]) {
                        contains++;
                        guessed_card = card;
                    }
                }
            }
        }
        switch (contains) {
            case 0:
                cout << "Case #"<<t<<": Volunteer cheated!"<<endl;
                break;
            case 1:
                cout << "Case #"<<t<<": " << guessed_card<<endl;
                break;
            default:
                cout << "Case #"<<t<<": Bad magician!"<<endl;
        }
        contains = 0;

    }

    return 0;
}

