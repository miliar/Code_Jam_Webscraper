#include <bits/stdc++.h>

using namespace std;

#define INF 1<<30
#define MOD 1000000007
typedef long long ll;
#define fori(i, ini, lim) for(int i= int(ini); i<(int)lim; ++i)
#define ford(i, ini, lim) for(int i= int(ini); i>=(int)lim; --i)

using ii = pair<int, int>;

int main(){

	int t; scanf("%d ", &t);
	int cases = 1;
	while(t--){
		int sum = 0;
		priority_queue<ii> v;
		int n; scanf("%d ", &n);
		fori(i,0,n){
			int n1; scanf("%d ", &n1);
			v.push(ii(n1,-i));
			sum += n1;
		}
		int c = 0;
		if(!(sum&1)) c= -1;
		printf("Case #%d: ", cases++);
		while(!v.empty()){
			ii cur = v.top(); v.pop();
			cur.first--;
			if(cur.first > 0) v.push(cur);
			if(c>0 && (c&1))printf(" ");
			c++;
			printf("%c", (char)((-cur.second) + 'A'));
		}
		printf("\n");
	}

	return 0;
}
