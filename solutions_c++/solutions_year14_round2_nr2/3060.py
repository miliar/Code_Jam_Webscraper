#include <stdio.h>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <cstring>
#include <string>
#include <cmath>
#include <cassert>
#include <ctime>
#include <algorithm>
#include <sstream>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <cstdlib>
#include <cstdio>
#include <iterator>
#include <functional>
#include <bitset>


#define TASK   "B-small"


using namespace std;


void solve(){
	
	long A = 0;
	long B = 0;
	long K = 0;

	
	scanf("%ld",&A);
	scanf("%ld",&B);	
	scanf("%ld",&K);		


	long result = 0;
	

	for(long i=0; i<A; i++){
		for(long j=0; j<B; j++){
			if((i&j) <  K){
				result++;
			}
		}		
	}
	
	printf("%ld\n",result);


}



int main(int argc, char **argv)
{
	freopen(TASK".in","r",stdin);
	freopen(TASK".out","w",stdout);
		
	char buf[1000];
	int testNum;
	gets(buf);
	sscanf(buf,"%d",&testNum);

	for (int testId = 1; testId <= testNum; testId++){
		
		printf("Case #%d: ",testId);
		solve();
		
	}	
	
	return 0;
}
