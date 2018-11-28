#include <iostream>
#include <vector>
using namespace std;



std::vector<std::string> inline StringSplit(const std::string &source, const char *delimiter = " ", bool keepEmpty = false)
{
    std::vector<std::string> results;

    size_t prev = 0;
    size_t next = 0;

    while ((next = source.find_first_of(delimiter, prev)) != std::string::npos)
    {
        if (keepEmpty || (next - prev != 0))
        {
            results.push_back(source.substr(prev, next - prev));
        }
        prev = next + 1;
    }

    if (prev < source.size())
    {
        results.push_back(source.substr(prev));
    }

    return results;
}

int glawn[100][100];

void main(void)
{
	char numcase[10];
	cin.getline(numcase, 10);

	int casecnt = atoi(numcase);

	for(int i = 0; i < casecnt; i++)
	{
		memset(glawn, 0, sizeof(glawn));
		
		char oneline[1000];

		cin.getline(oneline, 1000);

		vector<string> a =  StringSplit(oneline);

		int y = atoi(a[0].c_str());
		int x = atoi(a[1].c_str());
		
		for(int line = 0; line < y; line++)
		{
			a.clear();
			cin.getline(oneline, 1000);
			a =  StringSplit(oneline);

			for(int col = 0; col < x; col++)
			{
				glawn[line][col] = atoi(a[col].c_str());
			}
		}


		bool bPossible = true;
		// problem solve..
		for(int row = 0; row < y; row++)
		{
			for(int col = 0; col < x; col++)
			{
				bool bPossible1 = true;
				bool bPossible2 = true;
				for(int krow = 0; krow < y; krow++)
				{
					if(glawn[row][col] < glawn[krow][col])
					{
						bPossible1 = false;
					}
				}
				
				for(int kcol = 0; kcol < x; kcol++)
				{
					if(glawn[row][col] < glawn[row][kcol])
					{
						bPossible2 = false;
					}
				}

				if(bPossible1 == false && bPossible2 == false)
				{
					bPossible = false;
					goto T;
				}
			}
		}
T:
		if(bPossible)
		{
			cout<<"Case #"<<i+1<<": "<<"YES\n";
		}
		else
		{
			cout<<"Case #"<<i+1<<": "<<"NO\n";
		}
	}
}