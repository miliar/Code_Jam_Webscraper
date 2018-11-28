#include <cstdio>
#include <iostream>
#include <cstring>
using namespace std;
int main(void)
{
	int T;
	cin>>T;
	for(int t=1; t<=T; t++)
	{
		char word[1002];
		char newword[1002];
		scanf("%s",word);
		char temp[1002];
		int idx = 0;
		char curmax= word[idx];
		newword[idx] = '\0';
		while(word[idx] != '\0')
		{
			if(word[idx] >= curmax)
			{
				curmax = word[idx];
				sprintf(temp,"%c%s",word[idx],newword);
				strcpy(newword,temp);
			}
			else
			{
				sprintf(temp,"%s%c",newword,word[idx]);
				strcpy(newword,temp);
			}
			idx++;
		}
		printf("Case #%d: %s\n",t,newword);
	}
}
