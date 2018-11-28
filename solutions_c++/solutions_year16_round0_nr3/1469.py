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
		int N,J;
		scanf("%d %d\n",&N,&J);
		printf("Case #%d:\n",t);
		for(int i=0;i<J;i++){
			cout << "1";
			for(int j=0;j<(N-2)/2;j++){
				cout << !!(i & (1<<j)) << !!(i & (1<<j));
			}
			cout << "1";
			for(int j=3;j<=11;j++) cout << " " << j;
			cout << endl;
		}
	}
  return 0;
}
