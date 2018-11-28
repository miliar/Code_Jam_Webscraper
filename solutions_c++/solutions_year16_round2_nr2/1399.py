#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <utility>

using namespace std;

#define MAXC 20
#define MAXJ 20

int cas,T;
long long int minC, minJ, miniAdd, tmpAdd, tmpC, tmpJ;
char C[MAXC], J[MAXJ];

int main()
{
	freopen ("B-small-attempt0.in","r",stdin);
    freopen ("B-small-attempt0.out","w",stdout);
	
	scanf("%d", &T);
	for (cas = 1; cas <= T; ++cas)
	{
		memset(C, 0, sizeof(C));
		memset(J, 0, sizeof(J));
	
		scanf("%s %s", C, J);
		miniAdd = 1000000000000000000;
		
		for (int c0 = 0; c0 < 10; ++c0)
		{
			if (C[0] != '?')
			{
				if (C[0]-'0' != c0)
				{
					//printf("jump c0\n");
					continue;
				}
			}
			for (int c1 = 0; c1 < 10; ++c1)
			{
				if (strlen(C) < 2 && c1 != 0)
				{
					//printf("jump c1 0\n");
					continue;
				}
				if (strlen(C) >= 2)
				{
					if (C[1] != '?' && C[1]-'0' != c1)
					{
						//printf("jump c1 1\n");
						continue;
					}
				}
				for (int c2 = 0; c2 < 10; ++c2)
				{
					if (strlen(C) < 3 && c2 != 0)
					{
						//printf("jump c2 0\n");
						continue;
					}
					if (strlen(C) >= 3)
					{
						//printf("%c %d %d\n", C[2], C[2]-'0', c2);
						if (C[2] != '?' && C[2]-'0' != c2)
						{
							//printf("jump c2 1\n");
							continue;
						}
					}
					for (int j0 = 0; j0 < 10; ++j0)
					{
						if (J[0] != '?')
						{
							if (J[0]-'0' != j0)
							{
								//printf("jump j0 0\n");
								continue;
							}
						}
						for (int j1 = 0; j1 < 10; ++j1)
						{
							if (strlen(J) < 2 && j1 != 0)
							{
								//printf("jump j1 0\n");
								continue;
							}
							if (strlen(J) >= 2)
							{
								if (J[1] != '?' && J[1]-'0' != j1)
								{
									//printf("jump j1 1\n");
									continue;
								}
							}
							for (int j2 = 0; j2 < 10; ++j2)
							{
								if (strlen(J) < 3 && j2 != 0)
								{
									//printf("jump j2 0\n");
									continue;
								}
								if (strlen(J) >= 3)
								{
									if (J[2] != '?' && J[2]-'0' != j2)
									{
										//printf("jump j2 1\n");
										continue;
									}
								}
								if (strlen(J) == 1)
								{
									tmpC = c0;
									tmpJ = j0;
								}
								else if (strlen(J) == 2)
								{
									tmpC = c0*10+c1;
									tmpJ = j0*10+j1;
								}
								else if (strlen(J) == 3)
								{
									tmpC = c0*100+c1*10+c2;
									tmpJ = j0*100+j1*10+j2;
								}
								
								tmpAdd = abs(tmpC-tmpJ);
								if (tmpAdd < miniAdd)
								{
									miniAdd = tmpAdd;
									minC = tmpC;
									minJ = tmpJ;
								}
								
								//printf("%d%d%d %d%d%d\n", c0, c1, c2, j0, j1, j2);
							}
						}
					}
				}
			}
		}
		
		if (strlen(J) == 1)
		{
			printf("Case #%d: %01lld %01lld\n", cas, minC, minJ);
		}
		else if (strlen(J) == 2)
		{
			printf("Case #%d: %02lld %02lld\n", cas, minC, minJ);
		}
		if (strlen(J) == 3)
		{
			printf("Case #%d: %03lld %03lld\n", cas, minC, minJ);
		}
	}
	

	return 0;
}