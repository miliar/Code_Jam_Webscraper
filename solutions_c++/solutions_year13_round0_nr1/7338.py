#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

string grid [4];
int dx[4]={1,1,-1,-1};
int dy[4]={1,-1,-1,1};

bool valid( int n ){
  return n >= 0 && n < 4 ;
}
bool check( int a  , int b , char c ){
   if( a >= 0 && b >= 0 ) grid[a][b] = c;
   for(int i = 0 ; i < 4 ; ++i ){
     if( grid[i].find( string(4,c) )!= -1 ) return true;
	 for(int j = 0 ; j < 4 ; ++j){
	   
	   int k;
	   for( k = 0 ; k < 4  && i + k < 4 && grid[ i + k ][ j ] == c ; ++k );
	   if( k == 4 ) return true;

       for(int w = 0 ; w < 4 ; ++w){
	     for( k = 0 ; k < 4  && valid ( i + dx[ w ] * k )  && valid(j + dy[ w ] * k)&& grid[ i + dx[w] * k ][ j + dy[w]*k ] == c ; ++k );
	     if( k == 4 ) return true;
	   }
	 } 
	 
   }
  return false;

}

int main(){
 int t;
 cin >> t;
 for( int i = 1  ; i <= t ; ++i ){
   bool completo = true ;
   char winner = 'W';
   int a = -1 , b = -1;
   cout << "Case #"<<i<<": ";
   for(int j = 0 ; j < 4 ; ++j)
   {	   cin>>grid[j];
   			completo = completo && grid[j].find(".") == -1;
            if( grid[j] .find("T") != -1)
				a = j , b = grid[j].find("T");
   }
   if( check( a , b , 'X') )
	   cout << "X won"<<endl;
   else if( check( a, b , 'O') )
	   cout << "O won"<<endl; 
   else if( !completo )
	   cout << "Game has not completed"<<endl;
   else cout << "Draw"<<endl;	   

 }

}
