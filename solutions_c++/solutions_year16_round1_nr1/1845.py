#include<iostream>
#include <list>
#include<map>
#include<set>
#include<stdio.h>
using namespace std;
char s[1000+1];
int main() 
{
	freopen("A-large416.in","r",stdin);  
	freopen("A-large416.out","w",stdout);
	int T;
	scanf("%d",&T);
	getchar();
	int j=1;
	while(T--) 
	{
		gets(s);
		list<char> res;
		char *p=s;
		while((*p)!='\0')
		{
			if(res.empty())
			res.push_back((*p));
			else if((*p)>=*res.begin())
			res.push_front(*p);
			else
			res.push_back(*p);	
			p++;
		}
		list<char>::iterator itor=res.begin();
		printf("Case #%d: ",j++);
		while(itor!=res.end())
		{
			printf("%c",*itor);
			itor++;
		}
		printf("\n");
		
	}
}
