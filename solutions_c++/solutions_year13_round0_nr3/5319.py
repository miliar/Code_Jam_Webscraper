#include <iostream>
#include <stdio.h>
#include <string>
#include <string.h>
#include <vector>
#include <map>
#include <stack>
#include <queue>
#include <map>
#include <list>
#include <algorithm>
#include <functional>
#include <unordered_map>
using namespace std;

typedef long long int LLI;

int T;
LLI A,B;

bool isPalindrome(LLI n)
{
	LLI div = 1;
	while(n/div >=10)
		div *= 10;
	while(n>0)
	{
		int left = n/div;
		int right = n%10;
		if(left != right)return false;
		n = (n%div)/10;
		div /= 100;
	}
	return true;
}

void Solve(int nCase)
{
	int count = 0;
	for(LLI i = sqrt(A);i<=sqrt(B);i++)
	{
		if(!isPalindrome(i))continue;
		int j = i*i;
		if(j>= A && isPalindrome(j))
			count++;
	}
	cout<<"Case #"<<nCase<<": "<<count<<endl;
}
int main(int argc, char const *argv[])
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>A>>B;
		Solve(t);
	}
	return 0;
}