#include <stdio.h>
#include <stdlib.h>
#include <vector>
#include <string.h>
#include <queue>
using namespace std;

vector<short> tmp;

void flip(int i)
{
	vector<short> tmp2;
	tmp2.reserve(tmp.size());
	for(int j=i;j>-1;j--)
	{
		tmp2.push_back(tmp[j]^1);
	}
	for(int j=i+1;j<tmp.size();j++)
		tmp2.push_back(tmp[j]);
	tmp=tmp2;
}

int top;
int moves()
{
	while(top >-1 && tmp[top]==1) top--;
	if(top==-1)
		return 0;
	int j=0;
	while(j+1 <=top && tmp[j]==tmp[j+1]) j++;
	if(tmp[j]==0)
	{
		flip(top);
		return 1 + moves();
	}
	else
	{
		flip(j);
		flip(top);
		return 2+moves();
	}

}


int main()
{
	int n;
	scanf("%d",&n);
	getchar();
	for(int i=1;i<=n;i++)
	{
		tmp.resize(0);
		char s[101] ;
		scanf("%s",s);
		for(int j=0;j<strlen(s);j++)
			if(s[j]=='-')
				tmp.push_back(0);
			else
				tmp.push_back(1);
		top=tmp.size()-1;
		printf("Case #%d: %d\n",i,moves());
	}
	return 0;
}


