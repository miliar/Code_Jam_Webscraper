#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;


int counter = 0;

//data goes here

int solve(){
	printf("Case #%d: ", ++counter);

	int rings = 0;

  int r; scanf("%d", &r);
	int t; scanf("%d", &t);

	
	while(t > 0){
		int paintused = (r+1)*(r+1) - r*r;
		if(paintused <= t){
			rings++;
			r += 2;
		}
		t -= paintused;
	}


	printf("%d\n", rings);
	return 0;
}




int main() {
  int T; scanf("%d", &T);
  while (T--){
		solve();
	}

	return 0;
}
