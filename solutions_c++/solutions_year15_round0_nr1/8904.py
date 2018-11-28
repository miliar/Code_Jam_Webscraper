#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

int main() {
	int T,X,R,C,i;
	char S[1002];
	char number[]={"0"};
	int level[1002];
	scanf("%d",&T);
	for(i=1;i<=T;i++) {
		int answer=0,cur=0;
		scanf("%d %s",&X,S);
		for(int j=0;j<=X;j++) {
			number[0]=S[j];
			level[j]=atoi(number);
		}
		for(int j=0;j<=X;j++) {
			if(level[j]==0)
				continue;
			if((cur+answer)>=j)
				cur=cur+level[j];
			else {
				int temp=j-cur;
				if(temp>answer)
					answer=temp;
				cur=cur+level[j];
			}
		}
		printf("Case #%d: %d\n",i,answer);
	}
	return 0;
}

