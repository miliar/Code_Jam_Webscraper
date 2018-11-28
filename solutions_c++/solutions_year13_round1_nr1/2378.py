#include <iostream>
#include <fstream>
using namespace std;
#include <string.h>
#include <assert.h>

const char* filename = "data.txt";
const char* answerfile = "answer.txt";

const float Pi = 3.14159265359;

long long solveProblem(ifstream& instream)
{
 	char ptr[200];
 	instream.getline (ptr, 200);
	long long r = 0;
	long long t = 0;
	sscanf(ptr,"%llu %llu",&r,&t);

	// aire du cercle : pi * r * r
	long long nbCircles = 0;
	
	cout<<"T = "<<t<<endl;

	while( t > 0 )
	{
		// essaye de dessiner un cercle de rayon r:
		//float AreaBlack = Pi * r * r;
		//float AreaWhite = Pi * (r-1) * (r-1);

		//float Diff = AreaBlack - AreaWhite;
		long long Diff = 2*r + 1;

		if( t >= Diff )
		{
			nbCircles++;
		}	

		t -= Diff;
		r += 2;

		

	}	
	
	return nbCircles;
}

void writeAnswer( ofstream& outstream, int caseNum, long long answer )
{
	outstream<<"Case #"<<caseNum<<": ";
	outstream<<answer<<endl;
	cout<<answer<<endl;
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
	cout<<nbPbm<<" Problemes"<<endl;

	for( int i=0; i< nbPbm; i++ )
	{
		long long answer = solveProblem( instream );
		writeAnswer(outstream,i+1,answer);

		//instream.getline (ptr, 200); // empty line
		//cout<<ptr<<endl;
	}

	cout<<"solved"<<endl;
	return 0;
}
