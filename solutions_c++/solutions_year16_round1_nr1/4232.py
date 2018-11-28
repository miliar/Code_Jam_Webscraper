#include<bits/stdc++.h>
using namespace std;
main()
{
	int T,t,i;
	freopen("A.txt","w",stdout);
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		char s[1005];
		scanf("%s",s);
		list<char> L;
		list<char>::iterator it;
		for(i=0;s[i]!='\0';i++)
		{
			if(L.empty())
			{
				L.push_back(s[i]);
			}
			else
			{
				it=L.begin();
				if(s[i]>=*it)
				{
					L.insert(it,s[i]);
				}
				else
				{
					L.push_back(s[i]);
				}
			}
		}
		printf("Case #%d: ",t);
		for(it=L.begin();it!=L.end();it++)
		{
			printf("%c",*it);
		}
		printf("\n");
	}
    scanf(" ");
}

