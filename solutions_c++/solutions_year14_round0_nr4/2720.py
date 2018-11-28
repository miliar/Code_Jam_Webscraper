#include <iostream>
#include <vector>
#include <algorithm>
#include <deque>

using namespace std;

double solve(double C, double F, double X)
{
    double cps = 2.0; // cookie per second
    double min_time = X / cps;
    double next_time = C / cps;

    while (1) {
        double n_t = next_time + (X / (cps + F));
        if (n_t < min_time) min_time = n_t;
        else return min_time;

        cps += F;
        next_time += C / cps;
    }
}

int solve_dwar(deque<double> a, deque<double> b)
{
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int point = 0;

    while (!a.empty()) {
        if (a.front() < b.front()){
            a.pop_front(); b.pop_back();
        }
        else {
            a.pop_front(); b.pop_front();
            point++;
        }
    }
    return point;
}

int solve_war(deque<double> a, deque<double> b)
{
    sort(a.begin(), a.end());
    sort(b.begin(), b.end());

    int point = 0;

    while (!b.empty()) {
        if (a.front() < b.front()) {
            a.pop_front(); b.pop_front();
        }
        else {
            b.pop_front();
            point++;
        }
    }
    return point;
}


int main(void) {
    int c;
    cin >> c;

    for (int i = 0; i < c; i++) {
        int s;
        double tmp;
        deque<double> a, b;
        cin >> s;
        for (int i = 0; i < s; i++) { cin >> tmp; a.push_back(tmp); }
        for (int i = 0; i < s; i++) { cin >> tmp; b.push_back(tmp); }
        printf("Case #%d: %d %d\n", i + 1, solve_dwar(a, b), solve_war(a, b));
    }
}