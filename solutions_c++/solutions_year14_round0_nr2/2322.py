#include <string>
#include <cstring>
#include <cstdio>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
using namespace std;

double solve_case() {
    double F, C, X;
    cin >> C >> F >> X;
    double spent = 0.0,
        speed = 2.0,
        gath = 0.0,
        time_to_spend,
        to_factory,
        with_factory;
    while(true) {
        time_to_spend = (X - gath) / speed;
        to_factory = (C - gath) / speed;
        with_factory = X / (speed + F) + to_factory;

        if(with_factory < time_to_spend) {
            speed += F;
            spent += to_factory;
        }
        else return spent + time_to_spend;
    }
}

int main() {
    int cases;
    cin >> cases;
    for(int case_number=1; case_number<=cases; case_number++) {
        printf("Case #%d: ", case_number);
        printf("%.7lf\n", solve_case());
    }

    return 0;
}