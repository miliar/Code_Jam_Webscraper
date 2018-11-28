#include <stdio.h>
#include <iostream>
#include <string.h>

//#include <random>

int main()
{
// 	printf("100\n");
// 	std::uniform_int_distribution<uint64_t> dist(0, 1000000);
// 	for(int i=0; i<100; ++i)
// 	{
// 		printf("%llu\n", dist(std::random_device()));
// 	}
// 	return 0;




	int cases;
	std::cin >> cases;
	char buf[50];
	for(int c=0; c<cases; ++c)
	{
		uint64_t base=0;

		std::cin >> buf;
		if(buf[0]=='0')
		{
			printf("Case #%d: INSOMNIA\n", c+1);
			continue;
		}
		int len=(int)strlen(buf);
		unsigned char *bp=((unsigned char *)&base)+7;
		for(int i=0; i<len; ++i)
		{
			bp[-i]=buf[len-1-i]-'0';
		}
		auto StartIndex=[](unsigned char *p)
		{
			for(int i=0; i<8; ++i)
				if(p[i]!=0)
					return i;
			return 8;
		};
		uint64_t sum=base;
		unsigned char *sp=((unsigned char *)&sum)+7;
		unsigned int seen=0;
		for(;;)
		{
			for(int i=0; i<7; ++i)
			{
				if(sp[-i]>9)
				{
					sp[-i]-=10;
					sp[-i-1]+=1;
				}
			}
			for(int i=StartIndex((unsigned char *)&sum); i<8; ++i)
			{
				seen|=1<<((unsigned char *)&sum)[i];
			}
			if(seen==0x3ff)
				break;
			sum+=base;
		}
		int start=StartIndex((unsigned char *)&sum);
		sum+=0x30303030'30303030u;
		printf("Case #%d: %.*s\n", c+1, 8-start, ((unsigned char *)&sum)+start);
	}
	return 0;
}