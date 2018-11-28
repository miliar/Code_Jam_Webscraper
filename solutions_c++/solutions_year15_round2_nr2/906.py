#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <functional>
#include <queue>
#include <float.h>
#include <math.h>
#include <set>
#include <limits.h>
#include <assert.h>

using namespace std;

class CR1B_BTaskProcessor {
public:
	int minimizeUnhappiness( int R, int C, int N );

private:
	int countUnhappiness( int N, int blackInCorner, int blackOnEdge, int blackInside, 
		int whiteInCorner, int whiteOnEdge, int whiteInside );

};