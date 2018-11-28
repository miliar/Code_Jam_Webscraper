#include<cstdio>
#include<set>
#include<vector>

using namespace std;

int tab[2][5][5], row[2];

void calc(int testCase) {
	for(int i = 0; i<2; i++) {
		scanf("%d", row+i);
		for(int j = 1; j<=4; j++)
			for(int k = 1; k<=4; k++)
				scanf("%d", &tab[i][j][k]);
	}
	set<int> wier;
	vector<int> out;
	for(int i =1; i<=4; i++)
		wier.insert(tab[0][row[0]][i]);
	for(int i = 1; i<=4; i++)
		if(wier.count(tab[1][row[1]][i])!=0)
			out.push_back(tab[1][row[1]][i]);
	printf("Case #%d: ", testCase);
	if(out.size() > 1)
		printf("Bad magician!\n");
	if(out.size() == 1)
		printf("%d\n", out[0]);
	if(out.size()  < 1)
		printf("Volunteer cheated!\n");
}

int main(){
	int T;
	scanf("%d", &T);
	for(int i = 1; i<=T; i++){
		calc(i);
	}
	return 0;
}

