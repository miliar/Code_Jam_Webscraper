#include <iostream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <list>
using namespace std;

//#define real long long
#define real int
real N;

string valueString = "";

void process()
{
	int need = 0;
	int curr = 0;
	for (int i = 0; i < valueString.length(); i++)
	{
		char c = valueString[i];
		int k = c - '0';
		if (curr < i)
		{
			int t = i - curr;
			need += t;
			curr += t;
		}
		curr += k;
	}
	printf("%d",need);
}



void main()
{
	freopen("11.in", "r", stdin);
	freopen("11.out", "w", stdout);
	int times;
	scanf("%d", &times);
	for (int time = 0; time < times; time++)
	{
		scanf("%d", &N);
		char str[1100];
		scanf("%s", &str);
		valueString = str;
		printf("Case #%d: ", time + 1);
		process();
		printf("\n");
		fflush(stdout);
	}
}