#include <iostream>
#include <vector>

using namespace std;

bool isPossible(vector<vector<int> > pattern) {
    int N = pattern.size();
    int M = pattern[0].size();

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            bool decLeft = true;
            bool decRight = true;
            bool decUp = true;
            bool decDown = true;

            for (int k = 0; k < j; k++)
                if (pattern[i][k] > pattern[i][j])
                    decLeft = false;
            for (int k = j + 1; k < M; k++)
                if (pattern[i][k] > pattern[i][j])
                    decRight = false;
            for (int k = 0; k < i; k++)
                if (pattern[k][j] > pattern[i][j])
                    decUp = false;
            for (int k = i + 1; k < N; k++)
                if (pattern[k][j] > pattern[i][j])
                    decDown = false;

            bool valid = (decLeft && decRight) || (decUp && decDown);
            if (!valid)
                return false;
        }
    }

    return true;
}

int main() {
    int T, N, M, temp;
    cin >> T;

    for (int i = 1; i <= T; i++) {
        cin >> N >> M;

        vector<vector<int> > pattern;
        for (int j = 0; j < N; j++) {
            vector<int> line;
            for (int k = 0; k < M; k++) {
                cin >> temp;
                line.push_back(temp);
            }
            pattern.push_back(line);
        }

        cout << "Case #" << i << ": "
             << (isPossible(pattern) ? "YES" : "NO") << endl;
    }

    return 0;
}
