#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>

using namespace std;
/*
void trow ( int* a, int  r , int c , int* b )
{
// b is the array store result
for (int i = 0; i < r; i++)
{
int count = 0;
for (int j = 0; j < c; j++)
{
if( a[i*c] >= a[i*c+j] )
count++;
}
if ( count == c)
{
for (int j = 0; j < c; j++)
{
if( a[i*c] == a[i*c+j] )
b[i*c+j] = 1;
}
}
}
}
void tcolumn ( int* a, int  r , int c , int* b )
{
// b is the array store result
for (int i = 0; i < c; i++)
{
int count = 0;
for (int j = 0; j < r; j++)
{
if( a[i] >= a[j*c+i] )
count++;
}
if (count == r){
for (int j = 0; j < r; j++)
{
if( a[i] == a[j*c+i] )
b[j*c+i] = 1;
}
}
}
}
*/
//bool check( int* result ,int  r , int c )
//{
//	for (int i = 0; i < r; i++)
//	{
//		for (int j = 0; j < c; j++)
//		{
//			if( result[i*c + j ] == 0 )
//				return false;
//		}
//	}
//	return true;
//}

bool docheck ( int *a , int r , int c  , int* rm, int* cm)
{
	int n;
	for (int i = 0; i < r; i++)
	{
		for (int j = 0; j < c; j++)
		{
			n = a[i*c+j];
			if ( n < rm[i] && n < cm[j])
				return false;
		}
	}
	return true;
}

int main(){
	ifstream in ("B-large.in");
	ofstream out ("test.out" );

	int num; 
	in >> num;
	int* all;
	int* res;
	int temp;
	int* rowmax;
	int* colmax;
	int imax;
	// impossbile for every point it's row and column both have number higher than it self.
	for (int ii = 0; ii < num; ii++)
	{
		// enter row and column
		int row;
		int column;
		in >> row;
		in >> column;
		all = new int [ row*column] ;
		//		res = new int [ row*column] ;
		for (int i = 0; i < row; i++)
		{
			for (int j = 0; j < column; j++)
			{
				in >> temp;
				all[i*column+j] = temp;
				//				res[i*column+j] = 0;
			}
		}
		//find the highest in every row and column
		rowmax = new int[row];
		colmax = new int[column];
		for (int i = 0; i < row; i++)
		{
			imax = all[i*column];
			for (int j = 0; j < column; j++)
			{
				if ( imax < all[i*column +j] )
					imax = all[i*column +j] ;
			}
			rowmax[i] = imax;
		}
		for (int i = 0; i < column; i++)
		{
			imax = all[i];
			for (int j = 0; j < row; j++)
			{
				imax = max( imax, all[j*column + i] );
			}
			colmax[i] = imax;
		}

		// compair every point with higest in it's row and column
		// connot be both greater
		if ( docheck ( all, row, column , rowmax, colmax)  )
			out<< "Case #"<<ii+1<<": YES\n";
		else
			out<< "Case #"<<ii+1<<": NO\n";


		// test all rows
		//trow(all, row, column , res );
		//tcolumn (all , row, column, res );

		//for (int i = 0; i < row; i++)
		//{
		//	for (int j = 0; j < column; j++)
		//	{
		//		cout<<res[i*column+j]<<" " ;
		//	}
		//	cout<<endl;
		//}
		//cout<<"--------------------------\n";
		//if ( check (res , row , column) )
		//	out<< "Case #"<<ii+1<<": YES\n";
		//else
		//	out<< "Case #"<<ii+1<<": NO\n";
	}
}