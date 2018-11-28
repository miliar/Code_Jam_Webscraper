#include<cstdio>
#include<iostream>
#include<string>
#include<algorithm>

using namespace std;

int main() {
    int ntc;
    cin >> ntc;
    for(int TC=1; TC<=ntc; ++TC) {
        int Smax;
        string Si;
        cin >> Smax >> Si;
        
        int currentStandingOvation = 0;
        int neededFriends = 0;
        for(int i=0; i<Smax+1; i++) {
            int current = Si[i] - '0';
            int currentNeededFriends = max( 0, i - currentStandingOvation );
            
            currentStandingOvation += currentNeededFriends;
            currentStandingOvation += current;
            neededFriends += currentNeededFriends;
        }
        cout << "Case #" << TC << ": " << neededFriends << endl;
    }
    return 0;
}
