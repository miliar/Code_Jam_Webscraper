#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
	FILE *fp;
	char buff[1024];
	int t, x;
	unsigned long long a, b, k, ia, ib, ik, ans;;

	if (!(fp = fopen(argv[1], "r"))) return (-1);

	t = atoi(fgets(buff, sizeof(buff), fp));

	for(x=1;x<=t;x++)
	{
		fgets(buff, sizeof(buff), fp);
		sscanf(buff, "%ld %ld %ld", &a, &b, &k);

		ans = 0;

		for (ia=0;ia<a;ia++)
		{
			for (ib=0;ib<b;ib++)
			{
				for (ik=0;ik<k;ik++)
				{
					if ((unsigned long long)(ia & ib) == ik)
					{
//						printf("%ld %ld %ld %ld\n", ia, ib, ia&ib, ik);
						ans++;
					}
				}	
			}
		}

		cout << "Case #" << x << ": " << ans << endl;
	}
	
	fclose(fp);
	return (0);
}
