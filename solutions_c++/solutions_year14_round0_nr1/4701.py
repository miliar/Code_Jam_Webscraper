#include <bits/stdc++.h>

using namespace std;

int main()
{
	int Tnum;
	
	scanf("%d", &Tnum);
	
	for (int T = 1; T <= Tnum; T++){
		int r1, r2;
		vector<int> v;
		vector<int> cand;
		
		scanf("%d", &r1);
		--r1;
		for (int i = 0; i < 16; i++){
				scanf("%d", &r2);
				if (r1 * 4 <= i && i < r1 * 4 + 4) v.push_back(r2);
		}
		
		scanf("%d", &r2);
		--r2;
		
		for (int i = 0; i < 16; i++){
			scanf("%d", &r1);
			if (r2 * 4 <= i && i < r2 * 4 + 4){
				for (int j = 0; j < 4; j++) if (v[j] == r1) cand.push_back(v[j]);
			}
		}
		
		printf("Case #%d: ", T);
		if (cand.size() == 1) printf("%d\n", cand[0]);
		else if (cand.size() == 0) printf("Volunteer cheated!\n");
		else printf("Bad magician!\n");
		
	}
	
	return (0);
}