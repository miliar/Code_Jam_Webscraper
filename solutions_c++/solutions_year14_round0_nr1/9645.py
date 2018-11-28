#include <cstdlib>
#include <cstdio>
#include <set>

using namespace std;

int a,b,tmp,T;
set<int> first[4];
set<int> second[4];

int intersection()
{
  int number = -1;
  for( set<int>::iterator it = first[a].begin(); it != first[a].end(); it++){
    if( second[b].find(*it) != second[b].end()){
      if( number == -1 ){
        number = *it;
      } else {
        return -2;
      }
    }
  }
  return number;
}

int main(int argc, char * argv[])
{
  scanf("%d",&T);
  for( int i = 0; i < T; i++ ){
   scanf("%d",&a);a--;
   for( int j = 0; j < 4; j++ ){
    first[j].clear();
    for ( int k = 0; k < 4; k++ ){
      scanf("%d",&tmp);
      first[j].insert( tmp );
    }
   }

   scanf("%d",&b);b--;
   for( int j = 0; j < 4; j++ ){
    second[j].clear();
    for ( int k = 0; k < 4; k++ ){
      scanf("%d",&tmp);
      second[j].insert( tmp );
    }
   }
   
   int res = intersection();
   if( res == -2 ){
     printf("Case #%d: Bad magician!\n",i+1);
   } else if ( res == -1 ){
     printf("Case #%d: Volunteer cheated!\n",i+1);
   } else {
     printf("Case #%d: %d\n",i+1,res);
   }
   
  }
  return 0;
} 
