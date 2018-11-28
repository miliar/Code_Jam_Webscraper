#include <fstream>
#include <vector>
#include <algorithm>
#include <ax/ax_core.h> //http://libax.googlecode.com

std::ifstream			inFile;
axFile					outFile;
std::vector<int64_t>	sq;

typedef	std::vector<int64_t>::iterator	It;

axStatus	output( int c, size_t result ) {
	axStringA_<256>	tmp;
	tmp.format("Case #{?}: {?}\n", c+1, result );
	
	outFile.writeString( tmp );
	ax_print( tmp );

	return 0;
}

axStatus	doCase( int c ) {
	axStringA	buf;

	int A, B;
	inFile >> A >> B;

	It a = std::lower_bound( sq.begin(), sq.end(), A );
	It b = std::upper_bound( sq.begin(), sq.end(), B );

	for( It p = a; p < b; p++ ) {
		ax_log_var( *p );
	}

	size_t ans = b - a;
	
	output( c, ans );
	return 0;
}

bool isFair( int64_t v ) {
	axStringA_<256>	str;
	str.convert(v);
	size_t n = str.size();
	for( size_t i=0; i<n/2; i++ ) {
		if( str[i] != str[n-i-1] ) return false;
	}
	
	return true;
}

axStatus	run() {
	axStatus	st;

	sq.reserve(10000000);

	int64_t	max_num = 1;
	
	for( int i=0; i<14; i++ ) {
		max_num *= 10;
	}
	
	axStopWatch	watch;
	axStringA_<256>	str;
	
	for( int64_t i=1; ; i++ ) {
		if( ! isFair( i ) ) continue;
		int64_t	v = i*i;
		if( v > max_num ) break;
		if( ! isFair( v ) ) continue;
		
		ax_log( "sq[{?}]  {?}^2 = {?} (len={?}) time: {?}", sq.size(), i, v, str.size(), watch.get() );
		
		sq.push_back( v );
	}
	
	inFile.open("C-small-attempt1.in");
	if( ! inFile.is_open() ) return -1;
	
	st = outFile.openWrite("out.txt", true, true);		if( !st ) return st;

	axStringA	buf;
	int C;
	inFile >> C;
	for( int c=0; c<C; c++ ) {
		st = doCase( c );			if( !st ) return st;
	}


	return 0;
}


axStatus	changeDir() {
	axStatus st;
	axStringA path;
	st = axFilePath::getDirName(path, __FILE__ );		if( !st ) return st;
	st = axFileSystem::setCurrentDir(path);				if( !st ) return st;
	return 0;
}


int main(int argc, const char * argv[]) {
	axScope_NSAutoreleasePool	pool;

	changeDir();

	axStopWatch	watch;

	axStatus st = run();
	ax_log("===== end of program [{?} s] [return {?}] =====", watch.get(), st );

    return 0;
}

