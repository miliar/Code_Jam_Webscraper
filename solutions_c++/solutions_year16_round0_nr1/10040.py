/*
Jing.alpc30
*/
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

const int iif = 1000000000;
const double pi = 3.1415926;
const double inf = 1e20;
bool b[10];

bool check(int x)
{
	for(int i = 0; i < 10; i++)
		if(b[i] == 0)
		return  0;
	return 1;
}

void getnumber(int x)
{
	while(x)
	{
		b[x%10] = 1;
		x/=10;
	}
}
int calc(int x)
{
	int o = x;
	
	//memset(b, 0, sizeof(b));
	for(int i = 0; i < 10; i++)
		b[i] = 0;
	getnumber(x);
	while(check(x)==0)
	{
		
		x+=o;
		getnumber(x);
		//printf("%d ",x);
	}
	return x;
}

int main(int argc, char *argv[])
{
	int T;
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	scanf("%d",&T);
	for(int i = 0; i  < T; i++)
	{
		int n;
		scanf("%d",&n);
		printf("Case #%d: ", i+1); 
		if(n == 0)
			printf("INSOMNIA\n");
		else
		{
			printf("%d\n",calc(n));
		}
	}

	return 0;
}
