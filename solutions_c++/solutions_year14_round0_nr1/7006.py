#include<iostream>
using namespace std;

const int ROW = 4;
const int COL = 4;

void process(int mat1[ROW][COL], int mat2[ROW][COL], int t)
{
	int first = 0, second = 0, n_elem = ROW*COL, r,c;
	//Read input
	cin>>first;
	for(r = 0; r < ROW; r++) 
	{
		for(c = 0; c < COL; c++)
		{
				cin>>mat1[r][c];
		}
	}

	cin>>second;
	for(r = 0; r < ROW; r++) 
	{
		for(c = 0; c < COL; c++)
		{
				cin>>mat2[r][c];
		}
	}

	//Processing starts 
	int count = 0, num = 0;
	for(int c1 = 0; c1<COL; c1++)
	{
		for(int c2 = 0; c2<COL; c2++)
		{
			if(mat1[first-1][c1] == mat2[second-1][c2])
			{
				count++;
				num = mat1[first-1][c1];
			}
		}
	}

	cout<<"Case #"<<t<<": ";
	switch(count)
	{
	case 1:
		cout<<num;
		break;
	case 0:
		cout<<"Volunteer cheated!";
		break;
	default:
		cout<<"Bad magician!";
	}
	cout<<endl;
}

int main()
{
	int num_test = 0, t = 0;
	int mat1[ROW][COL];
	int mat2[ROW][COL];

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	//redirect cin to file
	cin >> num_test;
	
	while(t < num_test)
	{
		process(mat1,mat2,++t);
	}
}