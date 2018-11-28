#define _USE_32BIT_TIME_T 1
#include <vector> // headers {{{
#include <list>
#include <queue>
#include <set>
#include <map>
#include <string>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <functional>
#include <numeric>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <fstream>
#include <ctime>

#define DEBUG(x) cout << #x << ": " << x << "\n"
using namespace std; // }}}

bool test(const vector<double>& v0, const vector<double>& v1)
{
    int n = v0.size();
    for (int i = 0; i < v0.size(); ++i) {
        if (v0[n - 1 - i] < v1[i])
            return false;
    }
    return true;
}

string result(ifstream& cin)
{
    int N;
    cin >> N;
    vector<double> v0(N), v1(N);
    for (int i = 0; i < N; ++i)
        cin >> v0[i];
    for (int j = 0; j < N; ++j)
        cin >> v1[j];
    sort(v0.begin(), v0.end());
    sort(v1.begin(), v1.end());
    vector<double> v00(v0), v10(v1);
    reverse(v00.begin(), v00.end());
    while (!v00.empty() && !test(v00, v10)) {
        v00.pop_back();
        v10.pop_back();
    }
    int y = v00.size();
    int pos = 0, I = 0, z = 0;
    for (I = 0; pos < N && I < N; ++I, ++pos) {
        while (pos < N && v1[pos] < v0[I]) {
            ++pos;
            ++z;
        }
    }
    char buf[1000];
    sprintf(buf, "%d %d", y, z);
    return buf;
}

int main()
{
    time_t start, end;
    time(&start);
    
    ifstream cin("test.in");
    ofstream cout("test.out");
    //cout.precision(6);
    //cout.setf(ios::fixed,ios::floatfield);

    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        cout << "Case #" << i << ": " << result(cin) << endl;
        time(&end);
        ::cout << i << " " << difftime(end, start) << endl;
    }

    return 0;
}
