#include <iostream>
#include <algorithm>
using namespace std;

int get_w_score();
int get_dw_score();
bool canget_dw_score(int n);

int N;
double a[1001];
double b[1001];

int get_w_score() {
	bool ken_used[1001];
	for (int i = 0; i < N; i++)
		ken_used[i] = false;
	// naomi plays each of hers
	// then, ken picks the smallest of his available to win
	// ... or if he knows he'll lose, pics the smallest he has
	int score = 0;
	for (int i = 0; i < N; i++)
	{
		bool ken_scored = false;
		for (int j = 0; j < N; j++)
			if (!ken_used[j] && b[j] > a[i]) {
				ken_used[j] = true;
				ken_scored = true;
				break;
			}
		if (!ken_scored) // need to use one
			for (int j = 0; j < N; j++)
				if (!ken_used[j]) {
					ken_used[j] = true;
					break;
				}
		if (!ken_scored)
			score++;
	}
	return score;
}

int get_dw_score() {
	for (int n = 0; n <= N; n++)
	{
		// see if we can match the largest n of a with the smallest n of b
		if (!canget_dw_score(n))
			return n - 1;
	}
	return N;
}

bool canget_dw_score(int n)
{
	for (int i = 0; i < n; i++)
	{
		if (b[i] > a[N-n+i])
			return false;
	}
	return true;
}

int main() {
	int ncases;
	cin >> ncases;
	for (int icase = 1; icase <= ncases; icase++) {
		cin >> N;
		for (int i = 0; i < N; i++)
			cin >> a[i];
		for (int i = 0; i < N; i++)
			cin >> b[i];
		sort(a, a + N);
		sort(b, b + N);	
		
		int w_score, dw_score;
		// get naomi's war score
		w_score = get_w_score();
		// get naomi's deceitful war score
		dw_score = get_dw_score();
		
		cout << "Case #" << icase << ": " << dw_score << " " << w_score << endl;
	}
	return 0;
}
