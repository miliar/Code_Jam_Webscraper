#include<bits/stdc++.h>
using namespace std ;
typedef long long lll ;

namespace utility {
    template < typename T > std :: string toString( const T& n ) {
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
			if( ! ( c == ' ' || c == '\r' || c == '\n' || c == '\t' ) ) {
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

	double nextDouble() {
		char c ;
		while( true ) {
			c = nextChar() ;
			if( c == -1 ) {
				throw 404 ;
			}
			if( ! ( c == ' ' || c == '\r' || c == '\n' || c == '\t' ) ) {
				break ;
			}
		}
		if( ! ( c == '.' || c == '-' || ( c >= '0' && c <= '9' ) ) ) {
			throw 404 ;
		}
		string valString ;
		double val ;
		val = 0 ;
		valString = "" ;
		if( c == '-' ) {
			for( c = nextChar() ; ( c == '-' ) || ( c == '.' ) || ( c >= '0' && c <= '9' ) ; c = nextChar() ) {
				if( c == -1 ) {
					throw 404 ;
				}
				valString += c ;
				val = atof( valString.c_str() ) ;
			}
			return - val ;
		}
		else {
			for( ; ( c == '-' ) || ( c == '.' ) || ( c >= '0' && c <= '9' ) ; c = nextChar() ) {
				if( c == -1 ) {
					throw 404 ;
				}
			    valString += c ;
				val = atof( valString.c_str() ) ;
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
			if( ! ( c == ' ' || c == '\r' || c == '\n' || c == '\t' ) ) {
				break ;
			}
		}
		string val = "" ;
		for(  ; ! ( c == ' ' || c == '\r' || c == '\n' || c == '\t' ) ; c = nextChar() ) {
			if( c == -1 ) {
				throw 404 ;
			}
	        val += c ;
	    }
		return val ;
	}

	string nextLine() {
		char c ;
		while( true ) {
			c = nextChar() ;
			if( c == -1 ) {
				throw 404 ;
			}
			if( ! ( c == '\r' || c == '\n' ) ) {
				break ;
			}
		}
		string val = "" ;
		for(  ; ! ( c == '\r' || c == '\n' ) ; c = nextChar() ) {
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
		s += utility :: toString( d ) ;
		this -> writeString( s ) ;
	}

	void writeDoubleInNewLine( double d ) {
		this -> writeDouble( d ) ;
		this -> writeChar( '\n' ) ;
	}
} ;

class ProblemSolver {

public :

    bool check() {
        lll i ;
        for( i = 0 ; i < 10 ; i++ ) {
            if( this -> arr[ i ] <= 0 ) {
                return false ;
            }
        }
        return true ;
    }

    void initArr() {
        lll i ;
        for( i = 0 ; i < 10 ; i++ ) {
            this -> arr[ i ] = 0LL ;
        }
    }

	void solveCase( OutputWriter *owObj ) {
		lll res , i , j , a ;
        this -> initArr() ;
        i = this -> n ;
        res = -1LL ;
        for( j = 1LL ; j < 100000LL ; j++ ) {
            a = i * j ;
            while( a ) {
                this -> arr[ a % 10LL ]++ ;
                a /= 10LL ;
            }
            if( this -> check() ) {
                res = i * j ;
                break ;
            }
        }
        if( res == -1LL ) {
            owObj -> writeStringInNewLine( "Case #" + utility :: toString( this -> ind ) + ": INSOMNIA" ) ;
        }
        else {
            owObj -> writeStringInNewLine( "Case #" + utility :: toString( this -> ind ) + ": " + utility :: toString( res ) ) ;
        }
	}

	bool getInput( InputReader *irObj ) {
		lll i ;
		bool hasMoreInput ;
		hasMoreInput = true ;
		try {
			this -> n = irObj -> nextLong() ;
		}
		catch( int &ex ) {
			hasMoreInput = false ;
		}
		return hasMoreInput ;
	}

	void clearPerCase() {
		this -> incrementInd() ;
		this -> n = 0LL ;
		if( this -> CLEAR_ARRAY_PER_CASE == true ) {
            this -> clearArraysPerCase() ;
		}
	}

	void initConfigurations() {
		this -> HAS_TEST_CASES = true ;
		this -> INPUT_FILE_NAME = "al.in" ;
		this -> OUTPUT_FILE_NAME = "sample.out" ;
		this -> DO_OUTPUT_TO_FILE = true ;
		this -> CLEAR_ARRAY_PER_CASE = false ;
	}

	void incrementInd() {
		this -> ind++ ;
	}

	ProblemSolver() {
		this -> init() ;
		this -> initConfigurations() ;
	}

	void releaseMemory() {
		lll i , j ;
		delete[] this -> arr ;
		this -> arr = NULL ;
		delete[] this -> brr ;
		this -> brr = NULL ;
		delete[] this -> crr ;
		this -> crr = NULL ;
		delete[] this -> vis ;
		this -> vis = NULL ;
	}

	bool HAS_TEST_CASES ;
	string INPUT_FILE_NAME ;
	string OUTPUT_FILE_NAME ;
	bool DO_OUTPUT_TO_FILE ;
	bool CLEAR_ARRAY_PER_CASE ;

private :

	lll lim1 , lim2 , lim3 , ind , n ;
	lll *arr , *brr , *crr , *vis ;

	void precal() {
	}

	void init() {
	    this -> lim1 = 100010LL ;
        this -> lim2 = 110LL ;
        this -> lim3 = 2LL ;
        this -> ind = 0LL ;
        this -> n = 0LL ;
        this -> declareAndFillArrays() ;
        this -> precal() ;
	}

	void clearArraysPerCase() {
		lll i , j ;
		for( i = 0LL ; i < this -> lim1 ; i++ ) {
			this -> arr[ i ] = 0LL ;
			this -> brr[ i ] = 0LL ;
			this -> crr[ i ] = 0LL ;
			this -> vis[ i ] = 0LL ;
		}
	}

	void declareAndFillArrays() {
		this -> arr = new lll[ this-> lim1 ] ;
		this -> brr = new lll[ this-> lim1 ] ;
		this -> crr = new lll[ this-> lim1 ] ;
		this -> vis = new lll[ this-> lim1 ] ;
		this -> clearArraysPerCase() ;
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
