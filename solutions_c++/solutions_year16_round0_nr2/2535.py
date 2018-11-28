#include <cstdio>
#include <cstring>
#include <algorithm>
#define ll long long
using namespace std;

int f(char *s, bool piu)
{
	if(*s == '\0')
		return 0;
	if ((*s=='+')==piu)
		return f(s+1,piu);
	
	return 1+f(s+1,!piu);
	
}

int main()
{
	int t;
	char s[101];
	FILE *in = fopen("input.txt", "r");
	FILE *out = fopen("output.txt", "w");
	fscanf(in, "%d", &t);
	for(int i=0; i<t; i++)
	{
		fscanf(in,"%s",s);
		int l = strlen(s);
		for(int j=0; j<l/2; j++)
			swap(s[j], s[l-j-1]);
		fprintf(out,"Case #%d: %d\n",i+1,f(s,true));
	}
	return 0;
}
