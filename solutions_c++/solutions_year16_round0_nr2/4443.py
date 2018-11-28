#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<map>
#include<set>
#include<queue>
#include<stack>
#include<functional>
#include<algorithm>
#include<utility>
#define PB push_back
#define MP make_pair
#define _F first
#define _S second

using namespace std;

char str[1000];

int main(int argc, char* argv[]){
	int T;
	scanf("%d", &T);
	for(int i = 1; i <= T; i++){
		printf("Case #%d: ", i);
		scanf("%s", str);
		int len = strlen(str);
		int cnt = 1;
		char now = str[0];
		char start = str[0];
		for(int j = 1; j < len; j++){
		   if(str[j] == now)
			   continue;
		   now = str[j];
		   cnt++;
		}
		if(now == '+')
			cnt--;
		printf("%d\n", cnt);
	} 
    return 0;
}
