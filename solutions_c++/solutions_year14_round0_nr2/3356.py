#include <bits/stdc++.h>

using namespace std;

double c, f, x, answer;

void calculate(double rate = 2.0, double time = 0.0) {
    if(time >= answer)
        return;

    // If not building new farm
    answer = min(answer, time + (x / rate));

    calculate(rate + f, time + (c / rate));
}

int main() {
    freopen("B-large.in", "r", stdin);
     freopen("B-large.out", "w", stdout);

    //  ios_base::sync_with_stdio(0);
//    cin.tie(0);

    int t;
    cin >> t;

    for(int t1 = 1; t1 <= t; ++t1) {
        printf("Case #%d: ", t1);

        cin >> c >> f >> x;

        answer = 415457545454545455.0;

        calculate();


        printf("%.10f\n", answer);
    }

}
