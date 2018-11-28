#include <stdio.h>
#include <string.h>
#include <assert.h>

void convert(char* buff,int begin,int last)
{
	for(int i = begin,j = last;i <= j;++i,--j)
	{
		char c = buff[i];
		buff[i] = '+' + '-' - buff[j];
		buff[j] = '+' + '-' - c;
	}
}

int main()
{
	static const size_t buff_size = 1000;
	char buff[buff_size] = { 0 };
	unsigned int nCases = 0;scanf("%d",&nCases);
	for(unsigned int iCases = 1;iCases <= nCases;++iCases)
	{
		scanf("%s",buff);
		unsigned int ans = 0,len = strlen(buff);
		for(unsigned int ie = len - 1;ie != (unsigned int)(-1);--ie)
		{
			if(buff[ie] == '+') continue;
			size_t p = 0;
			for(;'+' == buff[p];++p);
			if(0 != p)
			{
				++ans;convert(buff,0,p-1);
			}
			assert('-' == buff[0]);
			++ans;convert(buff,0,ie);
		}
		printf("Case #%d: %u\n",iCases,ans);
	}
	return 0;
}
