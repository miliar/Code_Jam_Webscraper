#include <cstdio>
#include <algorithm>
using namespace std;

int main(){
  int T;
  int X, R, C;
  bool ans;

  scanf("%d", &T);
  for(int tt = 1; tt <= T; tt++){
    scanf("%d %d %d", &X, &R, &C);
    ans = false;

    if(X == 1)
      ans = true;
    else if(X == 2){
      if((R * C) % 2 == 0)
	ans = true;
    }
    else if(X == 3){
      if(3 <= max(R, C) && 2 <= min(R, C))
	if((R * C) % 3 == 0)
	  ans = true;
    }
    else if(X == 4){
      if(4 <= max(R, C) && 3 <= min(R, C))
	if((R * C) % 4 == 0)
	  ans = true;
    }
    else if(X == 5){
      if(5 <= max(R, C) && 4 <= min(R, C))
	if((R * C) % 5 == 0)
	  ans = true;
    }
    else if(X == 6){
      if(6 <= max(R, C) && 4 <= min(R, C))
	if((R * C) % 4 == 0)
	  ans = true;
    }
    
    printf("Case #%d: %s\n", tt, (ans ? "GABRIEL":"RICHARD"));
  }
}
