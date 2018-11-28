#include <cstdio>
#include <cmath>
#include <vector>

int main()
{
	freopen("A-large.in","r",stdin);

	std::vector<char> str;
	std::vector<int> ansOne;
	std::vector<int> ansTwo;
	std::vector<int> ansThree;
	std::vector<int> ansFour;
	std::vector<int> ansFive;
	std::vector<int> ansSix;
	std::vector<int> ansSeven;
	std::vector<int> ansEight;
	std::vector<int> ansNine;
	std::vector<int> ansZero;
	int T,i,j;
	char tmp;
	scanf("%d%*c",&T);

	for(i=0;i<T;i++)
	{
		int zero=0,one=0,two=0,three=0,four=0,five=0,six=0,seven=0,eight=0,nine=0;

		scanf("%1c",&tmp);

		str.push_back(tmp);

		while(tmp != '\n')
		{
			scanf("%1c",&tmp);
			str.push_back(tmp);
		}
		
		for(j=0;j<str.size();j++)
		{
			if(str[j] == 'Z')
			{
				zero++;
			}

			if(str[j] == 'W')
			{
				two++;
			}

			if(str[j] == 'U')
			{
				four++;
			}

			if(str[j] == 'X')
			{
				six++;
			}

			if(str[j] == 'G')
			{
				eight++;
			}
		}
		for(j=0;j<str.size();j++)
		{
			if(str[j] == 'H')
			{
				three++;
			}

			if(str[j] == 'F')
			{
				five++;
			}

			if(str[j] == 'S')
			{
				seven++;
			}
		}
		three -= eight;
		five -= four;
		seven -= six;
		for(j=0;j<str.size();j++)
		{
			if(str[j] == 'I')
			{
				nine++;
			}
		}
		nine = nine - eight - six - five;
		for(j=0;j<str.size();j++)
		{
			if(str[j] == 'N')
			{
				one++;
			}
		}
		one = one - seven - 2*nine;

		ansZero.push_back(zero);
		ansOne.push_back(one);
		ansTwo.push_back(two);
		ansThree.push_back(three);
		ansFour.push_back(four);
		ansFive.push_back(five);
		ansSix.push_back(six);
		ansSeven.push_back(seven);
		ansEight.push_back(eight);
		ansNine.push_back(nine);

		str.clear();
	}

	fclose(stdin);
	freopen("out","w",stdout);

	for(i=0;i<T;i++)
	{
		printf("Case #%d: ",i+1);
		
		for(j=0;j<ansZero[i];j++)
		{
			printf("0");
		}
		for(j=0;j<ansOne[i];j++)
		{
			printf("1");
		}
		for(j=0;j<ansTwo[i];j++)
		{
			printf("2");
		}
		for(j=0;j<ansThree[i];j++)
		{
			printf("3");
		}
		for(j=0;j<ansFour[i];j++)
		{
			printf("4");
		}
		for(j=0;j<ansFive[i];j++)
		{
			printf("5");
		}
		for(j=0;j<ansSix[i];j++)
		{
			printf("6");
		}
		for(j=0;j<ansSeven[i];j++)
		{
			printf("7");
		}
		for(j=0;j<ansEight[i];j++)
		{
			printf("8");
		}
		for(j=0;j<ansNine[i];j++)
		{
			printf("9");
		}

		printf("\n");
	}
}