#include <iostream>
#include <utility>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;

bool cmp(const pair<char, int> a, const pair<char, int> b) {
    return a.second > b.second;
}

bool isSpecialCase (vector< pair<char, int> > &senators) {
    if (senators.size() >= 3 && senators[0].second == 1
        && senators[1].second == 1 && senators[2].second == 1) {
            if (senators.size() == 3) {
                return true;
            } else {
                if (senators[0].second == 0) {
                    return true;
                }
            }

    }
    return false;
}

int main() {
    ifstream infile ("input.in");
    ofstream outfile("output.out");
    if (!infile || !outfile){
        return 0;
    }
    int T;
    infile >> T;
    for (int c = 1; c <= T; c++) {
        int N;
        infile >> N;
        vector< pair<char, int> > senators;
        for (int i = 0; i < N; i++) {
            pair<char, int> senator;
            senator.first = 'A' + i;
            infile >> senator.second;
            senators.push_back(senator);
        }
        sort(senators.begin(), senators.end(), cmp);
        outfile << "Case #" << c << ": ";
        while (senators[0].second != 0) {
            if (isSpecialCase(senators)) {
                outfile << senators[0].first << " " << senators[1].first << senators[2].first;
                break;
            } else {
                outfile << senators[0].first;
                senators[0].second--;
                if (senators[0].second >= senators[1].second) {
                    outfile << senators[0].first;
                    senators[0].second--;
                } else {
                    outfile << senators[1].first;
                    senators[1].second--;
                }
                outfile << " ";
                sort(senators.begin(), senators.end(), cmp);
            }
        }
        outfile << endl;
        /*
        for (int i = 0; i < N; i++) {
            outfile << senators[i].first << " ";
        }
        outfile << end;
        */
    }
    infile.close();
    outfile.close();
    return 0;
}
