#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

int T;

int N;

int caseNum = 0;

set<double> nBlocksOrig;
set<double> kBlocksOrig;

void readSize() {
    cin >> N;
}

void readN() {
    nBlocksOrig.clear();
    for (int i = 0; i < N; i++) {
        double block;
        cin >> block;
        nBlocksOrig.insert(block);
    }
}

void readK() {
    kBlocksOrig.clear();
    for (int i = 0; i < N; i++) {
        double block;
        cin >> block;
        kBlocksOrig.insert(block);
    }
}

void outputCase() {
    printf("Case #%d: ", ++caseNum);
}

void outputDW() {
    set<double> nBlocks = nBlocksOrig;
    set<double> kBlocks = kBlocksOrig;
    int score = 0;
    for (int i = 0; i < N; i++) {
        set<double>::iterator nit = nBlocks.begin();
        set<double>::iterator kit = kBlocks.begin();
        if (*nit > *kit) {
            score++;
            nBlocks.erase(nit);
            kBlocks.erase(kit);
        } else {
            nBlocks.erase(nit);
            kBlocks.erase(*kBlocks.rbegin());
        }
    }
    cout << score << " ";
}

void outputW() {
    set<double> nBlocks = nBlocksOrig;
    set<double> kBlocks = kBlocksOrig;
    int score = 0;
    for (int i = 0; i < N; i++) {
        set<double>::iterator nit = nBlocks.begin();
        set<double>::iterator kit = kBlocks.upper_bound(*nit);
        if (kit == kBlocks.end()) {
            kit = kBlocks.begin();
            score++;
        }
        nBlocks.erase(nit);
        kBlocks.erase(kit);
    }
    cout << score;
}

void outputEnd() {
    cout << endl;
}

int main() {
    cin >> T;
    for (int i = 0; i < T; i++) {
        //cout << N << endl;
        readSize();
        readN();
        readK();
        outputCase();
        outputDW();
        outputW();
        outputEnd();
    }
}
