#include <cstdio>
#include <vector>
//#include <string>

int main()
{
//	freopen("input.in","r",stdin);
	freopen("out","w",stdout);

	int T;
	int i,j,k;
	std::vector<char> last;
	std::vector<char> last2;
//	std::vector<std::string> ansList;

	scanf("%d*%c",&T);
	fflush(stdin);

	for(i=0;i<T;i++)
	{
		char ch;
		//char last = 'Z'+1;
		while(1)
		{
			scanf("%1c",&ch);

			if(last.empty())
			{
				last.push_back(ch);
			}
			else
			{
				if(last.front()>ch) last.push_back(ch);
				else
				{
					last2.push_back(ch);
					for(j=0;j<last.size();j++)
					{
						last2.push_back(last[j]);
					}

					last.swap(last2);
					last2.clear();
				}
			}

			if(ch == '\n' || ch =='NULL') break;
		}

		printf("Case #%d: ",i+1);
		for(j=0;j<last.size();j++)
		{
			printf("%c",last[j]);
		}
//		printf("\n");

		last.clear();
	}
}