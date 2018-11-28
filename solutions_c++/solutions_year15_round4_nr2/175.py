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
#include <limits>
#include <climits>
#include <cfloat>
#include <functional>
using namespace std;

const double EPS = 1.0e-10;

class Source
{
public:
    double temperature;
    double volume;
    Source(){
        temperature = 0.0;
        volume = 0.0;
    }
    Source(double temperature, double volume){
        this->temperature = temperature;
        this->volume = volume;
    }
    bool operator<(const Source& s) const{
        return make_pair(temperature, volume) < make_pair(s.temperature, s.volume);
    }
    Source combine(const Source& s) const{
        Source ans;
        ans.temperature = (temperature * volume + s.temperature * s.volume) / (volume + s.volume);
        ans.volume = volume + s.volume;
        return ans;
    }
    double canAddVolume(double c, double x) const{
        return ((x - temperature) * volume) / (c - x);
    }
};

double solve1(double v, double x, const vector<double>& r, const vector<double>& c)
{
    int n = r.size();
    Source a;
    vector<Source> b;
    for(int i=0; i<n; ++i){
        if(c[i] <= x + EPS)
            a = a.combine(Source(c[i], r[i]));
        else
            b.push_back(Source(c[i], r[i]));
    }
    if(a.volume <= EPS)
        return DBL_MAX;

    sort(b.begin(), b.end());
    n = b.size();
    for(int i=0; i<n; ++i){
        double volume = a.canAddVolume(b[i].temperature, x);
        volume = min(volume, b[i].volume);
        a = a.combine(Source(b[i].temperature, volume));
    }

    if(a.temperature < x - EPS)
        return DBL_MAX;
    else
        return v / a.volume;
}

double solve2(double v, double x, const vector<double>& r, const vector<double>& c)
{
    int n = r.size();
    Source a;
    vector<Source> b;
    for(int i=0; i<n; ++i){
        if(c[i] >= x - EPS)
            a = a.combine(Source(c[i], r[i]));
        else
            b.push_back(Source(c[i], r[i]));
    }
    if(a.volume <= EPS)
        return DBL_MAX;

    sort(b.rbegin(), b.rend());
    n = b.size();
    for(int i=0; i<n; ++i){
        double volume = a.canAddVolume(b[i].temperature, x);
        volume = min(volume, b[i].volume);
        a = a.combine(Source(b[i].temperature, volume));
    }

    if(a.temperature > x + EPS)
        return DBL_MAX;
    else
        return v / a.volume;
}

int main()
{
    int n;
    cin >> n;

    cout.setf(ios_base::fixed, ios_base::floatfield);
    cout << setprecision(10);

    for(int i=1; i<=n; ++i){
        int n;
        double v, x;
        cin >> n >> v >> x;

        vector<double> r(n), c(n);
        for(int j=0; j<n; ++j)
            cin >> r[j] >> c[j];

        double ans = min(solve1(v, x, r, c), solve2(v, x, r, c));
        if(ans < DBL_MAX / 2)
            cout << "Case #" << i << ": " << ans << endl;
        else
            cout << "Case #" << i << ": IMPOSSIBLE" << endl;
    }

    return 0;
}