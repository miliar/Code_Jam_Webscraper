#include <stdio.h>
#include <stdlib.h>
#include <stack>
#include <string.h>

#define MAX 1024

int DP[500][5] = {{0}};
using namespace std;

int check(stack<char>& s)
{
	if(s.size() == 1){
		if(s.top() == '+')
			return 0;
		else return 1;
	}

	return -1;
}

void solve()
{

	DP[1][0] = 1;
	DP[1][1] = 0;

	for(int i = 2; i < 101; i++){
		if(i % 2 == 0){
			DP[i][0] = DP[i-1][0];
			DP[i][1] = DP[i-1][1] + 2;
		}
		else{
			DP[i][0] = DP[i-1][0] + 2;
			DP[i][1] = DP[i-1][1];
		}
	}
}

int main()
{
	int T;
	scanf("%d", &T);

	solve();
	// printf("xx=%d\n", DP[2][0]);
	for(int i = 0; i < T; i++){
		char str[MAX];
		scanf("%s", str);
		stack <char> s;
		int len = strlen(str);
		s.push(str[0]);
		for(int j = 1; j < len; j++){
			if(s.top() != str[j])
				s.push(str[j]);
		}

		if(str[0] == '+')
			printf("Case #%d: %d\n", i+1, DP[s.size()][1]);
		else printf("Case #%d: %d\n", i+1, DP[s.size()][0]);
	}

	return 0;
}
