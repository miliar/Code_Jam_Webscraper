#include<cstdio>

int main(int argc, char **argv)
{
	int t = 0;
	FILE *in = fopen(argv[1], "r");
	FILE *out = fopen(argv[2], "w");

	fscanf(in, "%d", &t);
	for(int i=1; i<=t; i++)
	{
		int n, m;
		fscanf(in, "%d %d", &n, &m);
		
		int lawn[100][100] = {0};
		for(int j=0; j<n; j++)
		{
			for(int k=0; k<m; k++)
			{
				fscanf(in, "%d", &lawn[j][k]);
			}
		}

		int flag = 0;
		for(int j=0; j<n; j++)
		{
			for(int k=0; k<m; k++)
			{
				if(lawn[j][k] < 100)
				{
					int flag1 = 0, flag2 = 0;

					for(int z = 0; z<n; z++)
					{
						if(lawn[z][k] > lawn[j][k])
						{
							flag1 = 1;
							break;
						}
					}
					
					if(flag1)
					{
						for(int z = 0; z<m; z++)
						{
							if(lawn[j][z] > lawn[j][k])
							{
								flag2 = 1;
								break;
							}
						}

						if(flag2)
						{
							flag = 1;
							break;
						}
					}
				}
				//printf("%d ", lawn[j][k]);
			/*	flag = 0;
				if(lawn[j][k] == lawn[j][0])
				{
					for(int x=1; x<k; x++)
					{
						if(lawn[j][k] != lawn[j][x])
						{
							flag = 1;
							break;	
						}
					}
				}
				else
					flag = 1;
				
				if(!flag)
				{
					continue;
				}
				
				flag = 0;
				if(lawn[j][k] == lawn[j][m-1])
				{
					for(int x=k+1; x<(m-1); x++)
					{
						if(lawn[j][k] != lawn[j][x])
						{
							flag = 1;
							break;
						}
					}
				}
				else
					flag = 1;
				
				if(!flag)
				{
					continue;
				}				

				flag = 0;
				if(lawn[j][k] == lawn[0][k]) 
				{
					for(int x=1; x<j; x++)
					{
						if(lawn[j][k] != lawn[x][k])
						{
							flag = 1;
							break;
						}
					}
				}
				else
					flag = 1;
				
				if(!flag)
				{
					continue;
				}
			
				flag = 0;
				if(lawn[j][k] == lawn[n-1][k])
				{
					for(int x=j+1; x<n-1; x++)
					{
						if(lawn[j][k] != lawn[x][k])
						{
							flag = 1;
							break;
						}
					}
				}
				else
					flag = 1;
				
				if(flag)
				{
					break;
				}*/
			}
			//printf("\n");
			if(flag)
				break;
		}
		
		if(flag)
		{
			fprintf(out, "Case #%d: NO\n", i);
		}
		else
		{
			fprintf(out, "Case #%d: YES\n", i);
		}
	}
	return 0;
}
