//{{{
#define DEF
#ifdef DEF
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <functional>
#include <stack>
#include <vector>
#include <list>
#include <map>
#include <cctype>
#include <queue>
#include <cstring>
#include <cmath>
#include <set>
#include <deque>


//-----------------------------------------------------


using namespace std;
typedef unsigned int uint;
typedef long long int llint;
typedef unsigned long long int ullint;

typedef pair<int,int> Pii;
typedef pair<llint,llint> Pll;

#define mrepp(i,n,x)  for(int i = n-1; i >= x; i--)
#define mrep(i,n) mrepp(i,n,0)
#define repp(i,x,n)  for(int i = x; i < n; i++)
#define rep(i,n) repp(i,0,n)
#define pb        push_back
#define all(vec)  (vec).begin(),(vec).end()
#define each(i,c) for(__typeof((c).begin()) i=(c).begin();i!=(c).end();i++)
//#define reach(i,c) for(__typeof((c).rbegin()) i=(c).rbegin();i!=(c).rend();i++)
#define fst         first
#define scd         second

#define sz(v)     ((llint)(v).size())
//#define bit(n)    (1ll<<(li)(n))
//#define mkP        make_pair

//-----------------------------------------------------
#endif
//}}}

unsigned int fst_table[4][5];
unsigned int scd_table[4][5];
signed int test_num;
signed int fst_ans, scd_ans;
int match_num = 0;

int int_comp(const void *a, const void *b){
	if( *(int*)a < *(int*)b ){
		return -1;
	}else if( *(int*)a == *(int*)b ){
		return 0;
	}
	return 1;
}

int main(){
//#ifdef ONLINE_JUDGE
//    freopen("input.txt", "r", stdin);
//    freopen("output.txt", "w", stdout);
//#endif	
	//std::ios::sync_with_stdio();
	scanf("%d",&test_num);
	rep(n,test_num){
		scanf("%d",&fst_ans); fst_ans--;
		rep(i,4)rep(j,4) scanf("%d",&fst_table[i][j]);
		scanf("%d",&scd_ans); scd_ans--;
		rep(i,4)rep(j,4) scanf("%d",&scd_table[i][j]);
		
		qsort((void*)fst_table[fst_ans],4,sizeof(fst_table[0][0]),int_comp);
		qsort((void*)scd_table[scd_ans],4,sizeof(scd_table[0][0]),int_comp);
		
		//rep(i,4) cout << fst_table[fst_ans][i] << (i==3?'\n':' ');
		//rep(i,4) cout << scd_table[scd_ans][i] << (i==3?'\n':' ');
		
		unsigned int *fst_t = &fst_table[fst_ans][0];
		unsigned int *scd_t = &scd_table[scd_ans][0];
		match_num = 0;
		int ans;
		while( *fst_t ){
			while( *scd_t < *fst_t && *scd_t) scd_t++;
			if( *fst_t == *scd_t ){ match_num++; ans = *fst_t; }
			fst_t ++;
		}
		if( match_num == 0 ){
			printf("Case #%d: Volunteer cheated!\n",n+1);
		}else if( match_num == 1 ){
			printf("Case #%d: %d\n",n+1,ans);
		}else{
			printf("Case #%d: Bad magician!\n",n+1);
			
		}
	}
	
	return 0;
}
