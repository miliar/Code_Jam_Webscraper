#include <iostream>
#include <string>

using namespace std;

int main(int argc, char *argv[])
{
	int T, Cases=0, i, l1, l2, tmp, d1, d2, d3, d4, d5, d6, d7, d8, found, num;
	std::string dis;
	scanf("%d", &T);
    do
    {
		scanf("%d", &l1);
		for(i = 0; i < l1; ++i)
			getline(std::cin, dis);
		scanf("%d%d%d%d", &d1, &d2, &d3, &d4);
		for(;i <= 4; ++i)
			getline(std::cin, dis);
		scanf("%d", &l2);
		for(i = 0; i < l2; ++i)
			getline(std::cin, dis);
		scanf("%d%d%d%d", &d5, &d6, &d7, &d8);
		for(;i <= 4; ++i)
			getline(std::cin, dis);
		found = num = 0;
		if( d1 == d5)
		{
			num = d1;
			++found;
		}
		if( d1 == d6)
		{
			num = d1;
			++found;
		}
		if( d1 == d7)
		{
			num = d1;
			++found;
		}
		if( d1 == d8)
		{
			num = d1;
			++found;
		}

		if( d2 == d5)
		{
			num = d2;
			++found;
		}
		if( d2 == d6)
		{
			num = d2;
			++found;
		}
		if( d2 == d7)
		{
			num = d2;
			++found;
		}
		if( d2 == d8)
		{
			num = d2;
			++found;
		}

		if( d3 == d5)
		{
			num = d3;
			++found;
		}
		if( d3 == d6)
		{
			num = d3;
			++found;
		}
		if( d3 == d7)
		{
			num = d3;
			++found;
		}
		if( d3 == d8)
		{
			num = d3;
			++found;
		}

		if( d4 == d5)
		{
			num = d4;
			++found;
		}
		if( d4 == d6)
		{
			num = d4;
			++found;
		}
		if( d4 == d7)
		{
			num = d4;
			++found;
		}
		if( d4 == d8)
		{
			num = d4;
			++found;
		}

		switch(found)
		{
		case 0 : 
			printf("Case #%d: Volunteer cheated!\n", ++Cases);
			break;
		
		case 1 : 
			printf("Case #%d: %d\n", ++Cases,num);
			break;
		
		default:
			printf("Case #%d: Bad magician!\n", ++Cases);
			break;
		}
	}while(--T); 
}