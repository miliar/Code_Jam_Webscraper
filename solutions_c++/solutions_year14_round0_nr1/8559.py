#include <iostream>
#include <stdio.h>
#include <vector>
using namespace std;

int a[2][4][4];
int commonElement(int row[2]){
	int v[17],i,j;
	for(i = 0; i < 17; i++)
		v[i] = 0;
	for(i = 0; i < 2; i++){
		for(j = 0; j < 4; j ++)
			v[a[i][row[i]][j]]++;
	}
	vector<int> solution;
	for(i = 0; i < 17; i++){
		if(v[i] > 1)
			solution.push_back(i);

	}
	if(solution.size() > 1)
		return 0;
	if(solution.size() == 1)
		return solution.front();
	else
		return -1;
}
void read(){
	int t,row[2];
	scanf("%d",&t);
	for(int i = 0; i < t; i++){
		for(int l = 0; l < 2; l++){
			scanf("%d",&row[l]);
			--row[l];
			for(int j = 0; j < 4; j++)
				for(int k = 0; k < 4; k++)
					scanf("%d",&a[l][j][k]);
		}
		int sol = commonElement(row);
		if(sol == 0)
			printf("Case #%d: ",i + 1),printf("Bad magician!\n");
		else
		if(sol == -1)
			printf("Case #%d: ",i + 1),printf("Volunteer cheated!\n");
		else printf("Case #%d: %d\n",i + 1,sol);
	}

}
int main(){
	freopen("f.txt","r",stdin);
	freopen("fout.txt","w",stdout);
	read();
	return 0;
}
