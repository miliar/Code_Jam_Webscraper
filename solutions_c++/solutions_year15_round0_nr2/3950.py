#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>
#include <queue>
using namespace std;

int N;
int D;
vector<int> diners;
int minutes;

struct Node {
    int minutes;
    vector<int> plates;
};

int decrease(int value) {
    return value - 1;
}

void handleRegular() {
    //std::transform(diners.begin(), diners.end(), diners.begin(), decrease);
    for (int i = 0; i < diners.size(); i++) {
        if (diners[i] > 0) {
            diners[i]--;
        }
    }
}

void handleSpecial(int maxPancakes, int amount) {
    for (int i = 0; i < diners.size(); i++) {
        if (diners[i] == maxPancakes) {
            diners.push_back(amount);
            diners[i] -= amount;
            return;
        }
    }
}

void dump() {
    for (int i = 0; i < diners.size(); i++) {
        cout << diners[i] << " ";
    }
    cout << " ------------------ " << endl;
}

void solve() {
    Node currentNode;
    currentNode.minutes = 0;
    currentNode.plates = diners;
    queue<Node> q;
    q.push(currentNode);

    while(!q.empty()) {
        currentNode = q.front();
        q.pop();

        if (*max_element(currentNode.plates.begin(), currentNode.plates.end()) == 0) {
            minutes = currentNode.minutes;
            return;
        }

        diners = currentNode.plates;
        handleRegular();
        Node nextNode;
        nextNode.plates = diners;
        nextNode.minutes = currentNode.minutes + 1;
        q.push(nextNode);

        int maxElement = *max_element(currentNode.plates.begin(), currentNode.plates.end());
        for (int i = 1; i <= maxElement / 2; i++) {
            diners = currentNode.plates;
            handleSpecial(maxElement, i);
            Node specialNode;
            specialNode.plates = diners;
            specialNode.minutes = currentNode.minutes + 1;
            q.push(specialNode);
        }
    }
}

void clean() {
    minutes = 0;
    diners.clear();
}

void read() {
    cin >> D;
    for (int i = 0; i < D; i++) {
        int pancakes;
        cin >> pancakes;
        diners.push_back(pancakes);
    }
}

void print() {
    cout << minutes;
}

int main() {
    int n;
    scanf("%d", &n);
    cin.ignore (std::numeric_limits<std::streamsize>::max(), '\n');

    for (int i = 1; i <= n; i++) {
        clean();
        read();
        solve();

        printf("Case #%d: ", i);
        print();
        printf("\n");
    }

    return 0;
}

