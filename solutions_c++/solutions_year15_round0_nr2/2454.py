#include <algorithm>
#include <bitset>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <deque>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <utility>
#include <vector>

typedef unsigned long long int ulld;
using namespace std;

typedef pair<int,int> ii;
typedef vector<ii> vii;
typedef vector<int> vi;
typedef vector<bool> vb;

int main ()
{
    int t, caso = 1;
    cin >> t;
    while(t--){
        vector<int>p;
        int d, aux, resp, m;
        cin >> d;
        for(int i = 0; i < d; i++){
            cin >> aux;
            p.push_back(aux);
        }
        sort(p.begin(), p.end());
        reverse(p.begin(), p.end());
        resp = p[0];
        m = p[0];
        for (int r = 1; r < m; ++r)
        {
            double move = 0;
            for (int z = 0; z < p.size(); ++z)
            {
                if(p[z] <= r)
                    break;
                move += ceil((double)p[z] / (double)r) - 1;
            }
            if(move + r < resp)
                resp =  move+r;
        }
        cout << "Case #" << caso++ << ": " << resp << endl;
    }
    return 0;
}