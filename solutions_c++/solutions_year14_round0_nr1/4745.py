#include<iostream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<vector> 
#include<cstring>
#include<string>
#define mp make_pair
#define scn second
#define frs first
#define pb push_back
#define NAME "a"
#define fop freopen(NAME ".in", "r", stdin); freopen(NAME ".out", "w", stdout); 
using namespace std;

typedef unsigned long long ull;
typedef long long ll;    	
typedef pair<int, int> pi;

void dout() { cerr << endl; }
template <typename Head, typename... Tail>
void dout(Head H, Tail... T) {
  cerr << H << ' ';
  dout(T...);
}

int arr[10000];
int tb[100][100];
int t, a;

int main(){
	#ifdef LocalHost
		fop;
	#endif
	scanf("%d", &t);
	int y = 1;
	while (t --> 0) {
	    for (int i = 1; i <= 16; ++i)
	    	arr[i] = 0;		
		scanf("%d", &a);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf("%d", &tb[i][j]);
		for (int i = 0; i < 4; ++i)
			++arr[tb[a - 1][i]];
		scanf("%d", &a);
		for (int i = 0; i < 4; ++i)
			for (int j = 0; j < 4; ++j)
				scanf("%d", &tb[i][j]);
		for (int i = 0; i < 4; ++i)
			++arr[tb[a - 1][i]];
		int cnt = 0, ans = 0;
		for (int i = 1; i <= 16; ++i) {
			if (arr[i] == 2)
				ans = i, ++cnt;
		}
		if (cnt == 1) 
			printf("Case #%d: %d\n", y, ans);
		if (cnt >= 2) 
			printf("Case #%d: Bad magician!\n", y);
		if (cnt == 0) 
			printf("Case #%d: Volunteer cheated!\n", y);				
		++y;
	}
		
	return 0;
}