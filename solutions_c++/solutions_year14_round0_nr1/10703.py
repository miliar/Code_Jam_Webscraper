// 12.04.2014    2:12 PM
#include<iostream>

using namespace std;

int main()
{

	int matrix[4][4], testCases,numOfTests=0, localMatrix1[4], localMatrix2[4], enterRow1, enterRow2;
	
	cin>>testCases;
	int count[testCases];
	int num[testCases],p=0;
	for(int i=0; i<testCases;i++)
	{
		count[i]=0;
	}
	do{
		 	numOfTests++;
		cin>>enterRow1;
		enterRow1=enterRow1-1;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				cin>>matrix[i][j];
				if(i==enterRow1)
				{
					localMatrix1[j]=matrix[i][j];
				}
			}
		}
		cin>>enterRow2;
		enterRow2=enterRow2-1;
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				cin>>matrix[i][j];
				if(i==(enterRow2))
				{
					localMatrix2[j]=matrix[i][j];
				}
			}
		}
		 
		for(int i=0; i<4; i++)
		{
			for(int j=0; j<4; j++)
			{
				if(localMatrix1[i]==localMatrix2[j])
				{
					count[numOfTests]++;
					num[numOfTests]=localMatrix1[i];
					
				}
			}
		}
	

	}while(numOfTests<testCases);

	for(int i=1; i<=testCases; i++)
 	{
	 	if(count[i]==0)
		{
			cout<<"Case #"<<i<<": Volunteer cheated!"<<endl;
		}
		else if(count[i]==1)
		{
				cout<<"Case #"<<i<<": "<<num[i]<<endl;
			
	 	}
	 	else
	 	{
	 	 	cout<<"Case #"<<i<<": Bad magician!"<<endl;
	 	}
	}
	return 0;
}