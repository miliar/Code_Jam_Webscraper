#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
#include <math.h>
using namespace std;

class Data
{
	private:
		vector<char> chars;
		vector<int> c;
		bool IsThere( char c )
		{
			for( unsigned int i=0; i<this->chars.size(); i++ )
			{
				if( chars[i] != c )
					return false;
			}
		}
	public:
		void InputString( string s )
		{
			char flag;
			int tempc;

			tempc=1;
			this->chars.push_back( s[0] );

			for( int i=1; i<s.length(); i++ )
			{
				if( this->chars.back() != s[i] )
				{
					this->chars.push_back( s[i] );
					this->c.push_back( tempc );
					tempc=1;
				}
				else
				{
					tempc++;
					//cout << "tempc: " << tempc << endl;
				}
			} 

			if( this->chars.size() != this->c.size() )
			{
				this->c.push_back( tempc );
			}
		}
		string Elements( void )
		{
			unsigned int N;
			N = this->chars.size();
		
			string result;
			result = "";
			for( unsigned int i=0; i<N; i++ )
			{
				result += this->chars[i];
			}
			return result;
		}
		int Number( int i )
		{
			return c[i];
		}
};

class Set
{
	private:
		Data set[100];
		unsigned int Num;
		bool CheckElements( void )
		{
			string temp;
			temp = set[0].Elements();

			for( int i=0; i<this->Num; i++ )
			{
				if( temp != set[i].Elements() )
					return false;
			}
			return true;
		}
	public:
		void InputString( vector<string> s )
		{
			unsigned int N;
			N = s.size();
			this->Num = N;

			for( unsigned int i=0; i<N; i++ )
			{
				set[i].InputString( s[i] );
			}
		}
		bool Check( void )
		{
			return this->CheckElements();
		}
		string Elements( void )
		{
			return this->set[0].Elements();
		}
		int Move( void )
		{
			int ave, sum, len, mov;
			string e;
			e = this->Elements();
			len = e.length();
			mov = 0;

			for( int i=0; i<len; i++ )
			{
				sum = 0;
				for( int j=0; j<this->Num; j++ )
				{
					sum += this->set[j].Number(i);
				}
				//cout << "sum: " << sum << endl;
				ave = sum / this->Num;
				//cout << "ave: " << ave << endl;
				for( int j=0; j<this->Num; j++ )
				{
					mov += abs( this->set[j].Number(i) - ave );
					//cout << "mov: " << mov << endl;
				}
			}
			
			return mov;
		}
};

bool OmarWin( vector<string> s )
{
	bool result;
	string flag;

	flag = s[0];
	result = true;
	for( unsigned int i=1; i<s.size(); i++ )
	{
		if( flag != s[i] )
		{
			result = false;
		}
	}
	return result;
}

int main( int argc, char** argv )
{
	ifstream myfile;
	int T, N;
	vector<string> S;
	string temp;

	myfile.open(argv[1]);
	myfile >> T;

	for( int i=0; i<T; i++ )
	{
		Set st;
		myfile >> N;
		for( int j=0; j<N; j++ )
		{
			myfile >> temp;
			S.push_back(temp);
		}
		st.InputString( S );
		//cout << st.Elements() << endl;
		if( st.Check() == 0 )
		{
			cout << "Case #" << i+1 << ": Fegla Won" << endl;
		}
		else
		{
			cout << "Case #" << i+1 << ": " << st.Move() << endl;
		}
		S.clear();
	}

	return 0;
}

