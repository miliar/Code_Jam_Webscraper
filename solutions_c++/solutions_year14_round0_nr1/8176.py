#include<iostream>
#include<vector>
using namespace std;

int main()
{
int tt;
vector < int > A;
vector < int > B;
A.resize(4);
B.resize(4);
cin>>tt;
for( int ttt = 1; ttt <=tt; ttt++ )
{
	int row;
	cin>>row;
	for( int i=1;i<=4;i++)
	{
	  for ( int j = 0; j < 4; j++ )
	  {
	    int temp;
		cin>>temp;
		if(row == i )
			A[j] = temp;
	  }
	}

		cin>>row;
	for( int i=1;i<=4;i++)
	{
	  for ( int j = 0; j < 4; j++ )
	  {
	    int temp;
		cin>>temp;
		if(row == i )
			B[j] = temp;
	  }
	}

	int sol = -1,no = 0;
	for ( int i = 0; i < 4; i++ )
	{
	  for( int j = 0; j < 4; j++ )
	  {
	    if(A[i] == B[j] )
		{
		  sol = A[i];
		  no++;
		}
	  }
	}

	cout<<"Case #"<<ttt<<": ";

	if( no > 1 )
		cout<<"Bad magician!"<<endl;
	else if( no == 0 )
		cout<< "Volunteer cheated!"<<endl;
	else
		cout<<sol<<endl;
}

}