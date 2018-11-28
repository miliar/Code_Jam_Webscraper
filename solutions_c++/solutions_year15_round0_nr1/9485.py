#include<iostream>
#include<string>
#include<sstream>
#include<list>
#include<vector>

using namespace std;
int main(){
    int t;
    cin >> t;
    cin.ignore();
    for(int i = 1; i <= t; i++) {
        char stc[1301];
        cin.getline(stc,1300);
        string st(stc);

        stringstream ss;
        ss << st;
        int Smax;
        string desc;
        ss >> Smax >> desc;

        int standedUpPeople = 0;
        int invitedFriends = 0;
        for(int j = 0; j < desc.size(); j++) {
            int actualShyness = j;
            int peopleAtThisShynessLevel;
            char c = desc[j];
            peopleAtThisShynessLevel = c - '0';
            if((standedUpPeople) < actualShyness) {
                int neededPeople = actualShyness - standedUpPeople;
                invitedFriends += neededPeople;
                standedUpPeople += neededPeople;
            }
            standedUpPeople += peopleAtThisShynessLevel;
        }

        cout << "Case #" << i << ": " << invitedFriends << endl;
    }
}
