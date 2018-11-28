#include <cstdio>
#include <string>
#include <iostream>

using namespace std;


int main()
{
	int t;
	scanf("%d",&t);
	int case_count=1;
	while(t--)
	{
		string pancakes;
		cin >>pancakes;
		int flip_count=0;
		for(int i=1;i<pancakes.size();i++)
			if(pancakes[i-1]!=pancakes[i])
				flip_count++;
		if(pancakes[pancakes.size()-1]=='-')
			flip_count++;
		printf("Case #%d: %d\n",case_count++,flip_count);
		pancakes.clear();
	}
	return 0;
}