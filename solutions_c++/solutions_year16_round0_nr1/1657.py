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
		int N;
		scanf("%d",&N);
		if(N==0){
			printf("Case #%d: INSOMNIA\n",t);
			continue;
		}
		set <int> digits;
		int C=0;
		while(digits.size()<10){
			C+=N;
			int temp=C;
			while(temp>0){
				digits.insert(temp%10);
				temp/=10;
			}
		}	
		printf("Case #%d: %d\n",t,C);
	}
  return 0;
}
