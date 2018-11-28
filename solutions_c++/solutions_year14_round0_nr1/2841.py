#include <bits/stdc++.h>
using namespace std;
int a[5][5];
int n = 4;
int d[20];
int main(){
	int test;
	freopen("file.out","w",stdout);
	scanf("%d",&test); 
	for(int num = 1; num<=test; ++num){
		set<int> ans; int k;
		memset(d , 0 , sizeof d);
		scanf("%d",&k);
		for(int i = 1; i <= 4; ++i)
		for(int j = 1; j <= 4; ++j) scanf("%d",&a[i][j]);
		for(int j = 1; j <= 4; ++j) d[a[k][j]]++;
		
		scanf("%d",&k);
		for(int i = 1; i <= 4; ++i)
		for(int j = 1; j <= 4; ++j) scanf("%d",&a[i][j]);		
		for(int j = 1; j <= 4; ++j) d[a[k][j]]++;
		
		for(int i = 1; i <= 16; ++i) if (d[i] == 2) ans.insert(i);
		
		printf("Case #%d: ",num);
		if (ans.empty()) printf("Volunteer cheated!\n"); 
		else if (ans.size() > 1) printf("Bad magician!\n");
		else printf("%d\n",*ans.begin());
	
	}

}