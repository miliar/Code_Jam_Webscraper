#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

vector<int> tokenize(string counts) {
    string substr;
    vector<int> tokens;
    
    for (int i = 0; i < counts.length(); i++) {
        if (counts[i] != ' ') {
            substr += counts[i];
        } else {
            tokens.push_back(atoi(substr.c_str()));
            substr = "";
        }
    }

    tokens.push_back(atoi(substr.c_str()));

    return tokens;
}

int majority(vector<int> partyCounts) {
    int total = 0;
    for (int i = 0; i < partyCounts.size(); i++) {
        total += partyCounts[i];
    }

    return (total + partyCounts.size() - 1) / partyCounts.size();
}

bool areAllEvacuated(vector<int> partyCounts) {
    for (int i = 0; i < partyCounts.size(); i++) {
        if (partyCounts[i] != 0) {
            return false;
        }
    }

    return true;
}

int findMaxIndex(vector<int> v) {
    int max = v[0];
    int maxIndex = 0;

    for (int i = 1; i < v.size(); i++) {
        if (v[i] > max) {
            maxIndex = i;
            max = v[i];
        }
    }

    return maxIndex;
}

int main() {
    string counts;
    int numInputs;
    vector<int> partyCounts;

    cin >> numInputs;
    string tmp;
    getline(cin, tmp, '\n');

    for (int i = 1; i <= numInputs; i++) {
        getline(cin, tmp, '\n');
        getline(cin, counts, '\n');
        
        partyCounts = tokenize(counts);

        bool done = areAllEvacuated(partyCounts);

        cout << "Case #" << i << ": ";
        
        while (!done) {
            int maxIndex = findMaxIndex(partyCounts);
            int maxVal = partyCounts[maxIndex];
            partyCounts[maxIndex] = partyCounts[maxIndex] - 1;
            cout << char('A' + maxIndex);

            vector<int>::iterator it = find(partyCounts.begin(), partyCounts.end(), maxVal);

            if (it != partyCounts.end()) {
                (*it)--;
                vector<int>::iterator new_it = find(partyCounts.begin(), partyCounts.end(), maxVal);
                if (new_it != partyCounts.end()) {
                    (*it)++;
                } else {
                    cout << char('A' + (it - partyCounts.begin()));
                }
            } else {
                if (partyCounts[maxIndex] != 0) {
                    partyCounts[maxIndex] = partyCounts[maxIndex] - 1;
                    cout << char('A' + maxIndex);
                }
            }

            done = areAllEvacuated(partyCounts);

            if (!done) {
                cout << " ";
            } else {
                break;
            }
        }

        cout << endl;
    }

    return 0;
}