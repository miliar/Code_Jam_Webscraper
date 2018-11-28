#include "stdio.h"
#include "string.h"
#include "vector"
#include "algorithm"

using namespace std;

const int MAX_N = 510;
const int INF = 1000000000;

struct edge { int to, cap, rev_index; };

vector<edge> G[2*MAX_N*MAX_N];
bool used[2*MAX_N*MAX_N];


void add_edge(int from, int to){
  G[from].push_back((edge){to, 1, G[to].size()});
  G[to].push_back((edge){from, 0, G[from].size() - 1});
}

int dfs(int v, int t, int f){
  if(v == t) return f;
  used[v] = true;
  for(int i = 0; i < G[v].size(); i++){
    edge &e = G[v][i];
    if(!used[e.to] && e.cap > 0){
      int d = dfs(e.to, t, min(f, e.cap));
      if(d > 0){
        e.cap -= d;
        G[e.to][e.rev_index].cap += d;
        return d;
      }
    }
  }
  return 0;
}

int max_flow(int s, int t){
  int flow = 0;
  while(true){
    memset(used, 0, sizeof(used));
    int f = dfs(s, t, INF);
    if(f == 0) return flow;
    flow += f;
  }
}


int field[MAX_N][MAX_N];

int w , h , b;
int noden( int x , int y ){
  return 2*(x*max(w,h)+y);
}

int main(){

  /*  
  add_edge( 0 , 3 );
  add_edge( 0 , 1 );
  add_edge( 1 , 4 );
  add_edge( 3 , 4 );
  add_edge( 4 , 7 );
  add_edge( 4 , 5 );
  add_edge( 5 , 8 );
  add_edge( 7 , 8 );
  add_edge( 11 , 0 );
  add_edge( 11 , 3 );
  add_edge( 10 , 5 );
  add_edge( 10 , 8 );

  printf( "%d\n" , max_flow( 10 , 11 ) );

  return 0;
  
  */

  int t;
  scanf( "%d" , &t );

  for( int tc = 1; tc <= t; tc++ ){

    scanf( "%d %d %d" , &w , &h , &b );

    for( int i = 0; i < w; i++ ){
      for( int j = 0; j < h; j++ ){
	field[i][j] = 0;
      }
    }

    for( int i = 0; i < MAX_N*MAX_N*2; i++ )
      G[i].clear();

    printf( "a" );

    for( int i = 0; i < b; i++ ){
      int x1 , y1 , x2 , y2;
      scanf( "%d %d %d %d" , &x1 , &y1 , &x2 , &y2 );
      for( int j = x1; j <= x2; j++ ){
	for( int k = y1; k <= y2; k++ ){
	  field[j][k] = 1;
	}
      }
    }

    /*
    for( int i = 0; i < w; i++ ){
      for( int j = 0; j < h; j++ ){
	printf( "%d " , field[i][j] );
      }
      printf( "\n" );
    }

    for( int i = 0; i < w; i++ ){
      for( int j = 0; j < h; j++ ){
	printf( "%2d " , noden(i,j) );
      }
      printf( "\n" );
    }
    */
    

    for( int i = 0; i < w; i++ ){
      for( int j = 0; j < h; j++ ){
	if( field[i][j] == 0 ) add_edge( noden(i,j) , noden(i,j)+1 );
      }
    }

    for( int i = 0; i < w; i++ ){
      for( int j = 0; j < h; j++ ){
	if( field[i][j] == 1 ) continue;
	if( i < w-1 && field[i+1][j] == 0 ){
	  //printf( "%d %d\n" , noden(i,j)+1 , noden(i+1,j) );
	  add_edge( noden(i,j)+1 , noden(i+1,j) );
	}
	if( j > 0 && field[i][j-1] == 0 ){
	  //printf( "%d %d\n" , noden(i,j)+1 , noden(i,j-1) );
	  add_edge( noden(i,j)+1 , noden(i,j-1) );
	}
	if( i > 0 && field[i-1][j] == 0 ){
	  //printf( "%d %d\n" , noden(i,j)+1 , noden(i-1,j) );
	  add_edge( noden(i,j)+1 , noden(i-1,j) );
	}
	if( j < h-1 && field[i][j+1] == 0 ){
	  //printf( "%d %d\n" , noden(i,j)+1 , noden(i,j+1) );
	  add_edge( noden(i,j)+1 , noden(i,j+1) );
	}
      }
    }

    int s = 2*max(w,h)*max(w,h)+4;
    int t = 2*max(w,h)*max(w,h)+5;
    for( int i = 0; i < w; i++ ){
      if( field[i][0] == 0 ){
	//printf( "%d %d\n" , s , noden(i,0) );
	add_edge( s , noden(i,0) );
      }
      if( field[i][h-1] == 0 ){
	//printf( "%d %d\n" , t , noden(i,h-1) );
	add_edge( noden(i,h-1)+1 , t );
      }
    }


    printf( "Case #%d: %d\n" , tc , max_flow( s , t ) );
  }

  return 0;
}
