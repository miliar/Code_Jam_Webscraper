#include <cstdlib>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
vector<int> motes;
vector<bool> used;
int A, N;
		
int find_sol(int steps, int next)
{
	// cout << "*" <<  next << endl;
	//if (steps >= max_steps) return steps + max_steps;
	if (next >= N) return steps;
	if (A > motes[next])
	{
		// cout <<steps << " - " << A << " EAT " << motes[next] << " => ";
		A += motes[next];
		// cout << A << endl;
		return min(steps + N - next, find_sol(steps, next+1));
	}

	// cout<<steps << " - "  << A << " MUST ADD  =>" << 2*A-1 << endl;

	A += A -1;
	return min(steps + N - next, find_sol(steps +1, next));
}

int main(int argc, char *argv[])
{
	int T;
	cin >> T;
	int t = 1;
	while (t <= T){

		cin >> A >> N;
		motes = vector<int>(N);
		used = vector<bool>(N, false);
		for (int i = 0; i < N; ++i)
		{
			cin >> motes[i];
		}
		sort(motes.begin(), motes.end());
		/*for (int i = 0; i < N; ++i)
		{
			cout << motes[i] << ' ';
		}
		cout << endl;*/
		
		
		int steps;
		if (A == 1) steps = N;
		else steps = min(N,find_sol(0, 0));


		cout << "Case #" << t << ": "  << steps;
		
		cout << endl;

		t++;
	}
    return 0;
}


