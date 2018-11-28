#include <cstdio>
#include <set>
using namespace std;

int main(){
  int T; scanf("%d",&T);
  
  for(int t = 1; t <= T; ++t){
    set<int> f;
    int z; scanf("%d", &z);
    
    int u;
    for(int i = 0; i < 4; ++i){
      for(int j = 0; j < 4; ++j)
      {
	scanf("%d", &u);
	if(i == z - 1)
	  f.insert(u);
      }
    }
    
    set<int> f2;
    int z2; scanf("%d", &z2);
    
    for(int i = 0; i < 4; ++i){
      for(int j = 0; j < 4; ++j)
      {
	scanf("%d", &u);
	if(i == z2 - 1 && f.count(u))
	  f2.insert(u);
      }
    }
    
    printf("Case #%d: ", t);
    
    if(f2.size() > 1){
      printf("Bad magician!\n");
    }
    else if(f2.size() == 1)
      printf("%d\n",*(f2.begin()));
    else 
      printf("Volunteer cheated!\n");
  }
}

