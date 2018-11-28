#include <iostream>
#include <string>
#include <cstdio>
using namespace std;

void perform()
{
    int smax;
    int add_counter = 0;
    int counter = 0;

    string shy;
    cin >> smax >> shy;

    counter = shy[0] - '0';

    for (int si = 1; si <= smax; si++)
    {
        int shy_i = shy[si] - '0';
        if (counter < si && shy_i != 0)
        {
            add_counter += si - counter;
            counter += add_counter;
        }

        //cout << "\n si=" << si << "  counter=" << counter << endl;
        counter += shy_i;
    }
    cout << add_counter << endl;
}

void redirect()
{
    freopen("q1.in", "r", stdin);
    freopen("q1.out", "w", stdout);
}

int main()
{
    redirect();
    int total_tests;
    cin >> total_tests;
    for (int test_id = 1; test_id <= total_tests; test_id++)
    {
        cout << "Case #" << test_id << ": ";
        perform();
    }
    return 0;
}
