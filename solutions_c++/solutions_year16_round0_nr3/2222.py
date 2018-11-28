#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
using namespace std;

// e.g. numPadding = 4
// result: 0000, 0001, 0011, 0111, ...
list< list<bool> > generatePaddingSeq(int size) {
    // BFS to generate sequences
    queue< list<bool> > frontier;

    list<bool> root;
    root.push_back(false);
    frontier.push(root);
    root.back() = true;
    frontier.push(root);

    list<bool> empty;   // use empty node to indicate a layer is finished
    frontier.push(empty);
    int numLayers = 1;

    while (true) {
        list<bool> parent = frontier.front();
        frontier.pop();

        if (parent.size() == 0) {   // meaning this is an empty node
            numLayers += 1;
            if (numLayers == size) {
                break;
            } else {
                frontier.push(empty);
                continue;
            }
        }

        parent.push_back(false);
        frontier.push(parent);
        parent.back() = true;
        frontier.push(parent);
    }

    // transform to a list
    list< list<bool> > retrunSequence;
    while (!frontier.empty()) {
        retrunSequence.push_back(frontier.front());
        frontier.pop();
    }
    return retrunSequence;
}

list< list<int> > assembleNumbers(list< list<bool> >& paddingSequence) {
    list< list<int> > result;

    for (list< list<bool> >::iterator seq = paddingSequence.begin(); seq != paddingSequence.end(); seq++) {
        list<int> oneResult;
        oneResult.push_back(1); // basic number: the beginning 11
        oneResult.push_back(1);
        for (list<bool>::iterator pad = seq->begin(); pad != seq->end(); pad++) {
            if (*pad) {
                oneResult.push_back(1);
                oneResult.push_back(1);
            } else {
                oneResult.push_back(0);
                oneResult.push_back(0);
            }
        }
        oneResult.push_back(1); // basic number: the ending 11
        oneResult.push_back(1);

        result.push_back(oneResult);
    }

    return result;
}


int main() {
    // inputs
    const int TOTAL_NUM_DIGITS = 32;
    const int TOTAL_COINS_NEEDED = 500;
    // basic idea:
    // baseX(1100000000000011) = baseX(11) * baseX(10000000000001)
    // so we use 1100000000000011 as the basic number, then pad bunch of "11" on the "0"s

    // padding sequence
    int paddingSeqSize = (TOTAL_NUM_DIGITS - 4) / 2;
    list< list<bool> > paddingSequence = generatePaddingSeq(paddingSeqSize);
    for (list< list<bool> > ::iterator it = paddingSequence.begin(); it != paddingSequence.end(); it++) {
        for (list<bool>::iterator inner = it->begin(); inner != it->end(); inner++) {
            cout << *inner;
        }
        cout << endl;
    }

    // assemble
    list< list<int> > results = assembleNumbers(paddingSequence);

    // output
    string outputFileName = "result1";
    ofstream resultFile;
    resultFile.open(outputFileName, ofstream::out | ofstream::trunc);
    resultFile << "Case #1:" << endl;
    int linesWritten = 0;
    for (list< list<int> >::iterator it = results.begin(); it != results.end(); it++) {
        for (list<int>::iterator inner = it->begin(); inner != it->end(); inner++) {
            cout << *inner;
            resultFile << *inner;
        }

        for (int base = 2; base <= 10; base++) {
            int divider = base + 1;
            cout << " " << divider;
            resultFile << " " << divider;
        }
        cout << endl;
        resultFile << endl;

        linesWritten += 1;
        if (linesWritten == TOTAL_COINS_NEEDED) {
            break;
        }
    }
    resultFile.close();

    return 1;
}