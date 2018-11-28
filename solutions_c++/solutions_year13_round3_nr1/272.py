#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include <vector>
#include <list>
using namespace std;

int e, r, t;
int v[20];

bool isvow(char x)
{
	return x=='a' || x=='e' || x=='i' || x=='o' || x=='u';
}

bool check(char* name, int i, int j, int limit)
{
	int con = (!isvow(name[i])?1:0);
	if( con == 1 && limit == 1 )
		return true;
	int k=i+1;
	while(k<=j)
	{
		if( isvow(name[k]) )
			con = 0;
		else
		{
			++con;
			if( con >= limit )
				return true;
		}
		++k;
	}
	return false;
}

vector<int>* pre_process(char* name, int len, int limit)
{
	vector<int>* l = new vector<int>;

	int con = (!isvow(name[len-1])?1:0);
	if( con == 1 && limit == 1 )
		l->push_back(len-1);
	int k=len-2;
	while(k>=0)
	{
		if( isvow(name[k]) )
			con = 0;
		else
		{
			++con;
			if( con >= limit )
				l->push_back(k);
		}
		--k;
	}
	return l;
}

int main()
{
	char *name = new char[7000000];
	char str[10][10];
	int N;
	scanf("%d",&N);
	gets(str[0]);
	for(int I=1; I<=N; ++I)
	{
		int nval;
		scanf("%s%d", name, &nval);
		printf("Case #%d:", I);
		int dij[200][200];
		int len= strlen(name);
		long long y = 0;
		int i,j;
		if( check(name,0,len-1,nval) )
		{
			vector<int>* v = pre_process(name,len,nval);
			// all substrings index in v
			int idx = v->size() - 1;
			for(i=0; i<len; ++i)
			{
				while( idx >=0 && (*v)[idx] < i ) --idx;
				if( idx < 0 )
					break;
				int start_index = (*v)[idx];
				y += (long long) len - start_index - nval + 1;
			}
			delete v;
		}
		printf(" %lld\n", y);
	}
	return 0;
}

