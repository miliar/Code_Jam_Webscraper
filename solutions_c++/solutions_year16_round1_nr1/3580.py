#include <stdio.h>
#include <vector>
#include <string>
#include <string.h>
using namespace std;
vector<char> t;
vector<char>::iterator it;
int main()
{
	int T,i,j,length;
	char c, S[1010];
	scanf("%d",&T);
	for(j=1;j<=T;j++)
	{
		t.clear();
		scanf("%s",S);
		length = strlen(S);
		t.push_back(S[0]);
		c = S[0];
		for(i=1;i<length;i++)
		{
			if(S[i] < c)
				t.push_back(S[i]);
			else 
			{
				it = t.begin();
				t.insert(it,S[i]);
				c = S[i];
			}
					
		}
		printf("Case #%d: ",j);
		for(it=t.begin();it<t.end();it++)
			printf("%c",*it);
		printf("\n");
	}
	return 0;
}
