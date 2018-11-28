#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

typedef long long LL;
typedef unsigned int UL;
using namespace std;

const int MAXN = 10000 + 10;


int main () {
	int cases;
	cin >> cases;
	for (int tc = 1; tc <= cases; tc ++) {
        
        cout << "Case #" << tc << ": ";
        LL K, C, S;
        cin >> K >> C >> S;

        vector<pair<LL,LL>> index;
        
        for (LL k = 1; k <= K; k ++) 
            index.push_back(make_pair(k, k));
        
        for (int j = 0; j < C - 1; j ++) {
            for (int k = 0; k < K; k ++) {
                index[k].first = (index[k].first - 1) * K + index[k].second;    
            }
        }

        for (int j = 0; j < S; j ++) {
            if (j != 0) cout << " ";
            cout << index[j].first ;
        }
        cout << endl;
    }
}
