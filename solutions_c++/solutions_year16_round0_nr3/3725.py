#include <iostream>
#include <fstream>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <list>
#include <cstdio>
#include <cstring>
#include <string>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <climits>
#include <ctime>

#define pb       	push_back
#define fi       	first
#define se       	second
#define inf		 	1000000000
#define SET(A,b) memset(A,b,sizeof (A) )
#define SIZE(A) ((int)(A).size())
#define yeral() (node *)calloc(1,sizeof(node))
#define dbg(x) cerr<<#x<<":"<<x<<endl

using namespace std;

typedef long long int lint;
typedef pair<int,int> ii;


lint mat[15][35];
int N,J;
int factor[15];
int main()
{
	//int steps = 0;
	freopen("oku.txt","r",stdin);
	freopen("yaz.txt","w",stdout);
	
	scanf("%d",&N);
	scanf("%d %d",&N,&J);
	printf("Case #1:\n");
	for(int i=2;i<=10;i++){
		mat[i][0] = 1;
		for(int j=1;j<N;j++)
			mat[i][j] = mat[i][j-1]*i;
	}
	
	for(int bit = 0;J && bit <=(1<<N) - 1; bit++){
		if(((bit&1) == 0) || ((bit & 1<<(N-1)) == 0))
			continue;
			
		//printf("%d %d\n",bit,bit&1);
		int passed = 0;
		for(int i = 2;i<=10;i++){
			lint sum = 0;
			
			factor[i] = 0;
			for(int j=0;j<N;j++){
				if(bit & (1<<j))
					sum += mat[i][j];
							
			}
			
			for(int j = 2;1ll*j*j<=sum;j++){
				if(sum%j == 0){
					factor[i] = j;
					passed++;
					break;
				}
			}
			//prime chech-erostan or O(sqrtN)
		}
		if(passed == 9){
			for(int i = N-1;i>=0;i--)
				printf("%d",bit&(1<<i) ? 1:0);
			for(int i=2;i<=10;i++)
				printf(" %d",factor[i]);
			puts("");
		
			J--;
		}
	
	}	
	
}
