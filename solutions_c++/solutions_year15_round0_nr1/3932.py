#include <cstdio>
#include <cmath>
#include <vector>
#include <map>
#include <stdint.h>

using namespace std;

void solve(int count) {
    printf("Case #%d: ", count);
    
    int smax;
    char levels[1024];
    scanf("%d %s", &smax, levels);
    
    int friends = 0;
    int accum = 0;
    for (int i = 0; i <= smax; ++i) {
        int val = levels[i] - '0';
        accum += val;
        if (accum <= i) {
            friends++;
            accum++;
        }
    }
    
    printf("%d\n", friends);
}

int main(int argc, const char * argv[]) {
	int numCases = 0;
  	scanf("%d\n", &numCases);
    
    for (int count = 1; count <= numCases; ++count) {
        solve(count);
    }
    return 0;
}

