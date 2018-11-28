#include <stdio.h>
#include <vector>
#include <math.h>
#include <algorithm>
#include <queue>
//#include <unordered_map>
#include <string.h>
using namespace std;

/*typedef pair<int, int> ii;
typedef pair<bool, bool> bb;*/

int t, s, a, u;
char c;


int main(){
	scanf("%d", &t);
	for(int i = 1; i <= t; i++){
		scanf("%d", &s);
		scanf("%c", &c);
		a = u = 0;
		for(int j = 0; j <= s; j++){
			scanf("%c", &c);
			c -= '0';
			//printf("c = %d\n", c);
			if(u < j){
				a += j-u;
				u = j;
			}
			u += c;
		}
		printf("Case #%d: %d\n", i, a);
	}
	return 0;
}