#include "iostream"
#include "cstdio"
#include "queue"

using namespace std;
int ans[1000];
int ts ;
char s[1000];
vector<int> v[500];
int Q[1000];
//01010 10101 
int main(int argc, char const *argv[])
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	ans[1] = 1 ; v[1].push_back(2);
	for(int i = 2 ; i <= 100 ; ++ i)
		for(int j = 0 ; j <= 1 ; ++ j){
				v[2 * (i - 1) - (1 - j)].push_back(2 * i - j); 
				v[2 * i - (1 - j)].push_back(2 * i - j);
			}
	
	int fst = 0 , tail = 1 ; 
	Q[1] = 1 ; 
	while(fst < tail){
		int x = Q[++fst];
		for(int i = 0 ; i < v[x].size() ; ++ i)
			if(!ans[v[x][i]])
				ans[v[x][i]] = ans[x] + 1 , Q[++tail] = v[x][i];
	}

	cin >> ts ; 
	for(int T = 1 ; T <= ts ; ++ T){
		memset(s , 0 , sizeof s);
		scanf("%s",s);
		int cnt = 1 , L = strlen(s); 
		for(int i = 1 ; i < L ; ++ i) if(s[i] != s[i - 1]) cnt ++ ; 
		printf("Case #%d: %d\n",T,ans[2 * cnt - (s[0] == '+')] - 1);
	}
	return 0;
}
