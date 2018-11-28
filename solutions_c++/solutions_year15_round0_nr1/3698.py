#include <iostream>
#include <vector>
#include <set>
#include <thread>
#include <functional>
#include <algorithm>
#include <iterator>
#include <mutex>

using namespace std;

typedef int ANS_TYPE;

vector<ANS_TYPE> ans;

class Solution
{
public:
    ANS_TYPE solve();
    void read();
    void operator()() { ans[id] = solve(); }

    int id;

private:
    vector<int> S;
    int Smax;
};

void single_main();
void multi_main();

int main()
{
    multi_main();

    return 0;
}


void Solution::read()
{
    cin >> Smax;

    string s;
    cin >> s;
    for(int i=0; i<=Smax; ++i)
    {
	S.push_back(static_cast<int>(s[i] - '0'));
    }
}

ANS_TYPE Solution::solve()
{
    int needed = 0;
    int d = S[0];
    for(int i=1; i<=Smax; ++i)
    {
	if(S[i] > 0 && d < i)
	{
	    needed += (i - d);
	    d += (i - d);
	}

	d += S[i];
    }

    return needed;
}


void single_main()
{
    int T;
    cin >> T;

    for(int i=1; i<=T; ++i)
    {
	Solution sol;
	sol.read();
	cout << "Case #" << i << ": " << sol.solve() << endl;
    }
}

void multi_main()
{
    int T;
    cin >> T;

    ans.resize(T+1);

    vector<thread> threads;
    vector<Solution> solutions(T+1);
    for(int i=1; i<=T; ++i)
    {
        Solution & sol = solutions[i];
	sol.id = i;
	sol.read();
	threads.push_back(thread(ref(sol)));
    }

    for(auto &t: threads)
    {
	t.join();
    }

    for(int i=1; i<=T; ++i)
    {
	cout << "Case #" << i << ": " << ans[i] << endl;
    }
}
