//Bismillaahir Rahmaanir Raheem

#include <stdio.h>
#include <iostream>
using namespace std;

int main()
{
	int T, i, j, row1, row2, ans, count = 0, set1[5][5], set2[5][5], k;
	freopen("E:\\Special Applications\\MS Visual C++ 6.0\\MSDev98\\MyProjects\\Google Codejam 2014\\Input and Output\\A-small-attempt0.in", "r", stdin);
	freopen("E:\\Special Applications\\MS Visual C++ 6.0\\MSDev98\\MyProjects\\Google Codejam 2014\\Input and Output\\OutputProbA.txt", "w", stdout);
	cin>>T;
	for(k = 1; k <= T; k++)
	{
		count = 0;
		cin>>row1;
		for(i = 1; i <= 4; i++)
		{
			for(j = 1; j <= 4; j++)
				cin>>set1[i][j];
		}
		cin>>row2;
		for(i = 1; i <= 4; i++)
		{
			for(j = 1; j <= 4; j++)
				cin>>set2[i][j];
		}
		for(i = 1; i <= 4; i++)
		{
			for(j = 1; j <= 4; j++)
			{
				if(set1[row1][i] == set2[row2][j])
				{
					ans = set1[row1][i];
					count++;	//Initialise as 0;
				}
			}
		}
		cout<<"Case #"<<k<<": ";
		if(!count)
			cout<<"Volunteer cheated!"<<endl;
		else if(count == 1)
			cout<<ans<<endl;
		else
			cout<<"Bad magician!"<<endl;
	}
		
	return 0;
}