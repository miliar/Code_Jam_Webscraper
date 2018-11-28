#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <vector>
#include <deque>
#include <set>

using namespace std;

int main()
{
	int T;
	scanf("%d",&T);
	for(int t=1; t<=T; t++)
	{		
		int K,C,S;
		scanf("%d %d %d\n",&K,&C,&S);
		if(C>K) C=K;
		if(S<K+1-C){
			printf("Case #%d: IMPOSSIBLE\n",t);
			continue;
		}
		unsigned long long B=0;
		for(int i=1;i<C;i++) B=B*K+i;
		printf("Case #%d:",t);
		for(int i=1;i<=K+1-C;i++) cout << " " << B+i;
		cout << endl;
	}
  return 0;
}
