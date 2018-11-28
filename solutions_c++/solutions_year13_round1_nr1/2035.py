#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;

unsigned long long solve(unsigned long long r, int t)
{
    int tmm = t;
    unsigned long long rings = 0;
    unsigned long long rad = r;

    while (tmm > 0) {        
        tmm -= (2 * rad + 1);

        if (tmm < 0) {
            break;
        }
        
        rad += 2;
        rings++;
    }

    return rings;
}


int main()
{
    FILE *fp = fopen("prob_small.in", "r");  
    
    bool special = false;
	int /*r, t,*/ testcase;
    unsigned long long r, t;
    fscanf(fp, "%d\n", &testcase);


	for (int caseId = 1; caseId <= testcase; caseId++)
	{
        fscanf(fp, "%d", &r);
        fscanf(fp, "%d", &t);

        unsigned long long rings = solve(r, t);

        printf("Case #%d: %d\n", caseId, rings);

        fscanf(fp, "\n");
	}
	return 0;
}
