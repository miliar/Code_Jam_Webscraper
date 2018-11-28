#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>

using namespace std;

int t,i,j;
char s[105],s1[105];

bool check(int r){
	bool flag = 1;
	for(int k = 0; k < r; k++)
	flag &= (s[k] == '+');
	return flag;
}

void solve(int r){
	int ind = 0;
	char temp = s[0];
	for(j = 1; j < r; j++){
		if(s[j] != temp) break;
		ind = j;
	}
	for(int k = 0; k <= ind; k++){
		char temp = s[ind - k];
		if(temp == '+')
		temp = '-';
		else
		temp = '+';
		s1[k] = temp;
	}
	for(int k = 0; k <= ind; k++)
	s[k] = s1[k];
}

int main(){
	scanf("%d", &t);
	int testcase = 0;
	
	while(++testcase <= t){
		memset(s, 0, sizeof(s));
		scanf("%s", s);		
		int l = strlen(s);
		int ans = 0;
		
		while(!check(l)){
			ans++;
			solve(l);
		}
		
		printf("Case #%d: %d\n", testcase, ans);
	}
}

