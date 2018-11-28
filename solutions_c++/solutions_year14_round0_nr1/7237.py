#include<cstdio>
#include<iostream>
#include<vector>
#include<map>
using namespace std;

int main(){
	int T;
	int a, b;
	int A[4][4], B[4][4];
	
	int count;
	int x;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++){
		//printf("hello\n");
		scanf("%d", &a);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				scanf("%d", &A[i][j]);
			
		scanf("%d", &b);
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
				scanf("%d", &B[i][j]);
map<int, bool> ans;
		for(int i = 0; i < 4; i++)
			ans[A[a-1][i]] = true;
		
		count = 0;
		
		for(int i = 0; i < 4; i++)
			if(ans.find(B[b-1][i]) != ans.end()){
				count++;
				x = B[b-1][i];
			}

		if(count == 1)
			printf("Case #%d: %d\n", t, x);
		if( count == 0)
			printf("Case #%d: Volunteer Cheated!\n", t);
		if(count > 1)
			printf("Case #%d: Bad Magician!\n", t);
	}
	return 0;
}