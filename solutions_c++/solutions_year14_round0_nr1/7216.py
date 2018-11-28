#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstring>
#include <iterator>
#include <map>
#include <bitset>
#include <set>

using namespace std;

#define inf 200000000
#define neginf -20000000
#define PB push_back
#define pb pop_back
#define MK make_pair

typedef vector<int> vi;
typedef pair<int, int> ii;
typedef long long ll;
typedef vector<vi> vvi;
typedef vector<ii> vii;

int a, b, tab[4][4], bat[4][4];

int main(){
int T; scanf("%d", &T);
	for(int t = 1; t <= T; ++t){
	
		printf("Case #%d: ", t);
		
		set<int> s;
		
		scanf("%d", &a);
		for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; ++j)	scanf("%d", &tab[i][j]);
		
		
		scanf("%d", &b);
		for(int i = 0; i < 4; ++i) for(int j = 0; j < 4; ++j)	scanf("%d", &bat[i][j]);
		
		for(int i = 0; i < 4; ++i) s.insert(tab[a-1][i]);
		
		int c = 0, ans;
		for(int i = 0; i < 4; ++i)
			if(s.find(bat[b-1][i]) != s.end())
				ans = c ? ans : bat[b-1][i], c++;
		
		if(c == 1) printf("%d\n", ans);
		else if(c > 1) printf("Bad magician!\n");
		else printf("Volunteer cheated!\n");
	}
return 0;
}
