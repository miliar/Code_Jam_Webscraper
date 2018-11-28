#include<cstdio>
#include<algorithm>

using namespace std;

int A, B;
int T;
int CNT = 0;

bool table[1010];
int main(){
    scanf("%d", &T);	
	
	fill(table, table+1010, false);
    table[1] = table[4] = table[9] = table[121] = table[484] = true;
	while(T--){
		scanf("%d %d", &A, &B);
		int ans = 0;
	    for(int i = A; i <= B; ++i)	
		    if(table[i]) ans++;
		printf("Case #%d: %d\n", ++CNT, ans);
	}
}
