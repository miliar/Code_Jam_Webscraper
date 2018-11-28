#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>

using namespace std;


int main(int argc, char *argv[]) {
	int ecase, ecount;
	int caseStart = -1, caseEnd = 9999999;
	scanf("%d", &ecase);

	if (argc > 1) {
		if (sscanf(argv[1], "%d", &caseStart) == 1) {
			if (argc > 2)
				sscanf(argv[2], "%d", &caseEnd);
		}
		if (caseEnd < caseStart)
			caseEnd = caseStart;
		if (caseEnd != 9999999 && caseEnd >= 1 && caseStart <= 0)
			caseStart = 1;
		if (caseStart > 0)
			fprintf(stderr, "....................DEBUG MODE ENABLED (FROM CASE %d to %d)\n", caseStart, caseEnd);
	}

	char line[20000];
	int ans;
	int en;
	char flags[100000];
	vector<int> tokens[200];

	for (ecount = 1; ecount <= ecase; ecount++) {
		if (ecount < caseStart || ecount > caseEnd)
			continue;
	
		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d START\n", ecount);

		scanf("%d", &en);
		map<string, int> strIdx;
		int snum = 0;
		gets(line);
		for (int i = 0; i < en; i++) {
			tokens[i].resize(0);
			gets(line);
			string s(line);
			istringstream iss(s);
			do
			{
				string sub;
				iss >> sub;
				if (strIdx.find(sub) == strIdx.end())
					strIdx[sub] = snum++;
				tokens[i].push_back( strIdx[sub] );
			} while (iss);
			//for (int j = 0; j < tokens[i].size(); j++)
			//	printf("%d ", tokens[i][j]);
			//printf("\n");
		}

		ans = 1000000;

		int upbound = (1 << en);
		for (int i = 2; i < upbound; i+=4) {
			for (int j = 0; j < snum; j++)
				flags[j] = 0;
			for (int j = 0; j < en; j++) {
				int tf;
				if (i & (1 << j))
					tf = 1;
				else
					tf = 2;
				for (int k = 0; k < tokens[j].size(); k++)
					flags[ tokens[j][k] ] |= tf;
			}
			int tcnt = 0;
			for (int j = 0; j < snum; j++)
				if (flags[j] == 3)
					tcnt++;
			if (tcnt < ans)
				ans = tcnt;
		}

		printf("Case #%d: %d\n", ecount, ans-1);
		
		if (caseStart > 0)
			fprintf(stderr, "....................CASE %d END\n", ecount);
	}

	return 0;
}
