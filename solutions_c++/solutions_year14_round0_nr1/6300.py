#include <cstdio>
#include <cmath>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <set>

using namespace std;

#define all(c) (c).begin(),(c).end() 
#define sz(c) int((c).size())
#define pb push_back
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define rep(i,x,y) for(int i = x; i < y; i++)

typedef long long int LL;
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii;
typedef vector<ii> vii;

int a[17],b[17],fi[5][5],se[5][5];
int main()
{
	int t;
	scanf("%d",&t);
	rep(k,1,t+1){
		int x,y;
		scanf("%d",&x);
		rep(i,1,5) 
		rep(j,1,5){
			scanf("%d",&fi[i][j]);
			a[fi[i][j]]=i;
		}
		scanf("%d",&y);
		int ch[5] = {0};
		rep(i,1,5) 
		rep(j,1,5){
			scanf("%d",&se[i][j]);
			b[se[i][j]]=i;
		}
		rep(i,1,5) ch[b[fi[x][i]]]++;
		if(ch[y] == 1){
			rep(i,1,5)
				if(a[se[y][i]] == x){printf("Case #%d: %d\n",k,se[y][i]); break;}
		}
		else if(ch[y] == 0)
			printf("Case #%d: Volunteer cheated!\n",k);
		else printf("Case #%d: Bad magician!\n",k);
	}
	return 0;
}