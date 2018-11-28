#include <iostream>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

int currentBest;

int solve_helper(vector<int>& currentPancakes, int minutesPassed) {
    if (minutesPassed >= currentBest) {
        return currentBest;
    }

    if (currentPancakes.size() == 0) {
        return minutesPassed;
    }

    auto it = max_element(currentPancakes.begin(),
            currentPancakes.end());
    int maxPancakes = *it;

    if (maxPancakes <= 3) {
        return minutesPassed + maxPancakes;
    }

    int specialMinuteSolution;
    int consumeOneMinuteSolution;

    vector<int> copiedDS1;
    for (auto PI = currentPancakes.begin(), PE = currentPancakes.end();
            PI != PE; ++PI) {
        if (PI != it) {
            copiedDS1.push_back(*PI);
        }
    }

    int half = maxPancakes / 2;
    for (int i = 1; i <= half; ++i) {
        copiedDS1.push_back(i);
        copiedDS1.push_back(maxPancakes - i);

        specialMinuteSolution = solve_helper(copiedDS1, minutesPassed + 1);
        if (specialMinuteSolution < currentBest) {
            currentBest = specialMinuteSolution;
        }

        copiedDS1.pop_back();
        copiedDS1.pop_back();
    }

    specialMinuteSolution = currentBest;

    //vector<int> copiedDS2;
    //for (int numCakesRemaining : currentPancakes) {
    //    if (numCakesRemaining > 1) {
    //        copiedDS2.push_back(numCakesRemaining - 1);
    //    }
    //}

    //consumeOneMinuteSolution = solve_helper(copiedDS2, minutesPassed + 1);
    consumeOneMinuteSolution = minutesPassed + maxPancakes;
    if (consumeOneMinuteSolution < currentBest) {
        currentBest = consumeOneMinuteSolution;
    }

    if (specialMinuteSolution < consumeOneMinuteSolution) {
        return specialMinuteSolution;
    } else {
        return consumeOneMinuteSolution;
    }
}

int solve(vector<int>& currentPancakes) {
    auto it = max_element(currentPancakes.begin(),
            currentPancakes.end());
    currentBest = *it;
    return solve_helper(currentPancakes, 0);
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        int numDiners;
        cin >> numDiners;
        vector<int> currentPancakes;

        for (int j = 0; j < numDiners; ++j) {
            int nPancakes;
            cin >> nPancakes;
            currentPancakes.push_back(nPancakes);
        }

        int minutesNeeded = solve(currentPancakes);
        cout << "Case #" << i + 1 << ": " << minutesNeeded << endl;
    }

    return 0;
}
