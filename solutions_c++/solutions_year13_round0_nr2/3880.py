#include<iostream>
#include<conio.h>
#include<stdio.h>

using namespace std;

bool rowIsSolved(int lawn[100][100], bool lawnSolved[100][100], int row, int M, int currlargest)
{
	for(int i=0 ; i<M ; i++)
	{
		if(lawnSolved[row][i])
			if(lawn[row][i]>currlargest)
		return true;
	}
	return false;
}

bool colIsSolved(int lawn[100][100], bool lawnSolved[100][100], int col, int N, int currlargest)
{
	for(int j=0 ; j<N ; j++)
	{
		if(lawnSolved[j][col])
			if(lawn[j][col]>currlargest)
		return true;
	}
	return false;
}


int largestNext(int lawn[100][100],int max[10000][2], int imbalance, int &count, int N, int M)
{
	count = 0;
	int largest=0;
	for(int i=0 ; i<N ; i++)
		{
		for(int j=0 ; j<M ; j++)
		{
			if(lawn[i][j]<imbalance)
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


int main()
{
    freopen("C:/stream/B-large.in", "r", stdin);
	freopen("C:/stream/Out-B-large.txt", "w+", stdout);

    int testCases,M,N;
	cin>>testCases;
	for(int q=0 ; q<testCases ; q++)
	{
		int currlargest = 101, x, y, maxcount = 0;
		int lawn[100][100], curr[100][100], max[10000][2];
		bool lawnSolved[100][100];
		cin >> N >> M;
		for(int i=0 ; i<N ; i++)
		for(int j=0 ; j<M ; j++)
		{
			cin >> lawn[i][j];
			lawnSolved[i][j] = false;
		}
		int mowedPortion = 0;
		int imbalance=101;
		bool results = true;
		currlargest = largestNext(lawn,max,imbalance,maxcount,N,M);
		for(int i=0 ; i<N ; i++)
		for(int j=0 ; j<M ; j++)
		{
			curr[i][j] = currlargest;
		}
		while((mowedPortion<M*N)){
			currlargest = largestNext(lawn,max,imbalance,maxcount,N,M);
			if(currlargest==0)
			{
				results = false;
				break;
			}
			//values entered.. largest found
			//now mow the lawn
			for(int i=0 ; i<=maxcount ; i++)
			{

				if(!rowIsSolved(curr, lawnSolved, max[i][0], M, currlargest))
				{
					for(int j=0 ; j<M ; j++)
					{
						if(!lawnSolved[max[i][0]][j])
						{
							curr[max[i][0]][j] = currlargest;
							if(curr[max[i][0]][j] == lawn[max[i][0]][j])
							{
								lawnSolved[max[i][0]][j] = true;
								mowedPortion++;
							}
						}

					}
				}
				else if(!colIsSolved(curr, lawnSolved, max[i][1], N, currlargest))
				{
					for(int j=0 ; j<N ; j++)
					{
						if(!lawnSolved[j][max[i][1]])
						{
							curr[j][max[i][1]] = currlargest;
							if(curr[j][max[i][1]] == lawn[j][max[i][1]])
							{
								lawnSolved[j][max[i][1]]= true;
								mowedPortion++;
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
			imbalance = currlargest;
		}
		cout<<"Case #"<<q+1<<": ";
		if(results==true)
		{
			cout<<"YES"<<endl;

	//	cout<<"portions mowed :"<<mowedPortion;
		}
		else
		{
			cout<<"NO"<<endl;
		}
	}


	return 0;
}
