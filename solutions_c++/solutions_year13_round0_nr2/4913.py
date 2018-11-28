#include <iostream>

//#define _DEBUG_

using namespace std;

const int Nmax = 100, Mmax = 100;
int a [Nmax][Mmax], max_in_row[Nmax], max_in_column[Mmax];
int N,M;

/*
bool is_wrong(int i, int j)
{
   bool r = true;

   if(i>0 && j>0)
      r = r && !(a[i][j]<a[i-1][j] && a[i][j]<a[i][j-1]);
   if(i>0 && j<M-1)
      r = r && !(a[i][j]<a[i-1][j] && a[i][j]<a[i][j+1]);
   if(i<N-1 && j<M-1)
      r = r && !(a[i][j]<a[i+1][j] && a[i][j]<a[i][j+1]);
   if(i<N-1 && j>0)
      r = r && !(a[i][j]<a[i+1][j] && a[i][j]<a[i][j-1]);

   return  !r;
}
*/

bool solve()
{
   for(int i=0; i<N; i++)
   {
      max_in_row[i] = a[i][0];
      for(int j=1; j<M; j++)
         if(max_in_row[i]<a[i][j])
            max_in_row[i]=a[i][j];
   }
   for(int j=0; j<M; j++)
   {
      max_in_column[j] = a[0][j];
      for(int i=1; i<N; i++)
         if(max_in_column[j]<a[i][j])
            max_in_column[j]=a[i][j];
   }
   for(int i=0; i<N; i++)
      for(int j=0; j<M; j++)
         //if(is_wrong(i,j))
         if(a[i][j]<max_in_column[j] && a[i][j]<max_in_row[i])
           return false;
   return true;
}

int main()
{
	int T;
	bool res;

	cin >> T;
	for(int t=1; t<=T; t++)
	{
		/************************************
		*	Input Data
		*************************************/
		cin >> N >> M;
		for(int i=0; i<N; i++)
		   for(int j=0; j<M; j++)
		      cin >> a[i][j];

		#ifdef _DEBUG_
		for(int i=0; i<N; i++)
		{
		   for(int j=0; j<M; j++)
                      cout << ' ' << a[i][j];
                   cout<<endl;
                }
                #endif
		/************************************
		*	Solve the Problem
		*************************************/
		res = solve();

		/************************************
		*	Output Results
		*************************************/
		cout << "Case #" << t << ": " << (res? "YES" : "NO") << endl;
	}

	return 0;
}
