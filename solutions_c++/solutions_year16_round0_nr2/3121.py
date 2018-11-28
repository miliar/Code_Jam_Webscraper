#include <iostream>
#include <string>

using namespace std;
int solution[100];

int solve(string& problem)
{
    int i, j;
    int n = 0;
    for(i = problem.length() - 1; i >= 0; --i) {
        if(problem[i] == '-') {
            for(j = 0; j <= i; ++j)
                problem[j] = (problem[j] == '+') ? '-' : '+';
            n++;
        }
    }
    return n;
}

int main(void)
{
    int T;
    cin >> T;

    for(int i = 1; i <= T; ++i) {
        string problem;
        cin >> problem;
        int answer = solve(problem);
        cout << "Case #" << i << ": " << answer << endl;
    }

    return 0;
}

