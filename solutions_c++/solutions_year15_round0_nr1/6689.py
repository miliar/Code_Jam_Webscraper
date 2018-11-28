#include<bits/stdc++.h>
using namespace std ;
typedef long long lll ;

namespace helper {
    template < typename T > std::string toString( const T& n ) {
        std :: ostringstream stm ;
        stm << n ;
        return stm.str() ;
    }
}

class InputReader {

private :

	static const int bufferSize = ( 1 << 22 ) ;
	char buffer[ bufferSize ] ;
	int bufferLength , currentIndex ;

	char nextChar() {
		if( this -> currentIndex == this -> bufferLength ) {
			memset( this -> buffer , 0 , sizeof( this -> buffer ) ) ;
			this -> bufferLength = fread( this -> buffer , sizeof( char ) , bufferSize , stdin ) ;
			if( this -> bufferLength == 0 ) {
				return -1 ;
			}
			this -> currentIndex = 0 ;
		}
		return this -> buffer[ this -> currentIndex++ ] ;
	}

public :

	InputReader() {
		this -> bufferLength = 0 ;
		this -> currentIndex = 0 ;
	}

	int nextInt() {
		return ( int ) this -> nextLong() ;
	}

	lll nextLong() {
		char c ;
		while( true ) {
			c = nextChar() ;
			if( c == -1 ) {
				throw 404 ;
			}
			if( ! ( c == ' ' || c == '\n' || c == '\t' ) ) {
				break ;
			}
		}
		if( ! ( c == '-' || ( c >= '0' && c <= '9' ) ) ) {
			throw 404 ;
		}
		lll val = 0 ;
		if( c == '-' ) {
			for( c = nextChar() ; c >= '0' && c <= '9' ; c = nextChar() ) {
				if( c == -1 ) {
					throw 404 ;
				}
			    val = val * 10LL + ( c - '0' ) ;
			}
			return - val ;
		}
		else {
			for( ; c >= '0' && c <= '9' ; c = nextChar() ) {
				if( c == -1 ) {
					throw 404 ;
				}
			    val = val * 10LL + ( c - '0' ) ;
	        }
			return val ;
		}
	}

	string nextString() {
		char c ;
		while( true ) {
			c = nextChar() ;
			if( c == -1 ) {
				throw 404 ;
			}
			if( ! ( c == ' ' || c == '\n' || c == '\t' ) ) {
				break ;
			}
		}
		string val = "" ;
		for(  ; c >= '0' && c <= '9' ; c = nextChar() ) {
			if( c == -1 ) {
				throw 404 ;
			}
	        val += c ;
	    }
		return val ;
	}

} ;

class OutputWriter {

private :

	static const int bufferSize = ( 1 << 16 ) ;
	char buffer[ bufferSize ] ;
	int currentIndex ;

	void writeChar( char c ) {
		this -> buffer[ this -> currentIndex++ ] = c ;
		if( this -> currentIndex == bufferSize ) {
		    this -> flushOutput() ;
		}
	}

public :

	void flushOutput() {
		if( this -> currentIndex > 0 ) {
			fwrite( this -> buffer , sizeof( char ) , this -> currentIndex , stdout ) ;
		}
		this -> currentIndex = 0 ;
	}

	void writeString( string s ) {
		int i , len ;
		len = s.length() ;
		for( i = 0 ; i < len ; i++ ) {
			this -> writeChar( s[ i ] ) ;
		}
	}

    void writeStringInNewLine( string s ) {
		this -> writeString( s ) ;
        this -> writeChar( '\n' ) ;
	}

    void writeSpace() {
        this -> writeChar( ' ' ) ;
    }

    void writeNewLine() {
        this -> writeChar( '\n' ) ;
    }

	void writeInt( int n ) {
		if( n >= 10 ) {
		    this -> writeInt( n / 10 ) ;
		}
		this -> writeChar( '0' + n % 10 ) ;
	}

	void writeIntInNewLine( int n ) {
		this -> writeInt( n ) ;
		this -> writeChar( '\n' ) ;
	}

	void writeLong( lll n ) {
		if( n >= 10LL ) {
		    this -> writeInt( n / 10LL ) ;
		}
		this -> writeChar( '0' + n % 10LL ) ;
	}

	void writeLongInNewLine( lll n ) {
		this -> writeLong( n ) ;
		this -> writeChar( '\n' ) ;
	}

	void writeDouble( double d ) {
		string s = "" ;
		s += d ;
		this -> writeString( s ) ;
	}
} ;

class ProblemSolver {

public :

	void solveCase( OutputWriter *owObj ) {
		lll res , i , j , a ;
		res = 0 ;
		a = 0 ;
		for( i = 0 ; i < n + 1 ; i++ ) {
            if( a >= i ) {
            }
            else {
                res++ ;
                a++ ;
            }
            a += ( this -> s[ i ] - '0' ) ;
		}
		owObj -> writeStringInNewLine( "Case #" + helper :: toString( this -> ind ) + ": " + helper :: toString( res ) ) ;
	}

	bool getInput( InputReader *irObj ) {
		lll i ;
		bool hasMoreInput ;
		hasMoreInput = true ;
		try {
			this -> n = irObj -> nextLong() ;
			this -> s = irObj -> nextString() ;
		}
		catch( int &ex ) {
			hasMoreInput = false ;
		}
		return hasMoreInput ;
	}

