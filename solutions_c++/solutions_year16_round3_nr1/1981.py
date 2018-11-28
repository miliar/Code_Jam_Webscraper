#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <utility>
#include <cstdio>
#include <cmath>
#include <functional>
#include <numeric>

using namespace std;

bool check(vector<int>& party, vector<int> select) {
    vector<int> next_party(party);
    int next_sum = accumulate(party.begin(), party.end(), 0);
    for ( int x : select ) {
        next_party[x]--;
        next_sum--;
    }
    for ( int x : next_party ) {
        if ( x * 2 > next_sum ) {
            return false;
        }
    }
    for ( int x : select ) {
        printf("%c", 'A' + x);
        party[x]--;
    }
    printf(" ");
    return true;
}

bool evacuate(vector<int>& party) {
    const int N = party.size();
    for ( int i=0 ; i<N ; ++i ) {
        if (party[i] > 0) {
            vector<int> select;
            select.push_back(i);
            if ( check(party, select) ) return true;
            for (int j = 0; j < N; ++j) {
                if (party[j] > 0) {
                    select.push_back(j);
                    if ( check(party, select) ) return true;
                }
            }
        }
    }
    return false;
}

int main()
{
    int T;
    cin >> T;
    for ( int tc=1 ; tc<=T ; ++tc ) {
        printf("Case #%d: ", tc);

        int N;
        cin >> N;
        vector<int> party(N);
        int sum = 0;
        for ( int i=0 ; i<N ; ++i ) {
            cin >> party[i];
            sum += party[i];
        }

        while ( accumulate(party.begin(), party.end(), 0) ) {
            evacuate(party);
        }
        puts("");
    }
    return 0;
}
