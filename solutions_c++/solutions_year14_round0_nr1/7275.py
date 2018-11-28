//
//  main.cpp
//  MagicTrick
//
//  Created by Ciupin Iaroslav on 12/04/14.
//  Copyright (c) 2014 Ciupin Iaroslav. All rights reserved.
//

#include <iostream>
#include <vector>
using namespace std;

#define DECK_SIZE 4

void readDeck(vector<vector<int>> &deck) {
    for (int i = 0; i < DECK_SIZE; i++) {
        for (int j = 0; j < DECK_SIZE; j++) {
            cin >> deck[i][j];
        }
    }
}

int main(int argc, const char * argv[])
{
    int T = 0;
    cin >> T;
    vector<vector<int>> deck(DECK_SIZE);
    for (int i = 0; i < deck.size(); i++) {
        deck[i].resize(DECK_SIZE);
    }
    for (int t = 0; t < T; t++) {
        int answer1 = 0;
        cin >> answer1;
        readDeck(deck);
        vector<int> possible(DECK_SIZE);
        for (int i = 0; i < DECK_SIZE; i++) {
            possible[i] = deck[answer1 - 1][i];
        }
        int answer2 = 0;
        cin >> answer2;
        readDeck(deck);
        int candidate = 0;
        int numCandidates = 0;
        for (int i = 0; i < DECK_SIZE; i++) {
            for (int j = 0; j < DECK_SIZE; j++) {
                if (possible[i] == deck[answer2 - 1][j]) {
                    candidate = possible[i];
                    numCandidates++;
                }
            }
        }
        printf("Case #%d: ", t + 1);
        if (numCandidates == 0) {
            cout << "Volunteer cheated!\n";
        } else if (numCandidates == 1) {
            cout << candidate << endl;
        } else {
            cout << "Bad magician!\n";
        }
    }
    return 0;
}

