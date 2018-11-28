// by eopXD
#include <cstdio>
#include <cstring>
#include <algorithm>
#define SZ(x) (int)((x).size())
using namespace std;
typedef long long LL;
#include <vector>
int main ()
{
  freopen("A.in","r",stdin);
  freopen("A.out","w",stdout);
	int t; scanf("%d",&t);
	for ( int c=1; c<=t; c++ ) {
		int app[17]={};
		for ( int q=0; q<2; q++ ) {
			int r; scanf("%d",&r);
			for ( int i=1; i<=4; i++ ) 
				for ( int j=0; j<4; j++ ) {
					int x; scanf("%d",&x);
					if ( i==r ) app[x]++;	
				}
		}	
		vector<int> ans;
		for ( int i=1; i<=16; i++ ) if ( app[i]>1 ) ans.push_back(i);
		printf("Case #%d: ",c);
		if ( SZ(ans)==1 ) printf("%d\n",ans[0]);
		else if ( SZ(ans)==0 ) puts("Volunteer cheated!");
		else puts("Bad magician!");
	}
//  fclose(stdin);
//  fclose(stdout);
//  system("pause");
    return 0;
}
//---------------------------------------
