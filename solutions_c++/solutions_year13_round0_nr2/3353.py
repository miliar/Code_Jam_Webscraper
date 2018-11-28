#include <iostream>
#include <fstream>
using namespace std;
#include <string.h>
#include <assert.h>

const char* filename = "data.txt";
const char* answerfile = "answer.txt";


bool isImpossible()
{
}

bool solveProblem(ifstream& instream)
{
	// read the data in this array
	char ptr[1000];
 	instream.getline (ptr, 1000);
	int N,M;
	sscanf(ptr,"%d%d",&N,&M);  // size of the array
	int** board = new int*[N+2]; // board[row][column]
	// to avoid border problem make it +2	
	for( int i=0; i<N+2; i++ )
	{
		board[i] = new int[M+2];
		for( int j=0; j< M+2; j++ )
		{
			board[i][j] = 0;
		}
	}

	for( int i=1; i<=N; i++ )
	{
		instream.getline (ptr, 1000);
		char* pch = strtok (ptr," ");
		for( int j = 1; j<= M; j++ )
		{
			assert(pch!=NULL);
			int v = atoi(pch);
			board[i][j] = v;
			pch = strtok (NULL," ");
		}
	}

 	// copie the values at the edges:
	for( int i=0; i<N+2; i++ )
	{		
		board[i][0] = board[i][1];
		board[i][M+1] = board[i][M];
	}
	for( int j=0; j<M+2; j++ )
	{
		board[0][j] = board[1][j];
		board[N+1][j] = board[N][j];
	}

	for( int i=1; i<N+1; i++ )
	{
		for( int j=1; j< M+1; j++ )
		{
			cout<<board[i][j]<<" ";
		}
		cout<<endl;
	}

	for( int i=1; i<= N; i++ )
	{
		for( int j=1; j<=M; j++ )
		{
			// if the case is smaller than one of his neighbor horizontally and vertically, its 
			// not possible to solve.
			int v = board[i][j];
			// check on the whole line 'of course' hum
			for( int k = 1; k<= M; k ++ )
			{
				if( v< board[i][k] )
				{
					// check on the column
					for( int m=1; m <= N; m++ )
					{
							if( v < board[m][j] )
							{
								return false;
							}
					}	
				}
			}
		}
	}

	for( int i=0; i<N+2; i++ )
	{
		delete[] board[i];
	}
	delete[] board; // I should delete before the other returns..	
	return true;
}

void writeAnswer( ofstream& outstream, int caseNum, bool possible )
{
	outstream<<"Case #"<<caseNum<<": ";
	if( possible )
	{
		outstream<<"YES"<<endl;
		cout<<"YES"<<endl;
	}
	else
	{
		outstream<<"NO"<<endl;
		cout<<"NO"<<endl;
	}
}

int main()
{
	ifstream instream;
	instream.open (filename, ifstream::in );
	if( ! instream.good() )
	{
		cout<<"couldn't open "<<filename<<endl;
		return 0;
	}

	ofstream outstream;
	outstream.open (answerfile, ifstream::out );
	if( ! outstream.good() )
	{
		cout<<"couldn't open "<<answerfile<<endl;
		return 0;
	}

  char ptr[200];
  instream.getline (ptr, 200);
	int nbPbm = 0;
	sscanf(ptr,"%d",&nbPbm);
	cout<<nbPbm<<endl;

	for( int i=0; i< nbPbm; i++ )
	{
		bool answer = solveProblem( instream );
		writeAnswer(outstream,i+1,answer);
		cout<<endl;
		//int a;
		//cin>>a;
	}

	cout<<"solved"<<endl;
	return 0;
}
