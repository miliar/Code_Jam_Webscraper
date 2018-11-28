#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include<string.h>
using namespace std;
int mod = 1000000007;
vector<long long> S;
void initialize(long long M , long long N)
{
	S.push_back(1);
	long long MM=M;
	while(MM<=N){
		S.push_back(MM);
		MM = MM * M;
	}
}

int count(  int m, int n )
{
    // table[i] will be storing the number of solutions for
    // value i. We need n+1 rows as the table is consturcted
    // in bottom up manner using the base case (n = 0)
    int table[n+1];

    // Initialize all table values as 0
    memset(table, 0, sizeof(table));

    // Base case (If given value is 0)
    table[0] = 1;

    // Pick all coins one by one and update the table[] values
    // after the index greater than or equal to the value of the
    // picked coin
    for(int i=0; i<m; i++)
        for(int j=S[i]; j<=n; j++)
            table[j] =(table[j] + table[j-S[i]])%mod;

    return table[n];
}




int main() {
	int M,N;

	scanf("%d %d",&N,&M);
	initialize(M,N);
	printf("%d",count(S.size(),N));
	return 0;
}



