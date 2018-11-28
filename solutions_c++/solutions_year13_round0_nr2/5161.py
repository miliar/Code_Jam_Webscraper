#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

bool can_lawn (int**,int row,int colum,int n, int m,int pvt);

int main()
{
 	 freopen("B-large.in", "r", stdin);
	  freopen("ouput_large.out", "w", stdout);

	
	int n_test;
 int n ,m;
 bool test;
 cin>>n_test;
 for (int b = 1; b < n_test+1; b++)
 {
	 bool abs_test=true;

	 scanf("%d %d",&n,&m);
	 int** mat =new int*[n];
	 
	 //build mattrix
	 for (int i = 0; i < n; i++)
		 mat[i]=new int [m];
 
	 //inter data
	 for (int i = 0; i < n; i++)
	 {
		 for (int j = 0; j < m; j++)
		 {
			 scanf("%d",&mat[i][j]);
		 }
	 }

	 //serch for ones
	 for (int row = 0; row < n; row++)
	 {
		 for (int colum = 0; colum < m; colum++)
		 {
			 if(mat[row][colum] < 100)
			 {
				 test=can_lawn(mat,row,colum,n,m,mat[row][colum]);
				  if(!test)
				  {
				    abs_test=false;
				    row =n+5;
					break;
				  }
				 
			 }
		 }

	 }
	 		 if(abs_test)
    		 printf( "Case #%d: YES\n",b);
		 else
			 printf( "Case #%d: NO\n",b);

 }

}

bool can_lawn (int** mat,int row,int colum,int n,int m,int pvt)
{
 bool test=true;
 //test ofkyyyyyyyy
 for (int j = 0; j < m; j++)
 {
	 if(mat[row][j] > pvt)
	 {
	  test=false;
	  break;
	 }
 }

 if(!test)     //test ofky
 {
	 for (int i = 0; i < n; i++)
	 {
		 if(mat[i][colum] > pvt)
		 {
		   return false;
		 }
	 }
 return true;
 }

}
