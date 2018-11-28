#include <stdlib.h>
#include <cstdio>
#include <sstream>
#include <math.h>

using namespace std;

bool if_pali(int n)
{
	stringstream ss;
	ss << n;
	string s = ss.str();
	int len = s.length()-1;
	for(int i=0; i < (len + 1) /2; i++)
	{
		if(s[i] != s[len-i])
			return false;
	}
	return true;
}

int main()
{
	int t,a,b, count;
	scanf("%d", &t);
	for(int i=0; i<t; i++)
	{
		count = 0;
		scanf("%d %d", &a, &b);
		for(int n = (int)(ceil(sqrt(a))); n <= int(floor(sqrt(b))); n++ )
		{
			count += (if_pali(n) && if_pali(n*n));
		}
		printf("Case #%d: %d\n",i+1, count);

	}
	return 0;
}
