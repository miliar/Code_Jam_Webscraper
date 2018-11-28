#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <vector>
#include <algorithm>
#include <climits>
#include <cmath>

using namespace std;
#define MAX_SIZE 1000
int naomi[MAX_SIZE];
int ken[MAX_SIZE];

int main(int argc, const char *argv[])
{
	int caseNr;
	int caseId;
	scanf("%d", &caseNr);
	for (caseId=0; caseId<caseNr; caseId++) {
		int n,i;
		int score_war = 0;
		int score_dwar = 0;
		scanf("%d", &n);
		//printf("naomi:");
		for (i=0; i<n; i++) {
			float v;
			scanf("%f", &v);
			naomi[i] = (int)(v*100000);
			//printf("%d ", naomi[i]);
		}
		//printf("\n");
		sort(naomi, naomi+n);
		//printf("ken:");
		for (i=0; i<n; i++) {
			float v;
			scanf("%f", &v);
			ken[i] = (int)(v*100000);
			//printf("%d ", ken[i]);
		}
		//printf("\n");

		// compute score in normal war
		vector<int> vec_ken1(ken, ken+n);
		sort(vec_ken1.begin(), vec_ken1.end());
		for (i=0; i<n; i++) {
			vector<int>::iterator it;
			it = upper_bound(vec_ken1.begin(), vec_ken1.end(), naomi[i]);
			if (it == vec_ken1.end()) {
				score_war++;
				vec_ken1.erase(vec_ken1.begin());
			} else {
				vec_ken1.erase(it);
			}
		}

		// compute score in decetful war
		vector<int> vec_ken2(ken, ken+n);
		sort(vec_ken2.begin(), vec_ken2.end());
		for (i=0; i<n; i++) {
			/*
			vector<int>::iterator it;
			it = upper_bound(vec_ken2.begin(), vec_ken2.end(), naomi[i]);
			if (it == vec_ken2.end()) {
				score_dwar++;
				vec_ken2.erase(vec_ken2.begin());
			} else {
				vec_ken2.pop_back();
			}
			*/
			if (naomi[i] > vec_ken2.front()) {
				score_dwar++;
				vec_ken2.erase(vec_ken2.begin());
			} else {
				vec_ken2.pop_back();
			}
		}
		printf("Case #%d: %d %d\n", caseId+1, score_dwar, score_war);
	}
	return 0;
}
