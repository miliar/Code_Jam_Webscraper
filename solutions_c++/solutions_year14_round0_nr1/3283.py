#include <bits/stdc++.h>
using namespace std;
int ntc, r, tmp;
int main(){
	scanf("%i", &ntc);
	for(int tc=1;tc<=ntc;tc++){
		set<int> s;
		scanf("%i", &r);
		for(int i=1;i<=4;i++){
			for(int j=0;j<4;j++){
				scanf("%i", &tmp);
				if(i == r) s.insert(tmp);
			}
		}
		vector<int> match;
		scanf("%i", &r);
		for(int i=1;i<=4;i++){
			for(int j=0;j<4;j++){
				scanf("%i", &tmp);
				if(i == r && s.find(tmp) != s.end()) match.push_back(tmp);
			}
		}
		printf("Case #%i: ", tc);
		if(match.size() == 0) printf("Volunteer cheated!\n");
		else if (match.size() == 1) printf("%i\n", match[0]);
		else printf("Bad magician!\n");
	}
}