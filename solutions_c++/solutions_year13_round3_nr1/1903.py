#include <cstdio>
#include <cstring>
#include <fstream>
#include <cstdio>
#include <algorithm>
using namespace std;
#pragma warning(disable : 4996)
int T;
char str[1000001];
int n;
long long best=0;
long long a=0,b=0;
int length;
FILE *fin=fopen("A-small-attempt0.in","r");
ofstream fout("A-small-attempt0.out");
void input()
{
	fscanf(fin,"%s%d",str,&n);
}

bool canMake(int index)
{
	if(index-n+1<0) return false;

	for(int i=index;i>=index-n+1;i--)
	{
		if(str[i]=='a'||str[i]=='e'||str[i]=='i'||str[i]=='o'||str[i]=='u')
		{
			return false;
		}
	}
	return true;
}

void calB(int index)
{
	//str[index]出现的总共有几个。
	if(canMake(index))
	{
		b=index-n+2;
	}
}

void solve()
{
	//动态规划。
	a=0;
	b=0;
	length=strlen(str);
	for(int i=n-1;i<length;i++)
	{
		calB(i);
		a=a+b;
	}
	best=a;
}

void output(int t)
{
	fout<<"Case #"<<t<<": "<<best<<endl;
}

int main()
{
	fscanf(fin,"%d",&T);
	for(int t=1;t<=T;t++)
	{
		input();
		solve();
		output(t);
	}
	return 0;
}
