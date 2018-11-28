#include <string>
#include <iostream>
#include <algorithm>
#include <sstream>
#include <vector>
#include <set>
#include <cstdio>
#include <cstring>

using namespace std;

int main()
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("output.out", "w", stdout);
    set<int> cards;
    string line;
    int cases, stackCard, actualCase = 1;
    cin >> cases;
    getline(cin, line);
    while(cases--) {
        cards.clear();
        cin >> stackCard;
        stackCard--;
        getline(cin, line);
        for(int i = 0; i < 4; ++i ) {
            getline(cin, line);
            if(i == stackCard) {
                istringstream iss(line);
                while(1) {
                    int temp;
                    iss >> temp;
                    if(!iss)
                        break;
                    //cout << temp << endl;
                    cards.insert(temp);
                }
            }
        }
        //cout << cards.size() << endl;
        cin >> stackCard;
        stackCard--;
        getline(cin, line);
        vector<int> coincidence;
        for(int i = 0; i < 4; ++i ) {
            getline(cin, line);
            if(i == stackCard) {
                istringstream iss(line);
                while(1) {
                    int temp = 0;
                    iss >> temp;
                    if(!iss)
                        break;
                    if(cards.find(temp) != cards.end()) {
                        coincidence.push_back(temp);
                    }
                }
            }
        }
        cout << "Case #" << actualCase << ": ";
        if(coincidence.empty()) {
            cout << "Volunteer cheated!" << endl;
        } else if(coincidence.size() > 1) {
            cout << "Bad magician!" << endl;
        } else {
            cout << coincidence[0] << endl;
        }
        actualCase++;
    }
    return 0;
}
