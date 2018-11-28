#include <iostream>
#include <cstdio>

using namespace std;

int t;

int b[150][150];
int tag[150][150];
bool h[150];
int n , m;
int main()
{
	freopen("test.txt" , "r" , stdin);
	freopen("out.txt" , "w" , stdout);
	scanf("%d" , &t);
	int cas = 0;
	while (t --)
	{
		cas ++;

		scanf("%d %d" , &n , &m);
		for (int i = 0 ; i < n ; i ++){
			for (int j = 0;  j<m;j ++)
			{
				scanf("%d" , &b[i][j]);
				tag[i][j] = 100;
			}
		}
		bool flag = true;
		memset(h , 0 , sizeof(h));
		while (flag){

			flag = true;
			int ma = -1;
			for (int i=0 ; i < n ; i ++ ){
				for (int j = 0 ; j < m; j ++)
				{
					if (b[i][j] != tag[i][j])
					{
						ma = max(ma , b[i][j]);
					}
				}
			}
			if (ma == -1)
			{
				break;
			}
			bool dd = false;
			for (int i = 0 ; i < n ; i ++)
			{ 
				for (int j = 0 ; j< m ;j ++)
				{
					if (ma <= tag[i][j] && tag[i][j] != b[i][j])
					{
						bool has = false;
						for (int k = 0 ; k < m ; k ++){
							
							if (k!= j && tag[i][k]  == b[i][k] && b[i][k] > ma){
						
								has = true;
								break;
							}
						}
						if (has == false)
						{
							for (int k = 0 ; k < m ; k ++)
							{
								dd = true;
								tag[i][k] = ma;
							}
						}
						has = false;
						for (int k = 0 ; k < n ; k ++){
							if ( k!= i && tag[k][j]  == b[k][j] && b[k][j] > ma ){
								has = true;
								break;
							}
						}
						if (has == false)
						{
							for (int k = 0 ; k < n ; k ++)
							{
								dd = true;
								tag[k][j] = ma;
							}
						}
					}
				}
				
			}
			/*
			for (int i = 0 ; i < n ; i ++){
				for (int j = 0 ;j  < m ; j ++){
					printf("%d " , tag[i][j]);
				}
				printf("\n");
			}
			printf("=====================\n");
			*/
			h[ ma ] = true;
			flag = dd;
		}
		bool ans = true;
		for (int i = 0 ; i < n ; i ++)
		{
			for (int j = 0 ; j < m; j ++)
			{
				if(tag[i][j] != b[i][j])
				{
					ans = false;
				}
			}
		}
		if (ans == true)
			printf("Case #%d: YES\n" , cas);
		else printf("Case #%d: NO\n" , cas);
	}
}