#include <iostream>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <deque>
#include <set>
#include <map>
#include <fstream>
#include <utility>
#include <cmath>
#include <limits>
#include <set>
#include <iomanip>

#define cin fin
#define cout fout

#define all(c) c.begin(),c.end()
#define traverse(c,it) for(typeof(c.begin()) it = c.begin(); it != c.end(); it++)
#define ll long long
#define oo numeric_limits<int>::max();

using namespace std;

ifstream fin ("input.in");
ofstream fout ("output.out");

int main()
{
    cout << fixed << setprecision(7);
    int T;
    double C,F,X,c,time,rate;
    cin >> T;
    for(int t=0;t<T;t++){
        cin >> C >> F >> X;
        time=0;
        rate=2;
        while(((C/rate)+(X/(rate+F)))<(X/rate))
            time += C/rate,rate+=F;
        time += X/rate;
        cout << "Case #" << t+1 << ": " << time << endl;
    }
    return 0;
}
