#include <bits/stdc++.h>

using namespace std;

ifstream f("test.in");
//ofstream g("test.out");

const int NMAX = 1e3+5;

void scrie(int noTest, int ans){
    printf("Case #%d: %d\n", noTest, ans);
}

int main(){
    freopen("test.out", "w", stdout);
    int t;f >> t;
    string s; int smax;
    for(int noTest=1; noTest<=t; ++noTest){
        f >> smax;
        f >> s;
        int cntFriends = 0;
        int currentStandUpPeople = 0;
        if (s[0] == '0') cntFriends = 1, currentStandUpPeople = 1;
        else currentStandUpPeople = s[0] - '0';
        for(int i=1; i<s.size(); ++i){
            if (s[i] == '0') continue;
            if (currentStandUpPeople < i){
                int x = i - currentStandUpPeople;
                cntFriends += x;
                currentStandUpPeople += x + s[i] - '0';
            }else{
                currentStandUpPeople += s[i] - '0';
            }
        }

        scrie(noTest, cntFriends);
    }

    return 0;
}
