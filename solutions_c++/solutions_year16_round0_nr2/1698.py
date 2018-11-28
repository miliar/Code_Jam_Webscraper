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
	cin.ignore(1,'\n');
	for(int t=1; t<=T; t++)
	{		
		string S;
		getline(cin,S);
		S+="+";
		int change=0;
		for(int i=0;i<S.length()-1;i++) change+=S[i]!=S[i+1];
		printf("Case #%d: %d\n",t,change);
	}
  return 0;
}
