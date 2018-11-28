#include <algorithm>
#include <cstdio>
#include <set>
#include <vector>
using namespace std;


int evil_score(const vector<double>& naomi, const vector<double>& ken)
{
	int score = 0;
	
	for (int i = 0, ken_first = 0; i < (int)naomi.size(); i++)
		if (naomi[i] > ken[ken_first])
		{
			score++;
			ken_first++;
		}
	
	return score;
}


int war_score(const vector<double>& naomi, const vector<double>& ken)
{
	int score = 0;
	set<double> ken_set(ken.begin(), ken.end());
	
	for (int i = 0; i < (int)naomi.size(); i++)
	{
		set<double>::iterator it = ken_set.lower_bound(naomi[i]);
		if (it == ken_set.end())
		{
			score++;
			ken_set.erase(ken_set.begin());
		}
		else ken_set.erase(it);
	}
	
	return score;
}


void solve_case(int test_case)
{
	int N; scanf("%d", &N);
	vector<double> naomi(N), ken(N);
	for (int i = 0; i < N; i++)
		scanf("%lf", &naomi[i]);
	for (int i = 0; i < N; i++)
		scanf("%lf", &ken[i]);
		
	sort(naomi.begin(), naomi.end());
	sort(ken.begin(), ken.end());
	
	printf("Case #%d: %d %d\n", 
		   test_case, evil_score(naomi, ken), war_score(naomi, ken));
}


int main()
{
	int T; scanf("%d", &T);
	for (int t = 1; t <= T; t++)
		solve_case(t);
		
	return 0;
}