#define _CRT_SECURE_NO_WARNINGS

#include <iostream>
#include <cstdio>
#include <queue>
#include <algorithm>

using namespace std;

int calc_time(priority_queue<int>& q, int spec_time, int time)
{
    time = min(time, q.top() + spec_time);

    if (spec_time >= time || spec_time >= q.top())
        return time;

    if (q.top() <= 1)
        return time;

    int val = q.top();
    q.pop();
    for (int i = 1; i <= val / 2; ++i) {
        priority_queue<int> buf = q;
        buf.push(val - i);
        buf.push(i);
        time = calc_time(buf, spec_time + 1, time);
    }

    return time;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests(0);

	cin >> tests;

	for (int test = 1; test <= tests; ++test) {
		priority_queue<int> q;
		int plates(0);

		cin >> plates;
		for (int i = 0; i < plates; ++i) {
			int a(0);
			cin >> a;
			q.push(a);
		}

		int min_time(q.top());
		int spec_mins(0);

        min_time = calc_time(q, spec_mins, min_time);

		/*while (q.top() > 1) {
			int val(q.top());
			q.pop();
            int x(0);
            if (q.empty()) {
                x = val / 2;
            }
            else {
                if (q.top() == val)
                    x = val / 2;
                else x = val - q.top();
            }
            q.push(val - x);
			q.push(x);
			spec_mins++;
            min_time = min(min_time, q.top() + spec_mins);
		}*/

		cout << "Case #" << test << ": " << min_time << endl;
	}
	return 0;
}