	void clearPerCase() {
		this -> incrementInd() ;
		this -> incrementCc() ;
		this -> n = 0 ;
		this -> cn = 0 ;
		this -> clearArraysPerCase() ;
	}

	bool HAS_TEST_CASES = true ;
	string INPUT_FILE_NAME = "a2.in" ;
	string OUTPUT_FILE_NAME = "a.out" ;
	bool DO_OUTPUT_TO_FILE = true ;
	bool CLEAR_ARRAY_PER_CASE = false ;

	void incrementInd() {
		this -> ind++ ;
	}

	void setCn( int c ) {
		this -> cn = c ;
	}

	void incrementCn() {
		this -> cn++ ;
	}

	void incrementCc() {
		this -> cc++ ;
	}

	int getCn() {
		return this -> cn ;
	}

	ProblemSolver() {
		this -> init() ;
	}

	void releaseMemory() {
		lll i , j ;
		delete[] this -> arr ;
		this -> arr = NULL ;
		delete[] this -> brr ;
		this -> brr = NULL ;
		delete[] this -> vis ;
		this -> vis = NULL ;
		for( i = 0 ; i < this -> lim2 ; i++ ) {
			delete[] this -> memo[ i ] ;
			this -> memo[ i ] = NULL ;
			delete[] this -> done[ i ] ;
			this -> done[ i ] = NULL ;
		}
		delete[] this -> memo ;
		this -> memo = NULL ;
		delete[] this -> done ;
		this -> done = NULL ;
		delete[] this -> adjList ;
		this -> adjList = NULL ;
	}

private :

	lll lim1 , lim2 , cc , ind , c , cn , n ;
	lll *arr , *brr , *vis ;
	lll **memo , **done ;
	vector< lll > *adjList ;
	string s ;

	void init() {
	    this -> lim1 = 100010 ;
        this -> lim2 = 110 ;
        this -> cc = 1 ;
        this -> ind = 0 ;
        this -> n = 0 ;
        this -> cn = 0 ;
        this -> declareAndFillArrays() ;
	}

	void clearArraysPerCase() {
		lll i , j ;
		for( i = 0 ; i < this -> lim2 ; i++ ) {
			this -> adjList[ i ].clear() ;
		}
	}

	void declareAndFillArrays() {
		lll i , j ;
		this -> arr = new lll[ this-> lim1 ] ;
		memset( this -> arr , 0 , sizeof( this -> arr ) ) ;
		this -> brr = new lll[ this-> lim1 ] ;
		memset( this -> brr , 0 , sizeof( this -> brr ) ) ;
		this -> vis = new lll[ this-> lim1 ] ;
		memset( this -> vis , 0 , sizeof( this -> vis ) ) ;
		this -> memo = new lll*[ this-> lim2 ] ;
		this -> done = new lll*[ this-> lim2 ] ;
		for( i = 0 ; i < this -> lim2 ; i++ ) {
			this -> memo[ i ] = new lll[ this-> lim2 ] ;
			this -> done[ i ] = new lll[ this-> lim2 ] ;
		}
		this -> adjList = new vector< lll >[ this -> lim1 ] ;
	}

} ;

class CodeExecutioner {

private :

	ProblemSolver *psObj ;
	InputReader *irObj ;
	OutputWriter *owObj ;

	void runCases() {

		int T , ind ;
		bool hasMoreInput ;
		try {
			if( ifstream( this -> psObj -> INPUT_FILE_NAME.c_str() ) != 0 ) {
				freopen( this -> psObj -> INPUT_FILE_NAME.c_str() , "r" , stdin ) ;
			}
			if( this -> psObj -> DO_OUTPUT_TO_FILE == true ) {
				freopen( this -> psObj -> OUTPUT_FILE_NAME.c_str() , "w" , stdout ) ;
			}
		}
		catch( exception ex ) {
			throw ex ;
		}
		try {
			if( this -> psObj -> HAS_TEST_CASES == true ) {
				//for input with test cases
				T = this -> irObj -> nextInt() ;
				for( ind = 1 ; ind <= T ; ind++ ) {
					this -> psObj -> clearPerCase() ;
					this -> psObj -> getInput( this -> irObj ) ;
					this -> psObj -> solveCase( this -> owObj ) ;
				}
			}
			else {
				//for end of file input
				for( ind = 1 ; ; ind++ ) {
					this -> psObj -> clearPerCase() ;
					hasMoreInput = this -> psObj -> getInput( this -> irObj ) ;
					if( hasMoreInput == false ) {
						break ;
					}
					this -> psObj -> solveCase( this -> owObj ) ;
				}
			}
			this -> psObj -> releaseMemory() ;
		}
		catch( exception &ex ) {
			throw ex ;
		}
		this -> owObj -> flushOutput() ;
	}

	void init() {
		this -> psObj = new ProblemSolver() ;
    	this -> irObj = new InputReader() ;
    	this -> owObj = new OutputWriter() ;
    	this -> runCases() ;
	}

public :

	CodeExecutioner() {
    	this -> init() ;
	}
} ;

int main() {
    new CodeExecutioner() ;
    return 0 ;
}
