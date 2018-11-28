#include "cstdio"
#include "cstring"
#include "string"
#include "cmath"
#include "vector"
#include "set"
#include "utility"
#include "algorithm"
#include "map"
#include "iostream"

using namespace std;

int main(void)
{
	int t;
	scanf("%d", &t);

	for(int test=1;test<=t;test++)
	{
		map<string, int> dict;
		int idx = 0;
		int fix[30000];
		int n;

		memset(fix, 0, sizeof(fix));
		scanf("%d\n", &n);
		
		char input[20000];
		char *data;
		int offset;
		char word[2000];

		// english
		gets(input);		
		data = input;
		while(sscanf(data, "%s%n", word, &offset) != EOF)
		{
			data += offset;
			if(dict.find(word) == dict.end())
			{
				dict[word] = idx;
				idx++;
			}

			fix[dict[word]] |= 1;
		}		

		// french
		gets(input);		
		data = input;
		while(sscanf(data, "%s%n", word, &offset) != EOF)
		{
			data += offset;
			if(dict.find(word) == dict.end())
			{
				dict[word] = idx;
				idx++;
			}

			fix[dict[word]] |= 2;
		}		
		
		if(n == 2)
		{
			int ans = 0;
			for(int i=0;i<idx;i++)
    		ans += (fix[i] == 3);

			printf("Case #%d: %d\n", test, ans);
		} else {
			int loop = 1 << (n-2);
			int inputs[20][20];
			int lenInputs[20];

			for(int i=0;i<(n-2);i++)
			{
				gets(input);		
				data = input;
				
				lenInputs[i] = 0;
				while(sscanf(data, "%s%n", word, &offset) != EOF)
				{
					data += offset;
					if(dict.find(word) == dict.end())
					{
						dict[word] = idx;
						idx++;
					}
					
					inputs[i][lenInputs[i]] = dict[word];
					lenInputs[i]++;
				}
			}			

			int ans = 2000000000;
			for(int i=0;i<loop;i++)
			{
				int fly[30000];
				memset(fly, 0, sizeof(fly));

				for(int j=0;j<(n-2);j++)
				{
					bool en = (i & (1 << j));
					int mask = 1 << en;

					for(int k=0;k<lenInputs[j];k++)
					{
						fly[inputs[j][k]] |= mask;						
					}
				}

				int buff = 0;
				for(int j=0;j<idx;j++)
					buff += ((fix[j] | fly[j]) == 3);
				ans = min(ans, buff);
			}

			printf("Case #%d: %d\n", test, ans);
		}
	}
}

