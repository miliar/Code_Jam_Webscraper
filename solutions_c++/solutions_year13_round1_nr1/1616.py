#include "_StdAfx.h"
using namespace std;

const char* g_inname = "A-small-attempt0.in";
const char* g_outname = "A-small.out";
FILE* g_in;
FILE* g_out;
int g_nCase;

class CCase {
protected:
	int m_iCase;

public:

	bool bHasSolution;
	ullint mR, mT;
	ullint need;
	ullint drawn;
	ullint solution;

	void Solve()
	{
		drawn = 0;
		fscanf( g_in, "%llu %llu", &mR, &mT );
		ullint i=mR;
		solution = 0;
		while( 1) {
			need = 2*i+1;
			if( need > mT ) break;
			drawn++;
			mT -= need;
			i+=2;
			solution++;
		}
	}
	void PrintSolution( FILE* stream )
	{
		fprintf( stream, "Case #%d: %d\n", m_iCase, solution );
	}
	CCase( int iCase, FILE* infile ):
	m_iCase(iCase)
	{
	}
};

struct pt { int x[2]; };

int main( int argc, char** argv )
{

	g_in = fopen( g_inname, "r" );
	g_out = fopen( g_outname, "w" );
	
	fscanf( g_in, "%d", &g_nCase );

	//can parallize if needed
	CCase *pCase;
	for( int i=0; i<g_nCase; i++ ){
		printf( "Solving case %d...\n", i );
		pCase = new CCase( i+1, g_in );
		pCase->Solve();
		pCase->PrintSolution( g_out );
		pCase->PrintSolution( stdout );
		delete pCase;
	}

	fclose( g_in );
	fclose( g_out );
	
	typedef pair<int, int> node_t;
	deque<node_t> alist;
	set<node_t> aset;
	return 0;
}