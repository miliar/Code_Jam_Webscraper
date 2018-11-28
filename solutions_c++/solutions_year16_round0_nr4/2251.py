#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <stdlib.h>
#include <set>
#include <algorithm>
#include <math.h>
#include <stdio.h>
#include <unistd.h>
#include <stack>
#include <sstream>
#include <iomanip>
#include <bitset>
#define ff first
#define ss second

using namespace std;

typedef long long ll;

int main() {
	int t,i,tc=1,k,c,s;

	scanf("%d", &t);
	while(t--){
		scanf("%d%d%d", &k,&c,&s);		
		printf("Case #%d:", tc++);
		for(i = 1; i <= k; i++)
			printf(" %d", i);
		printf("\n");
	}

	return 0;
}
