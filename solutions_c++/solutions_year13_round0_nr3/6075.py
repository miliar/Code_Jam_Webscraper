#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <iostream>
#include <set>

using namespace std;

bool isPalindrome(unsigned long long int xx)
{
	char s[50];
	char s2[50];
	int i, j;

	snprintf(s, sizeof(s), "%lld", xx);

	j = 0;

	for (i=strlen(s)-1;i>=0;i--)
	{
		s2[j++] = s[i];
	}

	s2[j] = 0;

	return (strcmp(s, s2)==0);
}

int main(int argc, char *argv[])
{
	FILE *fp;
	char buff[1024];
	unsigned long long int x, a, b, k;
	int ci;
	int numOfCase;
	long double d;
	unsigned long long int fsc;
	set<unsigned long long int> sx;

	fp = fopen(argv[1], "r");

	if (!fp) return (-1);

	numOfCase = atoi(fgets(buff, sizeof(buff), fp));

	for(ci=1;ci<=numOfCase;ci++)
	{
		fgets(buff, sizeof(buff), fp);
		sscanf(buff, "%lld %lld", &a, &b);

		fsc = 0;

		for (x=a;x<=b;x++)
		{
//			if (sx.find(x) != sx.end())
//			{
//				cout << "use set for " << x << endl;
//				fsc++;
//			}
//			else if (isPalindrome(x))
			if (isPalindrome(x))
			{
				d = sqrt((long double)x);

				if (d == floor(d))
				{
					if (isPalindrome((unsigned long long int)floor(d)))
					{
//						sx.insert(x);
						fsc++;
					}
				}
			}
		}

		cout << "Case #" << ci << ": " << fsc << endl;
	}
	
	fclose(fp);
	return (0);
}

