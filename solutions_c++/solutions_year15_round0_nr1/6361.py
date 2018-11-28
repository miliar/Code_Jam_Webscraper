#include<iostream>
#include<vector>
using namespace std;

unsigned int solution(const std::vector<short>& counts) {
    unsigned int nPeopleStanding=0;
    unsigned int nAddedPeople=0;
    for (unsigned int i=0;i<counts.size();++i) {
        if (counts[i] != 0) {
            if (nPeopleStanding<i) {
                nAddedPeople += (i-nPeopleStanding);
                nPeopleStanding = i;
            }
            nPeopleStanding += counts[i];
        }
    }
    return nAddedPeople;
}

int main() {
    unsigned int T;
    cin >> T;
    for (unsigned int t=0;t<T;++t) {
        unsigned int n;
        cin >> n;
        std::vector<short> counts(n+1,0);
        unsigned char c;
        // cin >> c;
        for (unsigned int i=0;i<=n;++i) {
            cin >> c;
            counts[i] = c-'0';
        }
        cout << "Case #" << (t+1) << ": " << solution(counts) << std::endl;
    }
    return 0;
}
