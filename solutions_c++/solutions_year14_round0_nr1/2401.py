#include <cstdio>
#include <iostream>
#include <sstream>
#include <fstream>
#include <iomanip>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <bitset>
#include <numeric>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

int main()
{
    int T;
    cin >> T;

    for(int tc=1; tc<=T; ++tc){
        vector<vector<vector<int> > > a(2, vector<vector<int> >(4, vector<int>(4)));
        vector<int> y(2);
        for(int i=0; i<2; ++i){
            cin >> y[i];
            -- y[i];
            for(int j=0; j<4; ++j){
                for(int k=0; k<4; ++k)
                    cin >> a[i][j][k];
                sort(a[i][j].begin(), a[i][j].end());
            }
        }

        vector<int> v;
        set_intersection(a[0][y[0]].begin(), a[0][y[0]].end(),
                         a[1][y[1]].begin(), a[1][y[1]].end(),
                         back_inserter(v));

        cout << "Case #" << tc << ": ";
        if(v.size() == 0)
            cout << "Volunteer cheated!" << endl;
        else if(v.size() == 1)
            cout << v[0] << endl;
        else
            cout << "Bad magician!" << endl;
    }

    return 0;
}