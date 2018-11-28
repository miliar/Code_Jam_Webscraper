#include <bits/stdc++.h>


using namespace std;

const string number[10] = {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
char t_number[10] = {'Z','O','T','H','U','F','X','S','G','I'};
/*

0 -> 4 -> 6 -> 8 -> 3 -> 2 -> 5 -> 7 -> 1 -> 9

*/
int letter[300] ;
char buffer[2500];
set < char > sp;
vector < int > out;
vector < int > f;

int main(int argc,char *argv[]){
	//freopen( "in.txt" , "r" , stdin );
	//freopen( "out.txt" , "w" , stdout );
	int Case , cas = 0;
	scanf("%d",&Case);
	f.push_back( 0 );
	f.push_back( 4 );
	f.push_back( 6 );
	f.push_back( 8 );
	f.push_back( 3 );
	f.push_back( 2 );
	f.push_back( 5 );
	f.push_back( 7 );
	f.push_back( 1 );
	f.push_back( 9 );
	while(Case--){
		memset( letter , 0 ,  sizeof( letter) );
		scanf("%s",buffer);
		int len = strlen( buffer );
		for( int i = 0 ; i < len ; ++ i) letter[buffer[i]] ++ ;
		out.clear();
		for(int i = 0 ; i < 10 ; ++ i){
			int sx = f[i];
			int K = letter[t_number[sx]];
			for(int j = 0 ; j < K ; ++ j) out.push_back( sx );
			for( auto it : number[sx] ) letter[it] -= K;
		}
		printf("Case #%d: ",++cas);
		sort( out.begin() , out.end() );
		for( auto it : out ) printf("%d",it);
		printf("\n");
	}
	return 0;
}