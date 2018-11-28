#include<iostream>
#include<cstdio>

using namespace std;

int main()
{
	int t;
	int a,b;
	int board_1[5][5], board_2[5][5];
	
	
	scanf("%d",&t);
	for(int k = 1 ; k <= t ; k++)
	{
		scanf("%d",&a);
		a--;
		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
				scanf("%d",&board_1[i][j]);
				
				
		scanf("%d",&b);
		b--;
		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
				scanf("%d",&board_2[i][j]);
		
		int ans = 0;
		int num;
		
	/*	
		for(int i = 0 ; i < 4 ; i++)
			cout << board_1[a][i] << " " ;
		puts("");
		for(int i = 0 ; i < 4 ; i++)
			cout << board_2[b][i] << " " ;
		puts("");
	*/
			
		for(int i = 0 ; i < 4 ; i++)
			for(int j = 0 ; j < 4 ; j++)
				if(board_1[a][i] == board_2[b][j])
				{
					ans++;
					num = board_1[a][i];
				}
		
	//	cout << "ans = " << ans << endl;
		
		printf("Case #%d: ",k);
			
		if(ans == 0)
			puts("Volunteer cheated!");
		else if(ans == 1)
			printf("%d\n",num);
		else
			puts("Bad magician!");
	}
	return 0;
}


