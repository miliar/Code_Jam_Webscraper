#include<iostream>
#include<conio.h>
using namespace std;
int nextLargest(int lawn[100][100],int max[10000][2], int imba, int &count, int N, int M)
{
	count = 0;
	int largest=0;
	for(int i=0 ; i<N ; i++)
		{
		for(int j=0 ; j<M ; j++)
		{
			if(lawn[i][j]<imba)
			{
				if(lawn[i][j] == largest)
				{
					count ++;
					max[count][0] = i;
					max[count][1] = j;
				}
				else
				if(lawn[i][j] > largest)
				{
					largest = lawn[i][j];
					count = 0;
					max[count][0] = i;
					max[count][1] = j;
				}
			}
		}
		}
		return largest;
}
bool isRowSolved(int lawn[100][100], bool solved[100][100], int row, int M, int currlargest)
{
	for(int i=0 ; i<M ; i++)
	{
		if(solved[row][i])
			if(lawn[row][i]>currlargest)
		return true;
	}
	return false;
}
bool isColSolved(int lawn[100][100], bool solved[100][100], int col, int N, int currlargest)
{
	for(int j=0 ; j<N ; j++)
	{
		if(solved[j][col])
			if(lawn[j][col]>currlargest)
		return true;
	}
	return false;
}
int main()
{
	int cases,M,N;
	cin>>cases;
	for(int q=0 ; q<cases ; q++)
	{
		int currlargest = 101, x, y, maxcount = 0;
		int lawn[100][100], currlawn[100][100], max[10000][2];
		bool solved[100][100];
		cin >> N >> M;
		for(int i=0 ; i<N ; i++)
		for(int j=0 ; j<M ; j++)
		{
			cin >> lawn[i][j];
			solved[i][j] = false;
		}
		int portionsMowed = 0;
		int imba=101;
		bool results = true;
		currlargest = nextLargest(lawn,max,imba,maxcount,N,M);
		for(int i=0 ; i<N ; i++)
		for(int j=0 ; j<M ; j++)
		{
			currlawn[i][j] = currlargest;
		}
		while((portionsMowed<M*N)){
			currlargest = nextLargest(lawn,max,imba,maxcount,N,M);
			if(currlargest==0)
			{
				results = false;
				break;
			}
			//values entered.. largest found
			//now mow the lawn
			for(int i=0 ; i<=maxcount ; i++)
			{
				
				if(!isRowSolved(currlawn, solved, max[i][0], M, currlargest))
				{
					for(int j=0 ; j<M ; j++)
					{
						if(!solved[max[i][0]][j])
						{
							currlawn[max[i][0]][j] = currlargest;
							if(currlawn[max[i][0]][j] == lawn[max[i][0]][j])
							{
								solved[max[i][0]][j] = true;
								portionsMowed++;
							}
						}
	
					}
				}
				else if(!isColSolved(currlawn, solved, max[i][1], N, currlargest))
				{
					for(int j=0 ; j<N ; j++)
					{
						if(!solved[j][max[i][1]])
						{
							currlawn[j][max[i][1]] = currlargest;
							if(currlawn[j][max[i][1]] == lawn[j][max[i][1]])
							{
								solved[j][max[i][1]]= true;
								portionsMowed++;
							}
						}
						
					}
				}
				else
				{
				//	cout<<"current largest :"<<currlargest;
					results = false;
					break;
				}
			}
			
			if(results==false)
			break;
			imba = currlargest;
		}
		cout<<"Case #"<<q+1<<": ";
		if(results==true)
		{
			cout<<"YES"<<endl;
			
	//	cout<<"portions mowed :"<<portionsMowed;
		}
		else
		{
			cout<<"NO"<<endl;
		}
	}
	
	
	return 0;
}
