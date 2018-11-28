#include <set>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <vector>
#include <limits>
#include <utility>
#include <map>
#include <sstream>
#include <queue>

using namespace std;

#define MAXN 15
#define MAXD 50
#define MOD 1000000007

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> ii;

vi dfs_num, dfs_low, S, visited;
ll T,n, x, y;
int dfsNumberCounter;

vector< vector<int> > AdjList;

string s;


int main(){


    cin >> T;
    for (int cse = 1; cse <= T; cse++){
        cin >> n;
        map<int, int> mp;
        vector<int> res;
        for (int i = 0; i < 2*n -1; i++){
            for (int j = 0; j < n; j++){
                int val;
                cin >> val;
                mp[val]++;
            }
        }

        for (auto it : mp){
            if (it.second % 2){
                res.push_back(it.first);
            }
        }
        sort(res.begin(), res.end());
        cout << "Case #" << cse << ":";
        for (int i = 0; i < res.size(); i++){
            cout << " " << res[i];
        }
        cout << endl;

    }

    return 0;

}


