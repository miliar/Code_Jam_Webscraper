#include <iostream>
#include <string>
#include <array>
#include <cstring>
#include <queue>
#include <cstdlib>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;
double v, x;
int n, t;

pair<double, double> sources[105];
vector<pair<double, double> > equalss;
vector<pair<double, double> > lower;
vector<pair<double, double> > upper;

double maxVal = 100000000.0;
double EPSILON = 1e-12;

bool same(double a, double b)
{
    return fabs(a - b) < EPSILON;
}

int main() {
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> n >> v >> x;
        lower.clear(); upper.clear(); equalss.clear();
        for (int i = 0; i < n; i++) {
            double t1, t2;
            cin >> t1 >> t2;
            sources[i] = make_pair(t2, t1);
            if (t2 == x) {
                equalss.push_back(sources[i]);
            } else if (t2 < x) {
                lower.push_back(sources[i]);
            } else {
                upper.push_back(sources[i]);
            }
        }
        sort(lower.begin(), lower.end());
        sort(upper.begin(), upper.end());
        reverse(lower.begin(), lower.end());

        if (equalss.size() == 0) {
            if (lower.size() == 0 || upper.size() == 0) {
                cout << "Case #" << test << ": " << "IMPOSSIBLE" << endl;
                continue;
            }
        }

        double totalVol = 0.0;
        double totalTV = 0.0;

        if (lower.size() != 0 && upper.size() != 0) {
            // double lowerVol = 0.0, lowerTV = 0.0, upperVol = 0.0, upperTV = 0.0;
            // for (int i = 0; i < lower.size(); i++) {
            //     lowerVol += lower[i].second;
            //     lowerTV += lower[i].second * lower[i].first;
            // }
            // for (int i = 0; i < upper.size(); i++) {
            //     upperVol += upper[i].second;
            //     upperTV += upper[i].second * upper[i].first;
            // }
            for (int i = 0; i < lower.size(); i++) {
                totalVol += lower[i].second;
                totalTV += lower[i].second * lower[i].first;
            }
            for (int i = 0; i < upper.size(); i++) {
                totalVol += upper[i].second;
                totalTV += upper[i].second * upper[i].first;
            }
            while (!same(totalTV / totalVol, x)) {
                pair<double, double> max;
                bool wasGreater;
                if (totalTV / totalVol > x) {
                    max = upper[upper.size() - 1];
                    upper.pop_back();
                    wasGreater = true;
        totalVol = 0.0;
        totalTV = 0.0;
            for (int i = 0; i < lower.size(); i++) {
                totalVol += lower[i].second;
                totalTV += lower[i].second * lower[i].first;
            }
            for (int i = 0; i < upper.size(); i++) {
                totalVol += upper[i].second;
                totalTV += upper[i].second * upper[i].first;
            }



                    if (totalTV / totalVol < x) {
                        double lowerV = 0.0, upperV = 1.0;
                            double chooseV = (lowerV + upperV)/2;
                        while (!same((totalTV + chooseV * max.first * max.second) / (totalVol + chooseV * max.second), x)) {
                            // cout << (totalTV + chooseV * max.first * max.second) / (totalVol + chooseV * max.second) << " " << x << endl;
                            chooseV = (lowerV + upperV)/2;
                            if ((totalTV + chooseV * max.first * max.second) / (totalVol + chooseV * max.second) > x) {
                                upperV = chooseV;
                            } else {
                                lowerV = chooseV;
                            }
                        }
                        totalTV += chooseV * max.first * max.second;
                        totalVol += chooseV * max.second;
                        // cout << totalVol << endl;
                        break;
                    }
                } else {
                    max = lower[lower.size() - 1];
                    lower.pop_back();
                    wasGreater = false;
        totalVol = 0.0;
        totalTV = 0.0;
            for (int i = 0; i < lower.size(); i++) {
                totalVol += lower[i].second;
                totalTV += lower[i].second * lower[i].first;
            }
            for (int i = 0; i < upper.size(); i++) {
                totalVol += upper[i].second;
                totalTV += upper[i].second * upper[i].first;
            }


                    if (totalTV / totalVol > x) {
                        double lowerV = 0.0, upperV = 1.0;
                            double chooseV = (lowerV + upperV)/2;
                        while (!same((totalTV + chooseV * max.first * max.second) / (totalVol + chooseV * max.second), x)) {
                            // cout << chooseV << " " << (totalTV + chooseV * max.first * max.second) / (totalVol + chooseV * max.second) << " " << x << endl;
                            chooseV = (lowerV + upperV)/2;
                            if ((totalTV + chooseV * max.first * max.second) / (totalVol + chooseV * max.second) > x) {
                                lowerV = chooseV;
                            } else {
                                upperV = chooseV;
                            }
                        }
                        totalTV += chooseV * max.first * max.second;
                        totalVol += chooseV * max.second;
                        // cout << totalVol << endl;
                        break;
                    }
                }
        }
        // cout << v << " " << totalVol << endl;

        }
        for (int i = 0; i < equalss.size(); i++) {
            totalVol += equalss[i].second;
        }

            cout << "Case #" << test << ": " << setprecision(15) << (v / totalVol) << endl;
    }
}
