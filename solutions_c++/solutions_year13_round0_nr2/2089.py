#include <cstdio>
#include <cstring>
#include <cstdlib>


int garden[112][112];


bool check_h(int n, int m)
{
	for(int i = 0 ; i < 112 ; i ++)
	{
		if(garden[n][i] > garden[n][m]){
			return false;
		}
	}
	return true;
}

bool check_v(int n, int m)
{
	for(int i = 0 ; i < 112 ; i ++)
	{
		if(garden[i][m] > garden[n][m]){
			return false;
		}
	}
	return true;
}

bool check(int n, int m)
{
	if(check_v(n,m) || check_h(n,m)){
		return true;
	}
	return false;
}


int main()
{
	FILE *input = fopen("B.in","r+");
	FILE *output = fopen("B.out","w+");
	
	int tests; fscanf(input,"%d",&tests);
	
	for(int test = 1 ; test <= tests ; test ++)
	{
		int n,m; fscanf(input,"%d%d",&n,&m);
		
		memset(garden,0,sizeof(garden));

		for(int i = 1 ; i <= n ; i ++)
		{
			for(int j = 1 ; j <= m ; j ++){
				fscanf(input,"%d",&garden[i][j]);
			}
		}

		bool ans = true;
		for(int i = 1 ; i <= n ; i ++)
		{
			for(int j = 1 ; j <= m ; j ++)
			{
				if(!check(i,j)){
					ans = false;
					break;
				}
			}
			if(!ans){
				break;
			}
		}

		if(ans){
			fprintf(output,"Case #%d: YES\n",test);
		}
		else{
			fprintf(output,"Case #%d: NO\n",test);
		}
	}
	
	system("pause");
	return 0;
}