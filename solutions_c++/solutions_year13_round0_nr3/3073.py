#include <iostream>
#include <fstream>
using namespace std;
#include <string.h>
#include <assert.h>
#include <gmp.h> // using bignumber gnu library http://gmplib.org/

const char* filename = "data.txt";
const char* answerfile = "answer.txt";


bool isPalyndrome(mpz_t n)
{
	char * digits = mpz_get_str (NULL, 10, n);
	int len = strlen(digits);
	for( int i=0; i< len/2; i++ )
	{
		if( digits[i] != digits[len-1-i] )
		{
			return false;
		}
	}
	return true;
}

bool isSquarePalyndrome(mpz_t n)
{	
		mpz_t rop;
		mpz_init(rop);

		mpz_sqrt(rop,n);
		cout<<"square of "<<mpz_get_str (NULL, 10, n)<<" : "<<mpz_get_str (NULL, 10, rop)<<endl;
		return isPalyndrome(rop);
}

bool isFairAndSquare(mpz_t n)
{
	if( !isPalyndrome(n) )
	{
		return false;
	}
	if( !mpz_perfect_square_p(n) ) // not a square
	{
		return false;
	}
	if( !isSquarePalyndrome(n) )
	{
		return false;
	}


	return true;
}

int solveProblem(ifstream& instream)
{
	 	char ptr[500];
 		instream.getline (ptr, 500);
		
		mpz_t MPZA;
		mpz_t MPZB;
		char* pch = strtok (ptr," ");
		mpz_init_set_str (MPZA, pch, 10 );
		pch = strtok (NULL," ");
		mpz_init_set_str (MPZB, pch, 10 );
		
		int total = 0;
		mpz_t i;
		mpz_init_set(i,MPZA);
		for(; mpz_cmp(i,MPZB) <= 0 ; mpz_add_ui(i,i,1) )
		{
			if( isFairAndSquare(i) )
			{
				total++;
				cout<<mpz_get_str(NULL, 10, i)<<endl;
			}
		}		


		return total;
}

void writeAnswer( ofstream& outstream, int caseNum, int nm )
{
	outstream<<"Case #"<<caseNum<<": "<<nm<<endl;
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
	//cout<<nbPbm<<endl;

	for( int i=0; i< nbPbm; i++ )
	{
		int answer = solveProblem( instream );
		writeAnswer(outstream,i+1,answer);
		cout<<endl;
		//int a;
		//cin>>a;
	}

	cout<<"solved"<<endl;
	return 0;
}
