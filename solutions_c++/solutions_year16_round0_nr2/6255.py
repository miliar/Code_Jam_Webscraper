#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <queue>
#include <map>
#define MAX 1000000
using namespace std;


int main()
{
	int T,change;
	char symbol;
	string line;
	scanf("%d",&T);
	getchar();
	for(int t=1;t<=T;t++)
	{
		getline(cin,line);
		change=0;
		symbol=line[0];
		for(int i=1;i<line.size();i++)
		{
			if(line[i]!=symbol)
			{
				change++;
				symbol=line[i];
			}
		}
		if(line[line.size()-1]=='-')
			change++;
		printf("Case #%d: %d\n",t,change);
	}
	return 0;
}