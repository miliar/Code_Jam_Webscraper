#include <iostream>
#include <cstring>
#include <fstream>

using namespace std;

int main(){
    ifstream cin("A-large.in");
    ofstream cout("output.txt");

    int t;
    cin >> t;

    for (int tc = 0; tc < t; tc++){
        int n;
        string s;

        cin >> n >> s;
        int currentlyStanding = 0;
        int friendsInvited = 0;

        for (int i = 0; i <= n; i++){
            int k = s[i] - '0';
            if (k == 0) continue;
            if (i > currentlyStanding){
                int inviteFriends = i - currentlyStanding;
                currentlyStanding += inviteFriends;
                friendsInvited += inviteFriends;
            }

            currentlyStanding += k;
        }

        cout << "Case #" << (tc+1) << ": " << friendsInvited << endl;
    }

    return 0;
}
