#include <cstdio>
#include <vector>

using namespace std;


int cards1[4];
int cards2[4];

vector<int> ans;


int main()
{
	int testy; scanf("%d",&testy);
	
	for( int test = 0 ; test < testy ; test ++ )
	{
		ans.clear();
		int row1; scanf("%d",&row1);
		
		for( int i = 0 ; i < 4 ; i ++ )
		{
			for( int j = 0 ; j < 4 ; j ++ )
			{
				if( i == row1-1 ) {
					scanf("%d",&cards1[j]);
				}
				else {
					scanf("%*d");
				}
			}
		}
		
		int row2; scanf("%d",&row2);
		
		for( int i = 0 ; i < 4 ; i ++ )
		{
			for( int j = 0 ; j < 4 ; j ++ )
			{
				if( i == row2-1 ) {
					scanf("%d",&cards2[j]);
				}
				else {
					scanf("%*d");
				}
			}
		}
		
		for( int i = 0 ; i < 4 ; i ++ )
		{
			for( int j = 0 ; j < 4 ; j ++ )
			{
				if( cards1[i] == cards2[j] ) {
					ans.push_back(cards1[i]);
				}
			}
		}
		
		printf("Case #%d: ",test+1);
		
		if( ans.size() == 1 ) {
			printf("%d\n",ans[0]);
		}
		if( ans.size() == 0 ) {
			puts("Volunteer cheated!");
		}
		if( ans.size() > 1 ) {
			puts("Bad magician!");
		}
	}
	
	return 0;
}
	
	