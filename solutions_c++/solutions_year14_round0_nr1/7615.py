#include<iostream>

using namespace std;

int main()
{
	int answer, testCase;
	scanf("%d", &testCase);
	for(int i = 1 ; i<=testCase; i++)
	{
		int j = 0;
		int row[4];
		int arr[4][4];
		while(j < 2)
		{
			scanf("%d", &answer);
			
			for(int m = 0; m<4; m++)
				for(int n = 0; n<4; n++)
				{
					scanf("%d", &arr[m][n] );
					if(j == 0 && (answer-1) == m)
						row[n] = arr[m][n];
				}
			j++;	
		}
		int countSimilarity = 0;
		int result;
		for(j = 0; j<4; j++)
		{
			for(int k = 0; k<4; k++)
				if(row[j] == arr[answer-1][k])
				{
					countSimilarity++;
					result = row[j];
					break;
				}
		}
		if(countSimilarity == 1)
			cout<<"Case #"<<i<<": "<<result;
		else if(countSimilarity == 0)
			cout<<"Case #"<<i<<": Volunteer cheated!";
		else
			cout<<"Case #"<<i<<": Bad magician!";
		cout<<"\n";
	}
	return 0;
}
