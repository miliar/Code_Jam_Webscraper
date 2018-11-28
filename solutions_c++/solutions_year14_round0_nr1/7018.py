#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include<cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>

using namespace std;


int main()
{
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	ios_base::sync_with_stdio(false);
    int t,a,b;
    cin >> t;
    for(int x = 1; x <= t; x++) {
        cin >> a;
        map<int, int> m;
        int p[4][4], q[4][4];
        for(int i = 0 ; i < 4; i++)
            for(int  j = 0; j < 4; j++) cin >> p[i][j];
        cin >> b;
         for(int i = 0 ; i < 4; i++)
            for(int  j = 0; j < 4; j++) cin >> q[i][j];
        int ctr = 0;
        for(int i = 0; i < 4; i++) m[p[a-1][i]]++;
        for(int i = 0; i < 4; i++) m[q[b-1][i]]++;
        if(m.size() == 8) cout << "Case #" << x << ": " << "Volunteer cheated!" << endl;
        else if(m.size() < 7) cout << "Case #" << x << ": " << "Bad magician!" << endl;
        else {
                map<int, int> :: iterator it;
                for(it = m.begin(); it != m.end(); it++) {
                    if((*it).second == 2) {
                            cout << "Case #" << x << ": " <<(*it).first << endl;
                            break;
                    }
                }
        }
    }
}
