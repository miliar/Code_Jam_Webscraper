#include <iostream>
#include <vector>
#include <set>
#include <thread>
#include <functional>
#include <algorithm>
#include <iterator>
#include <mutex>
#include <queue>
#include <string>
#include <cmath>


using namespace std;

typedef int ANS_TYPE;

vector<ANS_TYPE> ans;

class Solution
{
public:
    ANS_TYPE solve();
    ANS_TYPE brute();
    void read();
    void operator()() { ans[id] = solve(); }

    int id;

private:
    int D;
    priority_queue<int> P;
    vector<int> Pv;
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
    cin >> D;

    for(int i=0; i<D; ++i)
    {
	int Pi;
	cin >> Pi;
	
	Pv.push_back(Pi);
	P.push(Pi);
    }
}


void print(const priority_queue<int> & P)
{
    priority_queue<int> pc(P);
    
    while(!pc.empty())
    {
	cout << pc.top() << " ";
	pc.pop();
    }
    cout << endl;
}

ANS_TYPE Solution::solve()
{
    int best = 1000;

    for(int i=0; i<Pv.size(); ++i)
    {
	for(int split=1; split*split<=Pv[i]; ++split)
	{
	    int cnt = split-1;
	    int largest = static_cast<int>(ceil(static_cast<double>(Pv[i]) / split));

	    cnt += largest;
	    for(int j=0; j<Pv.size(); ++j)
	    {
		if(i == j)
		    continue;

		cnt += static_cast<int>(ceil(static_cast<double>(Pv[j]) / largest))-1;
	    }
	    
	    best = min(best, cnt);
	}
    }

    return best;
}

/*
ANS_TYPE Solution::solve()
{
    int best = P.top();

    int cur = 0;

    while(cur < best)
    {
	int m = P.top();
	P.pop();
	
	cur++;
	P.push(m/2);
	P.push(m - m/2);
 
	best = min(cur + P.top(), best);
    }

    return best;
}
*/

ANS_TYPE brute_solve(vector<int> & v, int depth)
{
    if(depth > 4)
	return 10000;

    int best = v[0];
    for(int i : v)
	best = max(i, best);

    for(int i=0; i<v.size(); ++i)
    {
	for(int j=1; j<=v[i]/2; ++j)
	{
	    v[i] -= j;
	    v.push_back(j);
	    best = min(best, 1 + brute_solve(v, depth+1));
	    v[i] += j;
	    v.pop_back();
	}
    }

    return best;
}


ANS_TYPE Solution::brute()
{
    priority_queue<int> pq(P);
    vector<int> v;
    while(!pq.empty())
    {
	v.push_back(pq.top());
	pq.pop();
    }

    return brute_solve(v, 0);
}

void single_main()
{
    int T;
    cin >> T;

    for(int i=1; i<=T; ++i)
    {
	Solution sol;
	sol.read();

	cout << "Case #" << i << ": " << sol.brute() << endl;
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
