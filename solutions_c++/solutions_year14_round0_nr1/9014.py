#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdio>
#include <vector>

#define FOR(a,b,c) for(int (a)=(b);(a)<=(c);(a)++)
#define FORT(a,b,c) for(int (a)=(b);(a)>=(c);(a)--)
#define SIZE(A) ((int)(A).size())

using namespace std;

typedef double dbl;
typedef long long Lint;
typedef pair<int,int> ii;
typedef pair<Lint,Lint> Lii;

const Lint mod = 1e9;

const int MAXN = 200010;

int used[20];

int main(){
	
	int T,ans,tmp;

	scanf(" %d",&T);
	
	vector<int> res;
	
	FOR(test,1,T){
		
		memset(used,0,sizeof used);
		res.clear();
		
		FOR(step,1,2){
			scanf(" %d",&ans);		
			FOR(i,1,4)
				FOR(j,1,4)
				{
					scanf(" %d",&tmp);
					if(i==ans)
						used[tmp]++;
				}
		}
		
		FOR(i,1,16)
			if( used[i]==2 )
				res.push_back(i);
		
		if(SIZE(res)==0)	printf("Case #%d: Volunteer cheated!\n",test);
		if(SIZE(res)>1)		printf("Case #%d: Bad magician!\n",test);
		if(SIZE(res)==1)	printf("Case #%d: %d\n",test,res[0]);
		
	}
	
	return 0;
	
}
