#include "stdio.h"
#include <algorithm>
#include <vector>
using namespace std;

struct Node
{
	int inc,dec,pos;
	bool operator < (const Node& no)
	{
		if( no.inc != inc )
			return inc<no.inc;
		if( inc == pos )
			return true;
		if( no.inc == no.pos )
			return false;
		if( no.dec != dec )
			return dec < no.dec;
		return false;
	}
};

int Rec[10][1025];

void eval(int x[10], int i, int max)
{
	int r[10];
}


void EvalAll()
{
	int pow = 8;
	for(int i=3; i<=10; ++i)
	{
		int x[10] = {0,1,2,3,4,5,6,7,8,9};
		next_permutation(x, x+i);
		eval(x,i,pow);
		pow *= 2;
	}
}

void Eval(vector<int>& v)
{
	if( v.size() == 2 )
		return;
	vector<int> v1;
	vector<int> v2;
	for(int i=0; i<v.size(); i+=2)
	{
		v1.push_back(v[i]);
		v2.push_back(v[i+1]);
	}
	Eval(v1);
	Eval(v2);
	v.clear();
	v.insert(v.end(), v1.begin(), v1.end());
	v.insert(v.end(), v2.begin(), v2.end());
}

void Eval(int x[1025], int len, int n)
{
	vector<int> v1(x, x+len);
	Eval(v1);
	for(int i=0; i<len; ++i)
	{
		x[i] = v1[i];
	}
}

int main()
{
	EvalAll();

	char str[10][10];
	int N;
	scanf("%d",&N);
	gets(str[0]);
	Node node[3000];
	int seq[3000];
	int x[1025];
	int power[20] = {1,2,4,8,16,32,64,128,256,512,1024};
	for(int I=1; I<=N; ++I)
	{
		int n, p;
		scanf("%d%d",&n,&p);
		printf("Case #%d:", I);
		int i;
		for(i=0; i<power[n]; ++i)
		{
			x[i]=i;
		}
		Eval(x,power[n],n);
		int max = 0, min = 1024;
		for(i=0; i<p; ++i)
		{
			if(x[i] > max)
				max = x[i];
		}
		sort(x, x+p);
		for(i=0; i<p; ++i)
		{
			if( x[i] != i )
					break;
		}
		printf(" %d %d", i-1, max);
		printf("\n");

	}
	return 0;
}

