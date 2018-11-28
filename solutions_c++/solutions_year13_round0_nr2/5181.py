#include <stdint.h>
#include <cmath>
#include <ctime>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <algorithm>
#include <map>
#include <set>
#include <boost/lexical_cast.hpp>

using namespace std;

//#define TEST

namespace {


#if defined(TEST)
	const char INPUT_FILENAME[32]	= "B-test.in";
	const char OUTPUT_FILENAME[32]	= "B-result.txt";
#else
#	if 0
	const char INPUT_FILENAME[32]	= "B-small-attempt0.in";
	const char OUTPUT_FILENAME[32]	= "B-small_result.txt";
#	else
	const char INPUT_FILENAME[32]	= "B-large.in";
	const char OUTPUT_FILENAME[32]	= "B-large_result.txt";
#	endif
#endif
	
	//------------------------------
	// split
	void split( vector<string>& list, string& str, const string& delim )
	{
		int cutAt;
		while( (cutAt = str.find_first_of(delim)) != str.npos )
		{
			if(cutAt > 0)
			{
				list.push_back(str.substr(0, cutAt));
			}
			str = str.substr(cutAt + 1);
		}
		if(str.length() > 0)
		{
			list.push_back(str);
		}
	}

	//------------------------------
	struct SInput
	{
		int N;
		int M;
		vector< vector<int> > a;

	};
}	// anonymous namespace


class CWork
{
public:	
	//------------------------------
	void exec()
	{
		m_testNum = 0;
		load();
		ofstream stream( OUTPUT_FILENAME );
		for( int i=0; i<m_testNum; ++i )
		{
#if defined(TEST)
			execImpl(i, cout);
#else
			execImpl(i, stream);
#endif
		}
	}
	
private:
	//------------------------------
	void load()
	{
		ifstream s( INPUT_FILENAME );
		string str;
		getline( s, str );
		sscanf_s( str.c_str(), "%d", &m_testNum );

		for( int loop=0; loop<m_testNum; ++loop )
		{
			SInput input;
			getline( s, str );
			sscanf_s( str.c_str(), "%d %d", &input.N, &input.M );
			for( int i=0; i<input.N; ++i )
			{
				vector<string> result;
				vector<int> a;
				getline( s, str );
				split(result, str, " ");
				for each (string s in result)
				{
					a.push_back( boost::lexical_cast<int>(s) );
				}
				input.a.push_back(a);
			}
			m_input.push_back( input );
		}
	}

	//------------------------------
	void execImpl(int index, ostream& stream)
	{
		const SInput& input = m_input[index];
		vector<int> init = vector<int>( input.M, 100 );
		vector< vector<int> > work;
		for( int i=0; i<input.N; ++i ) {
			work.push_back(init);
		}
		// â°
		for( int y=0; y<input.N; ++y ) {
			vector<int>::const_iterator ite = std::max_element(input.a[y].begin(), input.a[y].end() );
			int max = *ite;
			for( int x=0; x<input.M; ++x ) {
				if( work[y][x] > max ) {
					work[y][x] = max;
				}
			}
		}
		// èc
		for( int x=0; x<input.M; ++x ) {
			vector<int> a;
			for( int y=0; y<input.N; ++y ) {
				a.push_back(input.a[y][x]);
			}
			vector<int>::iterator ite = std::max_element(a.begin(), a.end());
			int max = *ite;
			for( int y=0; y<input.N; ++y ) {
				if( work[y][x] > max ) {
					work[y][x] = max;
				}
			}
		}
		bool result = true;		
		for( int y=0; y<input.N; ++y ) {
			if( work[y] != input.a[y] ) {
				result = false;
				break;
			}
		}

		stream << "Case #" << (index+1) << ": ";
		if( result ) {
			stream << "YES";
		}
		else {
			stream << "NO";
		}
		stream << endl;
	}

	//------------------------------
	int m_testNum;
	vector<SInput> m_input;
};

int main(int argc, char *argv[])
{
	clock_t start,end;
	start = clock();

	CWork work;
	work.exec();
	
	end = clock();
	printf( "time=%fsec\n", (double)(end-start)/CLOCKS_PER_SEC);
	getchar();
}
