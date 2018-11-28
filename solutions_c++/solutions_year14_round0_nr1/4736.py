#include <cstdio>
#include <map>

using namespace std;

map < int , int > hash ; 
int n = 4 ;
int s[6][6]  ;
int main(){
	int T , CASE = 0; 
	scanf("%d",&T); 
	
	while( T-- ){
		hash.clear(); 
		
		int row ; 
		scanf("%d",&row ); 
		for(int i=0;i<n;++i)
			for(int j=0;j<n;++j)
				scanf("%d",&s[i][j]) ; 
		
	
		for(int j=0;j<n;++j)
			hash[s[row-1][j]] = 1 ;
		
		scanf("%d",&row) ;
		for(int i=0;i<n;++i)
			for(int j=0;j<n;++j)
				scanf("%d",&s[i][j] );
				
		int cnt = 0 , ans = 0 ;	
		for(int j=0;j<n;++j){
			if( hash.find( s[row-1][j] ) != hash.end() ){
				ans = s[row-1][j] ;
				cnt++;	
			}
		}
		
		if( !cnt )	printf("Case #%d: Volunteer cheated!\n",++CASE);
		else if( cnt >= 2 )	printf("Case #%d: Bad magician!\n",++CASE);
		else	printf("Case #%d: %d\n",++CASE,ans);
		
	}
	
	return 0; 
}
