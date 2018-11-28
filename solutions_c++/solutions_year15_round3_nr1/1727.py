#include <bits/stdc++.h>
using namespace std;
#define print_out(x) cout << "print_out: " << #x << " == " << x << endl;
#define sz(x) int((x).size())
#define pb(x) push_back(x)
#define mkp(a, b) make_pair(a, b)
#define F first
#define S second
#define whole(a) a.begin(), a.end()
#define FOR(i, S, N) for (int i = S; i < N; ++i)
#define contains(C, key) (C.find(key) != C.end())
typedef vector<int> VInt;
typedef vector<VInt> VVInt;
typedef pair<int, int> PII;
typedef long long int int64;
typedef unsigned int uint;


ifstream in("input.txt");
ofstream out("output.txt");

struct Solution
{
    int test_case_number;

    // input:
    int R, C, W;

    // output:
    int ans;

    // Solution procedures
    void solve()
    {
        int beg = C - W;

        ans = 0;
        int cur = W;
        while (cur < beg)
            ++ans, cur += W;
        cur -= W;

        if ((C - cur) - W > 0)
            ++ans;

        ans += W;
    }

    // Read & Write
    void read()
    {
        in >> R >> C >> W;
    }

    void write()
    {
        out << "Case #" << test_case_number << ": ";

        out << ans << "\n";
    }
};

int main()
{
    std::ios::sync_with_stdio(false);

    const int CORES_AMOUNT = 8;
    vector<Solution> sols(CORES_AMOUNT);
    vector<std::thread> threads(CORES_AMOUNT);
    vector<bool> launched(CORES_AMOUNT);

    int T;
    in >> T;
    cout << "Amount of test cases (T) = " << T << endl;

    int j = 0; // current thread / solution / launched array cell
    int i = 1; // current smallest unread test case number
    int solved = 0; // amount of solved cases
    for(;; ++i)
    {
        // wait until thread execution finishes and write answer
        if (launched[j])
        {
            threads[j].join();
            launched[j] = false;

            sols[j].write();
            cout << "Solved " << sols[j].test_case_number << " / " << T << endl;

            if (++solved == T)
                break;
        }

        if (i <= T)
        {
            // read new test case
            sols[j] = Solution();
            sols[j].test_case_number = i;
            sols[j].read();

            // launch thread
            threads[j] = std::thread(&Solution::solve, std::ref(sols[j]));
            launched[j] = true;
        }

        j = (j + 1) % CORES_AMOUNT;
    }

    cout << "Execution finished. Good luck!" << endl;
    return 0;
}

