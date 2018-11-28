#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;

int works;
int cost;
int main(){

    int T; scanf("%d", &T);
    for (int Tcount = 1; Tcount <= T; Tcount++)
    {
    	unsigned long P,Q; 
    	scanf("%ld/%ld",&P,&Q);
    	int i=1;

    	if( ((Q & ~(Q-1))==Q)? Q : 0)
    	{	
    	while(P*pow(2,i)<Q) {
    	    i++;
    	}
    	printf("Case #%d: %ld\n",Tcount,i);
		}
		else
			printf("Case #%d: impossible\n", Tcount );
    }
    return 0;

}