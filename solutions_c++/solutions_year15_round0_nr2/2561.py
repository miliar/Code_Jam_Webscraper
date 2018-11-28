#include <bits/stdc++.h>
#define NMAX 1005

using namespace std;

deque<int> elements;

void print_deque(deque<int> elements) {
    cout << "Elements: " << endl;
    for (auto e : elements) {
        cout << e << " ";
    }
    cout << endl;
}

int recursive(deque<int> elements, int splits, int solution) {
    //print_deque(elements);
    sort(elements.begin(), elements.end(), greater<int>());
    int max = elements.front();
    elements.pop_front();
    int new_solution = min(max + splits, solution);

    if (max < 4) return new_solution;

    for (int d = sqrt(max); d > 1; d--) {
        if (max % d == 0) {
            deque<int> new_elements;
            copy(elements.begin(), elements.end(), back_inserter(new_elements));
            fill_n(back_inserter(new_elements), d, max / d);

            new_solution = min(new_solution, recursive(new_elements, splits + d  - 1, new_solution));

            break;
        }
    }

    elements.push_back(max / 2);
    elements.push_back(max / 2 + max % 2);

    return recursive(elements, splits + 1, new_solution);
}

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int D;
        cin >> D;
        for (int i = 0; i < D; i++) {
            int x;
            cin >> x;
            elements.push_back(x);
        }

        int solution = recursive(elements, 0, numeric_limits<int>::max());

        cout << "Case #" << t << ": " << solution << endl;

        elements.clear();
    }

    return 0;
}
