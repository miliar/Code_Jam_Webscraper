#include <iostream>
#include <string>
#include <cstdio>

using namespace std;

void exec()
{
    double c, f, x;
    cin >> c >> f >> x;

    double min_time = x / 2.0;
    double speed = 2.0;
    double pasted_time = 0.0;
    int stp = 0;
    while(++stp && stp < 50000)
    {
        pasted_time += c / speed;
        speed += f;
        double current_time = pasted_time + x / speed;
        if (current_time < min_time)
            min_time = current_time;
    }
    printf("%.7lf\n", min_time);
}

int main()
{
    //freopen("q2in.txt", "r", stdin);
    //freopen("q2out.txt", "w", stdout);
    int t;
    cin >> t;
    for (int idx = 1; idx <= t; idx++)
    {
        cout << "Case #" << idx << ": ";
        exec();
    }
    return 0;
}
