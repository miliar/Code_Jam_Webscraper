#include <iostream>
#include <fstream>
using namespace std;
#include <string.h>
#include <assert.h>
#include <list>

const char* filename = "data.txt";
const char* answerfile = "answer.txt";

int bestAnswerSoFar = 1000000000;

// return number of steps
int solveProblem( list<int> values, int A, int nbrecurs )
{
	if( values.size() == 0 )
	{
		return 0;
	}

	if( nbrecurs > bestAnswerSoFar )
	{ 
		return bestAnswerSoFar + 100; // not the right path
	}
	

	// first eat all what he can:
	auto it = values.begin();
	int eatenMotes = 0;
	for( ; it != values.end(); it++ )
	{
		int v = *it;
		if( A > v )
		{
			// eat the mote
			A += v;
			eatenMotes++;
		}
		else
		{
			break; // can't eat anymore
		}
	}

	// how many remaining motes ?
	int remaining = values.size() - eatenMotes;
	if( remaining == 0 )
	{
		return 0; // problem solved!
	}

	list<int> addmotes;
	list<int> removemotes;
	for( ; it != values.end();  it++ )
	{
		addmotes.push_back( (*it) );
		removemotes.push_back( (*it) );
	}

	// recursively try to add or remove motes until we can fix the problem
	nbrecurs++;

	addmotes.push_front( A-1 );
	removemotes.pop_back();

	int answer2 = solveProblem(removemotes, A, nbrecurs);
	int answer1 = solveProblem(addmotes, A, nbrecurs);
	
	int best = 1 + min(answer1,answer2);

	if( nbrecurs == 0 && best < bestAnswerSoFar )
	{
		bestAnswerSoFar = best;
	}
	

	return best;
}

int solveProblem(ifstream& instream)
{
	
 	char ptr[2000000];
 	instream.getline (ptr, 200);
	int A = 0;
	int N = 0;
	sscanf(ptr,"%d %d",&A,&N);
	cout<<A<<","<<N<<endl;
	
	bestAnswerSoFar = N;

	list<int> values;
	instream.getline (ptr, 2000000);
	char* pch = strtok (ptr," ");
	int idx=0;
	while(pch != NULL )
	{
			int v = atoi(pch);
			values.push_back(v);
			idx++;
			pch = strtok (NULL," ");
			cout<<v<<" ";
	}
	cout<<endl;

	values.sort();
	int answer = solveProblem( values, A, 0 );
	return answer;
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
		int answer = solveProblem( instream );
		writeAnswer(outstream,i+1,answer);

		//instream.getline (ptr, 200); // empty line
		//cout<<ptr<<endl;
	}

	cout<<"solved"<<endl;
	return 0;
}
